import random
import time
import paramiko

from comMon.Log import MyLog as Log

log = Log.get_log()
mylogger = log.get_logger()
import readConfig as readConfig

dir = readConfig.proDir
localReadConfig = readConfig.ReadConfig()
def get_number():
    # 第二位数字

    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999,100000000)

    # 拼接手机号
    number="1{}{}{}".format(second, third, suffix)
    mylogger.info("随机生成手机号为：%s"%number)
    return number


def test_MigPc():
    """
    获得PC sit环境图形验证码
    :return:
    """
    command=  r' cd /opt/front/logs/; tail -2f catalina.out'
    s=test_Verificationcode(command)
    return s


def test_PcCode(cellphone):
    """
    获得PC  SIT环境的短信验证码
    :param cellphone:
    :return:
    """
    command = r'cd /opt/front/logs/; grep -A 1 "comMon.laqu.front.controller.user.SMSController -sms_code :注册短信  手机号码：%s"  catalina.out' % (cellphone)
    s=test_Verificationcode(command,cellphone)
    return s

def test_H5code(cellphone):
    """
    获得H5 SIT 环境的短信验证码
    :param cellphone:
    :return:
    """
    tim = time.strftime("%Y-%m-%d", time.localtime())
    command =  r' cd /opt/mop/logs/%s; grep -A 1 "%s"  info-log.log' % (tim, cellphone)
    s = test_Verificationcode(command, cellphone)
    return s

def pre_Magpc(value):
    command= r'cd /opt/apache-tomcat/logs; grep -A 1 " 注册图形验证码内容 token:%s"  catalina.out'%(value)
    cellphone=""
    s=prePc_Verificationcode(command,cellphone)
    return s

def pre_H5code(cellphone):
    comand = 'cd /opt/mop/logs ; grep -A 1 "%s" catalina.out' % (cellphone)
    s =pre_Verificationcode(comand,cellphone)
    return  s

def pre_PcCode(cellphone):
    command = r'cd /opt/apache-tomcat/logs; grep -A 1 " com.laqu.front.controller.user.SMSController -sms_code :注册短信  手机号码：%s" catalina.out' %(cellphone)
    s = prePc_Verificationcode(command, cellphone)
    return s


def test_Verificationcode(command,cellphone):

    try:
        hostname = localReadConfig.get_H5testSSL("hostname")
        port = localReadConfig.get_H5testSSL("port")
        username = localReadConfig.get_H5testSSL("username")
        password = localReadConfig.get_H5testSSL("password")
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.load_system_host_keys()
        s.connect(hostname, port, username, password)

        #command = r'cd /opt/front/logs/; grep -A 1 "comMon.laqu.front.controller.user.SMSController -sms_code :注册短信  手机号码：%s"  catalina.out' % (cellphone)
        # command = r' cd /opt/mop/logs; grep -A 1 "手机号码：' + cellphone + '"  catalina.out'
        stdin, stdout, stderr = s.exec_command(command)
        logs = stdout.readlines()  # 缓存流中读取
        i = 0
        for i in range(len(logs)):  # 循环日志的
            # print(logs[i].rstrip())
            i = i + 1
            if i == len(logs):
                srt = logs[i - 1].rstrip()
                if cellphone=="":
                    mylogger.info("SIT-PC环境获得图形验证码:" +srt[-4:])
                    return  srt[-4:]
                else:
                    mylogger.info("PC-SIT环境手机号=%s 获取的注册验证码:" % (cellphone) + srt[-6:])
                # print(srt[-6:])  # 截取倒数第6位到结尾
                    return srt[-6:]
    except Exception as  e:
        mylogger.error(e)
    finally:
        s.close()



# def databaseTable(sql):
#     connect = pymysql.Connect(
#         host="192.168.1.194", user="laqu", passwd="laqu", port=3306, charset='utf8'
#     )
#     cursor = connect.cursor()
#     # 查询数据
#     cursor.execute(sql)  # 执行sql
#     connect.commit()
#
#     if cursor.rowcount == 0:
#         print("数据库中没有找到你要的值")
#         return 0
#     else:
#         data = cursor.fetchall()
#         return data
#     cursor.close()


