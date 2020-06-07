#! -*-conding:utf-8 -*-
#@Time: 2020/6/7 0007 17:26
#@swzhou
'''
读取headers
'''

from Router.Common.handle_json import handleJson
from Router.Common.handle_ini import handleIni

import os
base_path = os.path.dirname(os.path.dirname(__file__))

class HandleHeader():

    def get_headers(self):
        file_name = handleIni.get_value('file_headers.json','Config_file')
        data = handleJson.read_file(file_name)
        return data

handleHeader = HandleHeader()

if __name__ == '__main__':
    print(handleHeader.get_headers())