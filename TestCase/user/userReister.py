# coding=utf-8
import time
import unittest

import comMon.publicClass as publicClass
from  TestCase.bases import intface


class userRegister(intface.intFaceTest):




    def test_userReister_search00001(self):
        try:
            cellphone="1320550979"
            case_name="当手机号不足11位数的时候"
            self.driver.get("https://pre.laqu.comMon/register/first/valid?memberType=1")
            token = self.driver.find_element_by_id("tonkenNum").get_attribute("value")
            self.driver.find_element_by_class_name("phone_num").send_keys(cellphone)
            self.driver.find_element_by_class_name("imgcodesrc").click()
            self.driver.find_element_by_class_name("imgcodesrc").click()
            pigcode = publicClass.pre_Magpc(token)
            self.driver.find_element_by_id("imgcode").send_keys(pigcode)
            self.driver.find_element_by_class_name("getcode").click()
            errortype=self.driver.find_element_by_class_name("errortype").text
            self.assertEqual(errortype,"手机号格式错误")
            print("%s:PASS"%case_name)
        except AssertionError as e:
            self.browser.get_windows_img("saerch0001-手机号格式")
            print(e)
    def test_userReister_search00002(self):
        try:
            cellphone = ""
            case_name = "当手机号为空的时候"
            self.driver.get("https://pre.laqu.comMon/register/first/valid?memberType=1")
            token = self.driver.find_element_by_id("tonkenNum").get_attribute("value")
            self.driver.find_element_by_class_name("phone_num").send_keys(cellphone)
            self.driver.find_element_by_class_name("imgcodesrc").click()
            self.driver.find_element_by_class_name("imgcodesrc").click()
            pigcode = publicClass.pre_Magpc(token)
            self.driver.find_element_by_id("imgcode").send_keys(pigcode)
            self.driver.find_element_by_class_name("getcode").click()
            errortype = self.driver.find_element_by_class_name("errortype").text
            self.assertEqual(errortype, "手机号不能为空")
            print("%s:PASS" % case_name)
        except AssertionError as e:
            self.browser.get_windows_img("saerch0002-手机号格式")
            print(e)

    def test_userReister_search00003(self):
        try:
            cellphone = "12345678910"
            case_name = "当手机号格式错误时"
            self.driver.get("https://pre.laqu.comMon/register/first/valid?memberType=1")
            token = self.driver.find_element_by_id("tonkenNum").get_attribute("value")
            self.driver.find_element_by_class_name("phone_num").send_keys(cellphone)
            self.driver.find_element_by_class_name("imgcodesrc").click()
            self.driver.find_element_by_class_name("imgcodesrc").click()
            pigcode = publicClass.pre_Magpc(token)
            self.driver.find_element_by_id("imgcode").send_keys(pigcode)
            self.driver.find_element_by_class_name("getcode").click()
            errortype = self.driver.find_element_by_class_name("errortype").text
            self.assertEqual(errortype, "手机号格式错误")
            print("%s:PASS" % case_name)
        except AssertionError as e:
            self.browser.get_windows_img("saerch0003-手机号格式")
            print(e)
    def test_userReister_search00004(self):
        try:
            cellphone = publicClass.get_number()
            case_name = "当图片验证码为空时"
            self.driver.get("https://pre.laqu.comMon/register/first/valid?memberType=1")
            token = self.driver.find_element_by_id("tonkenNum").get_attribute("value")
            self.driver.find_element_by_class_name("phone_num").send_keys(cellphone)
            self.driver.find_element_by_class_name("imgcodesrc").click()
            self.driver.find_element_by_class_name("imgcodesrc").click()
            pigcode = ""
            self.driver.find_element_by_id("imgcode").send_keys(pigcode)
            self.driver.find_element_by_class_name("getcode").click()
            errortype = self.driver.find_element_by_class_name("errortype").text
            self.assertEqual(errortype, "请先输入正确的图像验证码!")
            print("%s:PASS" % case_name)
        except AssertionError as e:
            self.browser.get_windows_img("saerch0004-图片验证码")
            print(e)

    def test_userReister_search00005(self):
        try:
            cellphone = publicClass.get_number()
            case_name = "当图形验证验证码为错误时"
            self.driver.get("https://pre.laqu.comMon/register/first/valid?memberType=1")
            token = self.driver.find_element_by_id("tonkenNum").get_attribute("value")
            self.driver.find_element_by_class_name("phone_num").send_keys(cellphone)
            self.driver.find_element_by_class_name("imgcodesrc").click()
            self.driver.find_element_by_class_name("imgcodesrc").click()
            pigcode = "abcd"
            self.driver.find_element_by_id("imgcode").send_keys(pigcode)
            self.driver.find_element_by_class_name("getcode").click()
            errortype = self.driver.find_element_by_class_name("errortype").text
            self.assertEqual(errortype, "图形验证码填写不正确")
            print("%s:PASS" % case_name)
        except AssertionError as e:
            self.browser.get_windows_img("saerch0005-图片验证码")
            print(e)

    def test_userReister_search00006(self):
        try:
            cellphone = publicClass.get_number()
            case_name = "当图形验证验证码不足四位时"
            self.driver.get("https://pre.laqu.comMon/register/first/valid?memberType=1")

            self.driver.find_element_by_class_name("phone_num").send_keys(cellphone)
            self.driver.find_element_by_class_name("imgcodesrc").click()
            self.driver.find_element_by_class_name("imgcodesrc").click()
            pigcode = "abc"
            self.driver.find_element_by_id("imgcode").send_keys(pigcode)
            self.driver.find_element_by_class_name("getcode").click()
            errortype = self.driver.find_element_by_class_name("errortype").text
            self.assertEqual(errortype, "请先输入正确的图像验证码!")
            print("%s:PASS" % case_name)
        except AssertionError as e:
            self.browser.get_windows_img("saerch0006-图片验证码")
            raise print(e)


    def test_userReister_search00007(self):
        try:
            cellphone = publicClass.get_number()
            case_name = "当短信验证码为空时"
            self.driver.get("https://pre.laqu.comMon/register/first/valid?memberType=1")
            token = self.driver.find_element_by_id("tonkenNum").get_attribute("value")
            self.driver.find_element_by_class_name("phone_num").send_keys(cellphone)
            self.driver.find_element_by_class_name("imgcodesrc").click()
            self.driver.find_element_by_class_name("imgcodesrc").click()
            pigcode = publicClass.pre_Magpc(token)
            self.driver.find_element_by_id("imgcode").send_keys(pigcode)
            self.driver.find_element_by_class_name("getcode").click()

            code = ""
            self.driver.find_element_by_id("message_code").send_keys(code)
            self.driver.find_element_by_class_name("submit_btn").click()
            errortype = self.driver.find_element_by_class_name("errortype").text
            self.assertEqual(errortype, "请先输入正确的手机验证码!")

            print("%s:PASS" % case_name)
        except AssertionError as e:
            self.browser.get_windows_img("saerch0007-短信验证码")
            raise print(e)


    def test_userReister_search00008(self):
        try:
            cellphone = publicClass.get_number()
            case_name = "当短信验证码错误时"
            self.driver.get("https://pre.laqu.comMon/register/first/valid?memberType=1")
            token = self.driver.find_element_by_id("tonkenNum").get_attribute("value")
            self.driver.find_element_by_class_name("phone_num").send_keys(cellphone)
            self.driver.find_element_by_class_name("imgcodesrc").click()
            self.driver.find_element_by_class_name("imgcodesrc").click()
            pigcode = publicClass.pre_Magpc(token)
            self.driver.find_element_by_id("imgcode").send_keys(pigcode)
            self.driver.find_element_by_class_name("getcode").click()
            code = "123456"
            self.driver.find_element_by_id("message_code").send_keys(code)
            self.driver.find_element_by_class_name("submit_btn").click()
            errortype = self.driver.find_element_by_class_name("error").text
            self.assertEqual(errortype, "短信验证码不正确！")

            print("%s:PASS" % case_name)
        except AssertionError as e:
            self.browser.get_windows_img("saerch0008-短信验证码")
            raise print(e)


    def test_userReister_search00009(self):
        try:
            cellphone = publicClass.get_number()
            case_name = "当协议没有点击时"
            self.driver.get("https://pre.laqu.comMon/register/first/valid?memberType=1")
            token = self.driver.find_element_by_id("tonkenNum").get_attribute("value")
            self.driver.find_element_by_class_name("phone_num").send_keys(cellphone)
            self.driver.find_element_by_class_name("imgcodesrc").click()
            self.driver.find_element_by_class_name("imgcodesrc").click()
            pigcode = publicClass.pre_Magpc(token)
            self.driver.find_element_by_id("imgcode").send_keys(pigcode)
            self.driver.find_element_by_class_name("getcode").click()

            code = publicClass.pre_PcCode(cellphone)
            self.driver.find_element_by_id("message_code").send_keys(code)
            self.driver.find_element_by_xpath('//*[@id="my_from"]/div/div/input').click()
            self.driver.find_element_by_class_name("submit_btn").click()

            errortype = self.driver.find_element_by_class_name("errortype").text
            self.assertEqual(errortype, "请先同意用户协议!")
            print("%s:PASS" % case_name)
        except AssertionError as e:
            self.browser.get_windows_img("saerch0009-协议点击")
            print(e)

    def test_userReister_search00010(self):
        try:
            cellphone = publicClass.get_number()
            case_name = "两次点击协议后"
            self.driver.get("https://pre.laqu.comMon/register/first/valid?memberType=1")
            token = self.driver.find_element_by_id("tonkenNum").get_attribute("value")
            self.driver.find_element_by_class_name("phone_num").send_keys(cellphone)
            self.driver.find_element_by_class_name("imgcodesrc").click()
            self.driver.find_element_by_class_name("imgcodesrc").click()
            pigcode = publicClass.pre_Magpc(token)
            self.driver.find_element_by_id("imgcode").send_keys(pigcode)
            self.driver.find_element_by_class_name("getcode").click()

            code = publicClass.pre_PcCode(cellphone)
            self.driver.find_element_by_id("message_code").send_keys(code)
            self.driver.find_element_by_xpath('//*[@id="my_from"]/div/div/input').click()
            self.driver.find_element_by_class_name("submit_btn").click()
            errortype = self.driver.find_element_by_class_name("errortype").text
            self.assertEqual(errortype, "请先同意用户协议!")
            self.driver.find_element_by_xpath('//*[@id="my_from"]/div/div/input').click()
            style=self.driver.find_element_by_class_name("submit_btn").get_attribute("style")
            self.assertEqual(style, "background: rgb(255, 54, 111);")
            print("%s:PASS" % case_name)
        except AssertionError as e:
            self.browser.get_windows_img("saerch00010-协议点击")
            raise print(e)

    def test_userReister_search00011(self):
        try:

            case_name = "协议链接地址"
            self.driver.get("https://pre.laqu.comMon/register/first/valid?memberType=1")
            href1=self.driver.find_element_by_xpath('//*[@id="my_from"]/div/div/a[1]').get_attribute("href")
            self.assertEqual(href1,self.url+'/html/home/user_protocolB.html')

            href2 = self.driver.find_element_by_xpath('//*[@id="my_from"]/div/div/a[2]').get_attribute("href")
            self.assertEqual(href2, self.url+'/html/home/user_protocolA.html')
            print("%s:PASS" % case_name)
        except AssertionError as e:
            self.browser.get_windows_img("saerch00010-协议地址")
            raise print(e)


    def test_userReister_search000012(self):
        try:
            case_name="手机号正确注册"
            cellphone = publicClass.get_number()
            password = "12345q"
            self.driver.get("https://pre.laqu.comMon/register/first/valid?memberType=1")
            token = self.driver.find_element_by_id("tonkenNum").get_attribute("value")
            self.driver.find_element_by_class_name("phone_num").send_keys(cellphone)
            self.driver.find_element_by_class_name("imgcodesrc").click()
            self.driver.find_element_by_class_name("imgcodesrc").click()
            pigcode = publicClass.pre_Magpc(token)
            self.driver.find_element_by_id("imgcode").send_keys(pigcode)

            self.driver.find_element_by_class_name("getcode").click()
            time.sleep(1)

            self.click_afterSendMsg()  # 发送短信后倒计时验证

            code = publicClass.pre_PcCode(cellphone)

            self.driver.find_element_by_id("message_code").send_keys(code)

            self.driver.find_element_by_class_name("submit_btn").click()

            self.driver.find_element_by_id("passwordset").send_keys(password)

            self.find_defaultPWD()  # 默认密码隐藏不显示状态

            self.click_openEyes()  # 睁眼后密码显示状态

            self.driver.find_element_by_class_name("submit_btn").click()

            self.assertEqual(self.driver.title, "注册成功")
            print("%s:PASS" % case_name)
        except AssertionError as e:
            self.browser.get_windows_img("saerch00010-手机号注册")
            raise print(e)

    def click_afterSendMsg(self):
        """
        发送短信后倒计时验证
        :return:
        """
        try:
            textcode = self.driver.find_element_by_class_name("getcodedelaysand").text
            self.logger.info(textcode)
            self.assertIn("秒后重发", textcode)
        except  AssertionError as e:
            self.logger.error(e)

    def find_defaultPWD(self):
        """
        默认密码隐藏状态
        :return:
        """
        try:

            type = self.driver.find_element_by_id("passwordset").get_attribute("type")

            self.assertEqual(type, "password")

        except AssertionError as e:
            self.browser.get_windows_img("密码闭眼显示异常")
            self.logger.error("密码闭眼显示异常：%s" % e)


    def click_openEyes(self):
        try:
            self.driver.find_element_by_id("passwordeye").click()
            type = self.driver.find_element_by_id("passwordset").get_attribute("type")
            self.assertEqual(type, "text")
        except AssertionError as e:
            self.browser.get_windows_img("密码真眼显示异常")
            self.logger.error("密码真眼显示异常：%s" % e)

            # def test_zogin(self):
            #     self.driver.get("https://pre.laqu.com/go-login")
            #     cellphone="14787946089"
            #     passworld="12345q"
            #     self.driver.find_element_by_id("usertype").click()
            #     self.driver.find_element_by_id("username").send_keys(cellphone)
            #
            #     self.driver.find_element_by_id("password").send_keys(passworld)
            #
            #
            #     self.driver.find_element_by_class_name("submit_btn").click()
            #
            #     self.assertEqual(self.driver.title,"【拉趣网官网】免费试用|试客|打造爆款|安全不降权的免费试用平台 安全爆款就上拉趣网")
            #     time.sleep(10)


