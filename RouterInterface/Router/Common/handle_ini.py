#! -*-conding:utf-8 -*-
#@Time: 2020/6/6 0006 16:45
#@swzhou
'''
功能说明
'''


import configparser
import os
import sys
base_path = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(base_path)
from pathlib import Path


class HandleIni:
    def load_ini(self,file = None):
        if file == None:
            file = '/Config/config.ini'
        file_path = base_path + file
        # print(file_path)
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8-sig')
        return cf

    def get_value(self,key,section = None):
        if section == None:
            section = 'Router'
        cf = self.load_ini()
        try:
            data = cf.get(section,key)
        except Exception:
            print(Path(__file__).name,"没有获取到数据")
            data =None
        return data

handleIni = HandleIni()

if __name__ == '__main__':
    print(handleIni.get_value('host'))