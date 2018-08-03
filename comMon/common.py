import json

from xml.etree import ElementTree as ElementTree

import requests
import urllib3
import xlrd
from xlrd import open_workbook

import readConfig as readConfig
from comMon.Log import MyLog as Log
from comMon import configHttp as configHttp

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


urllib3.disable_warnings()
localReadConfig = readConfig.ReadConfig()
proDir = readConfig.proDir
localConfigHttp = configHttp.ConfigHttp()
log = Log.get_log()
logger = log.get_logger()

caseNo = 0


# def get_visitor_token():
#     """
#     create a token for visitor
#     :return:
#     """
#     host = localReadConfig.get_http("BASEURL")
#     response = requests.get(host+"/v2/User/Token/generate")
#     info = response.json()
#     token = info.get("info")
#     logger.debug("Create token:%s" % (token))
#     return token


# def set_visitor_token_to_config():
#     """
#     set token that created for visitor to config
#     :return:
#     """
#     token_v = get_visitor_token()
#     localReadConfig.set_headers("TOKEN_V", token_v)


def get_value_from_return_json(json, name1, name2):
    """
    get value by key
    :param json:
    :param name1:
    :param name2:
    :return:
    """
    info = json['info']
    group = info[name1]
    value = group[name2]
    return value


def show_return_msg(response):
    """
    详情显示返回的JSON的MSG内容
    :param response:
    :return:
    """
    url = response.url
    msg = response.text
    print("\n请求地址：" + url)
    # 可以显示中文
    print("\n返回参数：" + '\n' + json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))


# ****************************** read testCase excel ********************************

def get_xls(xls_name, sheet_name):
    """
    获得excel中指定名称的所有数据
    :param xls_name：excel的名称
    :param sheet_name：excel中的分组名称
    :return:excel中的数据的集合 数组形式储存每一个数据
    """

    cls = []

    xlsPath = os.path.join(proDir, "testFile", 'case', xls_name)  # 从根路径中打开testFile文件夹case中的excel数据存放的路径
    print(xlsPath)
    file = open_workbook(xlsPath)  # 打开这个数据存放文件

    sheet = file.sheet_by_name(sheet_name)  # 对应的excel的名称

    nrows = sheet.nrows  # 获得当前的数据的行数
    for i in range(nrows):
        if sheet.row_values(i)[0] != 'case_name':  # 如果当前第一条数据不是 case_name ;就是剔除第一条数据用的，参数名称用的。
            cls.append(sheet.row_values(i))  # 就把剩下的值提取出来,添加集合

    return cls


# ****************************** read SQL xml ********************************

database = {}  # 默认配置为空


def set_xml():  #
    """
    set sql xml
    :return:解析SQL.xml中内容
    """
    # 下面判断就是先考虑最外层解析的database,在解析中层的table 最后解析最底层的ID标识
    if len(database) == 0:  # 如果数据集合为空时
        sql_path = os.path.join(proDir, "testFile", "SQL.xml")  # 打开配置文件地址
        tree = ElementTree.parse(sql_path)  # 解析配文件
        for db in tree.findall("database"):  # 全局解析XML中database属性
            db_name = db.get("name")  # 解析获得每一个database属性的table属性中的名称
            # print(db_name)
            table = {}
            for tb in db.getchildren():  # 获得解析的database的子属性
                table_name = tb.get("name")  # 获得table子属性的标识名
                # print(table_name)
                sql = {}
                for data in tb.getchildren():  # 获得table子属性的标识名
                    sql_id = data.get("id")  # 获得id子属性的标识名
                    # print(sql_id)
                    sql[sql_id] = data.text  # 得到对应ID属性的内容
                table[table_name] = sql  # 得到对应table属性的内容
            database[db_name] = table  # 得到对应的的数据库中内容


def get_xml_dict(database_name, table_name):
    """
    :param database_name: 获得SQL.xml的database的名称
    :param table_name:获得数据库名称对应的table的名称
    :return:database_dict 返回SQL的集合
    """
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict  # 获得当前datbase下table的所有SQL的集合


def get_sql(database_name, table_name, sql_id):
    """
    获得指定的SQL语句
    :param database_name:get SQL.xml by given database's name
    :param table_name:get SQL.xml by given table's name
    :param sql_id:The SQL.xml for sql_index
    :return:sql
    """
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql


# ****************************** read interfaceURL xml ********************************


def get_url_from_xml(name):
    """
    By name get url from interfaceURL.xml
    :param name: interface's url name
    :return: url
    """
    url_list = []
    url_path = os.path.join(proDir, 'testFile', 'interfaceURL.xml')
    tree = ElementTree.parse(url_path)
    for u in tree.findall('url'):
        url_name = u.get('name')
        if url_name == name:
            for c in u.getchildren():
                url_list.append(c.text)

    url = '/'.join(url_list)
    return url


# ****************************** get cookies  ********************************
def get_cookies(nick, password):
    """
    get_cookies
    :param nick:
    :param password:
    :return:cookies
    """
    try:
        urllib3.disable_warnings()
        #             禁用ub3的SLL安全整数Warning提示
        session = requests.session()
        data1 = {"memberType": "1", 'nick': nick, 'password': password}
        scheme = localReadConfig.get_http("scheme")
        host = localReadConfig.get_http("baseurl")
        loginurl = scheme + '://' + host + get_url_from_xml("userLogin")
        session.post(loginurl, data=data1, verify=False)
        cookies = requests.utils.dict_from_cookiejar(session.cookies)

        if cookies == "":
            logger.error("*****you nick or password error********")
            return None
        return cookies
    except TimeoutError:
        logger.error("Time out!")
        return None
    finally:
        session.close()


def readExcel(fileName, SheetName):
    """

    :param fileName:
    :param SheetName:
    :return:data
    """
    try:
        xlsPath = os.path.join(proDir, "testFile", 'case', fileName)
        data = xlrd.open_workbook(xlsPath)

        table = data.sheet_by_name(SheetName)
        # 获取总行数、总列数
        nrows = table.nrows
        ncols = table.ncols
        if nrows > 1:
            # 获取第一列的内容，列表格式
            keys = table.row_values(0)  # print(keys)

            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, nrows):
                values = table.row_values(col)
                # keys，values这两个列表一一对应来组合转换为字典
                api_dict = dict(zip(keys, values))
                # print(api_dict)
                listApiData.append(api_dict)

            return listApiData

        else:
            print("表格未填写数据")
            return None
    except Exception as e:
        logger.error(e)
