'''
Created on 2018年1月13日

@author: Administrator
'''
import json
import requests
#      这个类其实是没有任何乱用的，只不过我这个demo 接口需要这这一步进行加密而已~~


def publicsign(wuxisign,urlhander) :
    urlcount = "/generate/post/url"
    url = urlhander + urlcount 
    headers = {}
    hr = requests.post(url,data=wuxisign, headers=headers,verify=False)
    hjson = json.loads(hr.text)   
    return hjson
#     pwdEncrypt = hjson["pwdEncrypt"]
#     print(pwdEncrypt)
#     
#     sign =hjson["sign"]
#     
#     print(sign)
    
