#! -*-conding:utf-8 -*-
#@Time: 2020/6/7 0007 16:41
#@swzhou
'''
读取、写入 json
'''

import os
import json

from Router.Common.handle_ini import handleIni

base_path = os.path.dirname(os.path.dirname(__file__))

class HandleJson():

    def read_file(self,file_name = None):
        if file_name == None:
            file_name = handleIni.get_value('file_cookie.json','Config_file')
        file_path = base_path + file_name
        with open(file_path,encoding='utf-8') as f:
            data = json.load(f)
        return data

    def get_value(self,key,file_name = None):
        data = self.read_file(file_name)
        return data.get(key)

    def write_value(self,data,file_name = None):
        data_value = json.dumps(data)
        if file_name == None:
            file_name = handleIni.get_value('file_cookie.json', 'Config_file')
        file_path = base_path + file_name
        with open(file_path,'w') as f:
            f.write(data_value)

handleJson = HandleJson()

if __name__ == '__main__':
    print(handleJson.get_value('web'))
    data = {'111': '222'}
    handleJson.write_value(data)