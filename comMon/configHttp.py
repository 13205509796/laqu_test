import requests
import urllib3

import readConfig as readConfig
from comMon.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()


class ConfigHttp:
    urllib3.disable_warnings()

    def __init__(self):
        global scheme, host, port, timeout  # 定义全局变量
        scheme = localReadConfig.get_http("scheme")  # https or http
        host = localReadConfig.get_http("baseurl")  # 域名
        port = localReadConfig.get_http("port")  # 端口号
        timeout = localReadConfig.get_http("timeout")  # 超时时间
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0
        self.cookies = 0

    def set_cookies(self, cookies):
        """
        set cookies
        :param cookies:
        :return:
        """
        self.cookies = cookies

    def set_url(self, url):
        """
        set url
        :param: interface url
        :return:
        """
        self.url = scheme + '://' + host + url

    def set_headers(self, header):
        """
        set headers
        :param header:
        :return:
        """
        self.headers = header

    def set_params(self, param):
        """
        set params
        :param param:
        :return:
        """
        self.params = param

    def set_data(self, data):
        """
        set data
        :param data:
        :return:
        """
        self.data = data
        print("请求接口：", self.data)

    def set_files(self, filename):
        """
        set upload files
        :param filename:
        :return:
        """
        if filename != '':
            file_path = 'testFile/img/' + filename
            self.files = {'file': open(file_path, 'rb')}

        if filename == '' or filename is None:
            self.state = 1

    # defined http get method
    def get(self):
        """
        defined get method
        :return:
        """
        urllib3.disable_warnings()
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(timeout),\
                                    verify=False, cookies=self.cookies)
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    # include get params and post data
    # uninclude upload file
    def post(self):
        """
        defined post method
        :return:
        """
        urllib3.disable_warnings()
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, timeout=float(timeout),\
                                     verify=False, cookies=self.cookies)
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    # include upload file
    # def postWithFile(self):
    #     """
    #     defined post method
    #     :return:
    #     """
    #     try:
    #         response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
    #                                  timeout=float(timeout))
    #         return response
    #     except TimeoutError:
    #         self.logger.error("Time out!")
    #         return None

    # defined http post method
    # for json
    # def postWithJson(self):
    #     """
    #     defined post method
    #     :return:
    #     """
    #     try:
    #         response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout))
    #         return response
    #     except TimeoutError:
    #         self.logger.error("Time out!")
    #         return None


if __name__ == "__main__":
    print("ConfigHTTP")
