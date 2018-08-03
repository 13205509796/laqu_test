# coding=utf-8
import sys
import os
curPath = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(curPath)
import unittest
import comMon.publicClass as publicClass

from nose.plugins.attrib import attr
from comMon.common import readExcel
from ddt import ddt, data
import readConfig as readConfig
import nose
localReadConfig = readConfig.ReadConfig()
page= "merchantRegister"
name="laquUser.xlsx"
laquUser_xls = readExcel(name,page)
from  TestCase.bases import intface

@ddt
class Test_userRegister(intface.intFaceTest):

    print("--------商家注册用例开始执行-----")
    def setUp(self):
        pass
    def tearDown(self):
       pass


    @data(*laquUser_xls)
    def test_merchantReister0001(self, data):
        try:

            if data["cellphone"] == "1":
                cellphone = publicClass.get_number()
            else:
                cellphone = data["cellphone"]
            self.driver.get(self.url+"/register/first/valid?memberType=2")
            token = self.driver.find_element_by_id("tonkenNum").get_attribute("value")
            self.driver.find_element_by_class_name("phone_num").send_keys(cellphone)
            self.driver.find_element_by_class_name("imgcodesrc").click()
            if data["picmsg"] == "1":
                pigcode = publicClass.pre_Magpc(token)
            else:
                pigcode = data["picmsg"]
            self.driver.find_element_by_id("imgcode").send_keys(pigcode)
            self.driver.find_element_by_class_name("getcode").click()
            if data["type"] == "1":
                if data["code"] == "1":
                    code = publicClass.pre_PcCode(cellphone)
                else:
                    code = data["code"]
                self.driver.find_element_by_id("message_code").send_keys(code)
                self.driver.find_element_by_class_name("submit_btn").click()
            if data["msg"] == "设置登录密码":
                test = self.driver.find_element_by_xpath('//*[@id="my_from"]/div/p[1]').text
                self.assertEqual(test, data["msg"])
            elif data["msg"] == "短信验证码不正确！":
                test = self.driver.find_element_by_class_name("error").text
                self.assertEqual(test, data["msg"])
                test2 = self.driver.find_element_by_class_name("system_error").text
                self.assertEqual(test2, data["msg"])
            else:
                msg = self.driver.find_element_by_class_name("errortype").text
                self.assertEqual(msg, data["msg"])
            #print("%s:pass" % data["case_name"])
            self.logger.info("%s:pass" % data["case_name"])
        except Exception as e:
            print("\n\n测试用例Excel名称:%s,\n页码:%s,\n用例数据:%s行，\n用例名称:%s ,\n结果:Failure" % (name,page,data["id"],data["case_name"]))
            raise self.logger.error(e)

    def test_demo(self):
        pass
if __name__ == '__main__':
    unittest.main