# coding=utf-8
import sys
import os
curPath = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(curPath)
import unittest


from comMon.Log import MyLog

import HTMLTestRunner




class userRegister(unittest.TestCase):

    def test001(self):
        print("001")
        pass

    def test002(self):
        print("002")
        pass


if __name__ == '__main__':
    log = MyLog.get_log()
    resultPath = log.get_Onereport_path()
    test_suite = unittest.TestSuite()  # 创建一个测试集合
    test_suite.addTest(userRegister("test001"))  # 测试套件中添加测试用例
    # test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
    fp = open(resultPath, 'wb')  # 打开一个保存结果的html文件
    print(resultPath)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp)
    # 生成执行用例的对象
    runner.run(test_suite)
    fp.close()
