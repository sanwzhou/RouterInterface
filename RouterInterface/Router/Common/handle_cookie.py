#! -*-conding:utf-8 -*-
#@Time: 2020/6/7 0007 17:12
#@swzhou
'''
操作cookie
'''

from Router.Common.handle_json import handleJson
from Router.Common.handle_ini import handleIni


class Handle_cookie():

    def get_cookie_value(self,key):
        file_name = handleIni.get_value('file_cookie.json', 'Config_file')
        data = handleJson.read_file(file_name)
        return data.get(key)

    def write_cookie_value(self,data,key):
        file_name = handleIni.get_value('file_cookie.json', 'Config_file')
        data1 = handleJson.read_file(file_name)
        data1[key] = data
        handleJson.write_value(data1)


handleCookie = Handle_cookie()

if __name__ == '__main__':
    print(handleCookie.get_cookie_value('web'))
    data1 = {'111':'222'}
    handleCookie.write_cookie_value(data1,'web')