if __name__ == '__main__':
    unittest.main()

"""
        quu..__
         $$$b  `---.__
          "$$b        `--.                          ___.---uuudP
           `$$b           `.__.------.__     __.---'      $$$$"              .
             "$b          -'            `-.-'            $$$"              .'|
               ".                                       d$"             _.'  |
                 `.   /                              ..."             .'     |
                   `./                           ..::-'            _.'       |
                    /                         .:::-'            .-'         .'
                   :                          ::''\          _.'            |
                  .' .-.             .-.           `.      .'               |
                  : /'$$|           .@"$\           `.   .'              _.-'
                 .'|$u$$|          |$$,$$|           |  <            _.-'
                 | `:$$:'          :$$$$$:           `.  `.       .-'
                 :                  `"--'             |    `-.     \
                :##.       ==             .###.       `.      `.    `\
                |##:                      :###:        |        >     >
                |#'     `..'`..'          `###'        x:      /     /
                 \                                   xXX|     /    ./
                  \                                xXXX'|    /   ./
                  /`-.                                  `.  /   /
                 :    `-  ...........,                   | /  .'
                 |         ``:::::::'       .            |<    `.
                 |             ```          |           x| \ `.:``.
                 |                         .'    /'   xXX|  `:`M`M':.
                 |    |                    ;    /:' xXXX'|  -'MMMMM:'
                 `.  .'                   :    /:'       |-'MMMM.-'
                  |  |                   .'   /'        .'MMM.-'
                  `'`'                   :  ,'          |MMM<
                    |                     `'            |tbap\
                     \                                  :MM.-'
                      \                 |              .''
                       \.               `.            /
                        /     .:::::::.. :           /
                       |     .:::::::::::`.         /
                       |   .:::------------\       /
                      /   .''               >::'  /
                      `',:                 :    .'
                                           `:.:'


"""
