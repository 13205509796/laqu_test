# 浏览器引擎类
from selenium import webdriver

import readConfig as readConfig
from comMon.Log import MyLog as Log

log = Log.get_log()
logger = log.get_logger()
localReadConfig = readConfig.ReadConfig()



class BrowserEngine(object):

    def pc_open_browser(self):

        dir = readConfig.proDir
        self.chrome_driver_path = dir + '/tool/chromedriver.exe'
        browser = localReadConfig.get_bromser("browserName")

        logger.info('you had select %s' % browser)
        url = localReadConfig.get_defaultUrl("URL")

        logger.info('you want to visit %s' % url)
        if browser == 'Firefox':
            self.driver = webdriver.Firefox(executable_padth=self.firefox_driver_path)
            logger.info('Starting firefox browser')
        elif browser == 'Chrome':
            option = webdriver.ChromeOptions()
            option.add_argument("headless")
            self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path ,chrome_options=option)
            logger.info('Starting chrome browser')


        # URL请求
        self.driver.get(url)
        logger.info('Open url: %s' % url)
        # 窗口全屏幕
        self.driver.maximize_window()
        logger.info('Maximize the current window')
        # 加载等待时间
        self.driver.implicitly_wait(1)
        logger.info('Set implicitly wait 5 seconds')

        return self.driver
    # def h5_open_browser(self):
    #
    #     # 读取配置文件
    #     config = configparser.ConfigParser()
    #     file_path = self.dir + '/conFig/config.ini'
    #     print('H5配置问件路径===========', file_path)
    #     config.read(file_path)
    #     # 从配置 文件 中获取浏览器名称并打印日志
    #     browser = config.get('browserType', 'browserName')
    #     print('H5所使用浏览器=========', browser)
    #     mylogger.info('you had H5 select %s' % browser)
    #     # 从配置文件 中获取要访问的URL并打印日志
    #     url = config.get('H5testServer', 'URL')
    #     print('H5测试项目开始地址=============', url)
    #     mylogger.info('you want to visit %s' % url)
    #
    #     h5deviceName=config.get('H5deviceName', 'Name')
    #     print('H5测试测试模拟器=============', h5deviceName)
    #     mobileEmulation = {'deviceName': 'iPhone X'}
    #     options = webdriver.ChromeOptions()
    #     options.add_experimental_option('mobileEmulation', mobileEmulation)
    #     self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path, chrome_options=options)
    #     self.driver.get(url)
    #     mylogger.info('Open url: %s' % url)
    #     return self.driver

