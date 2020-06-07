#! -*-conding:utf-8 -*-
#@Time: 2020/6/6 0006 16:38
#@swzhou
'''
封装request请求
'''

import json
import requests

from Router.Common.handle_ini import handleIni
from Router.Common.handle_cookie import handleCookie


class BaseRequest():

    def send_get(self,url,data,cookie = None,get_cookie= None,header=None):

        response = requests.get(url=url, params=data, cookies=cookie,headers=header)

        if get_cookie: #判断并写入cookie ，get_cookie传入格式 {'is_cookie':'web'}
            cookie_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_jar)
            handleCookie.write_cookie_value(cookie_value,get_cookie['is_cookie'])

        res = response.content.decode('utf-8')

        return res

    def send_post(self,url,data,cookie = None,get_cookie= None,header=None):

        response = requests.post(url=url, data=data,cookies=cookie,headers=header)

        if get_cookie:
            cookie_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_jar)
            handleCookie.write_cookie_value(cookie_value,get_cookie['is_cookie'])

        res = response.content.decode('utf-8')

        return res

    def run_main(self,method,url,data,cookie = None,get_cookie= None,header=None):

        host = handleIni.get_value('host')
        if 'http:' not in url:
            url = host + url
        # print(url)
        if method == 'get':
            res = self.send_get(url,data,cookie,get_cookie,header)
        elif method == 'post':
            res = self.send_post(url,data,cookie,get_cookie,header)
        else:
            print('暂不支持该请求方式')
            res = None

        try: #尝试使用json解析
            res = json.loads(res)
        except Exception:
            # print('res结果 不是一个标准的json')
            pass
        return res

baseRequest = BaseRequest()

if __name__ == '__main__':
    print(baseRequest.run_main('post','action/login',{"username":"admin","password":"admin"}))
