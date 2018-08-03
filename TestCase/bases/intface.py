import unittest

from comMon.Log import MyLog

import readConfig as readConfig
from comMon.basePage import BasePage

localReadConfig = readConfig.ReadConfig()

class intFaceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BasePage()
        cls.driver = cls.browser.pc_open_browser()
        cls.log = MyLog.get_log()
        cls.logger = cls.log.get_logger()
        cls.url = localReadConfig.get_defaultUrl("URL")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("-------------用例执行结束-------------")
"""
                              _ooOoo_
                             o8888888o
                             88" . "88
                             (| -_- |)
                             O\  =  /O
                          ____/`---'\____
                        .'  \\|     |//  `.
                       /  \\|||  :  |||//  \
                      /  _||||| -:- |||||-  \
                      |   | \\\  -  /// |   |
                      | \_|  ''\---/''  |   |
                      \  .-\__  `-`  ___/-. /
                    ___`. .'  /--.--\  `. . __
                 ."" '<  `.___\_<|>_/___.'  >'"".
                | | :  `- \`.;`\ _ /`;.`/ - ` : | |
                \  \ `-.   \_ __\ /__ _/   .-` /  /
           ======`-.____`-.___\_____/___.-`____.-'======
                              `=---='
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                      佛祖保佑        Case稳过                
"""