# def appLoginregister(phone):
#     myPyDate = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#     pwd="5ef962cdf5700cc8e97e3660ca065e72"
#     app_key = "689cf76eb3c96b7cb3ddb07e4e5efe54"
#     api_key=pwd+"app_key="+app_key+"&date="+myPyDate+pwd
#     sql="SELECT MD5('"+api_key+"')"
#     md5_api_key=databaseTable(sql)[0][0]
#
#     #获取token
#     dataCont = {
#         "api_sign":md5_api_key,\
#         "app_key":app_key,\
#         "date":myPyDate
#     }
#     rustul=requests.get(url="http://192.168.1.177/mop/token/get",params=dataCont).json()
#     token=rustul["data"]
#     #发送短信
#     list=[token,app_key,phone,myPyDate]
#     list=sorted(list)#升序 a>z
#     #list.reverse()#反转 z>a
#     separator = '&'
#     data_joined = separator.join(list) #获得降序排列后的字符串组合
#     print(data_joined)
#     new_api_key = pwd+data_joined+pwd
#     md5_api_key=databaseTable("select md5('"+new_api_key+"')")[0][0]
#     print("md5_api_key:",md5_api_key)
#     paramscode={
#         "token":token,\
#         "phone":phone,\
#         "api_sign":md5_api_key,\
#         "app_key":app_key,\
#         "date":myPyDate
#     }
#     print("参数：",paramscode)
#     code=requests.get(url="http://192.168.1.177/mop/sms/register/send",params=paramscode).json()
#     print(code)
def prePc_Verificationcode(comand,cellphone):
    """
     :return:验证码

    """

    try:
        hostname = localReadConfig.get_PCpreSSL("hostname")
        port = localReadConfig.get_PCpreSSL( "port")
        username = localReadConfig.get_PCpreSSL("username")
        key_path = localReadConfig.get_PCpreSSL("key_path")

        private_key = paramiko.RSAKey.from_private_key_file(dir + key_path)
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        mylogger.info("连接成功UAT服务器：%s "%hostname)
        # 连接服务器
        ssh.connect(hostname=hostname, port=port, username=username, pkey=private_key)
        # 执行命令

        stdin, stdout, stderr = ssh.exec_command(comand)
        # 获取命令结果
        #result = stdout.read()

        logs = stdout.readlines()
        # 打印输出
        #print(result.decode())
        i = 0
        for i in range(len(logs)):  # 循环日志的
            # mylogger.info(logs[i].rstrip())
            i = i + 1
            if i == len(logs):
                srt = logs[i - 1].rstrip()
              #  mylogger.info(srt[-6:])  # 截取倒数第6位到结尾
                if cellphone=="":
                    mylogger.info("UAT-PC环境获得图形验证码:"+ srt[-4:])
                    return srt[-4:]
                else:
                    mylogger.info("UAT-PC环境手机号=%s 获取的注册验证码:" % (cellphone) + srt[-6:])
                    return srt[-6:]
    except Exception as  e:
        mylogger.error(e)
    finally:
        ssh.close()



def pre_Verificationcode(comand,cellphone):
    """
     :return 验证码

    """
    try:
        hostname = localReadConfig.get_H5preSSL("hostname")
        port =localReadConfig.get_H5preSSL("port")
        username =localReadConfig.get_H5preSSL("username")
        key_path = localReadConfig.get_H5preSSL("key_path")

        private_key = paramiko.RSAKey.from_private_key_file(dir + key_path)
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=hostname, port=port, username=username, pkey=private_key)
        # 执行命令


        stdin, stdout, stderr = ssh.exec_command(comand)
        # 获取命令结果
        # result = stdout.read()
        logs = stdout.readlines()
        # 打印输出
        # print(result.decode())
        i = 0
        for i in range(len(logs)):  # 循环日志的
            # mylogger.info(logs[i].rstrip())
            i = i + 1
            if i == len(logs):
                srt = logs[i - 1].rstrip()
                mylogger.info(srt[-6:])  # 截取倒数第6位到结尾
                mylogger.info("UAT-H5环境手机号=%s 获取的注册验证码:" % (cellphone) + srt[-6:])
                return srt[-6:]
    except Exception as  e:
        mylogger.error(e)
    finally:
        ssh.close()