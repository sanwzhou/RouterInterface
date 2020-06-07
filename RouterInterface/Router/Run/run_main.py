#! -*-conding:utf-8 -*-
#@Time: 2020/6/7 0007 14:58
#@swzhou
'''
功能说明
'''

import os
import ddt
import json
import unittest
import HTMLTestRunner

from Router.Common.handle_excel import handleExcel
from Router.Common.handle_ini import handleIni
from Router.Common.handle_json import handleJson
from Router.Common.handle_header import handleHeader
from Router.Base.baseRequest import baseRequest

data = handleExcel.get_excel_data()


@ddt.ddt
class RunMain(unittest.TestCase):

    @ddt.data(*data)
    def test_run_Main(self,data):
        get_cookie = None
        cookie = None
        header = None

        is_run = data[int(handleIni.get_value('is_run','Excel_column'))]
        if is_run == 'yes':
            case_id = data[int(handleIni.get_value('case_id', 'Excel_column'))]

            is_condition =  data[int(handleIni.get_value('is_condition', 'Excel_column'))]
            if is_condition != None:
                depend_key =  data[int(handleIni.get_value('depend_key', 'Excel_column'))]

            is_cookie =  data[int(handleIni.get_value('is_cookie', 'Excel_column'))]
            if is_cookie == 'write':
                get_cookie = {"is_cookie":"web"}
            elif is_cookie == 'yes':
                cookie = handleJson.get_value('web')

            is_header =  data[int(handleIni.get_value('is_header', 'Excel_column'))]
            if is_header == 'yes':
                header = handleHeader.get_headers()

            url = data[int(handleIni.get_value('url', 'Excel_column'))]
            method = data[int(handleIni.get_value('method', 'Excel_column'))]

            request_data = data[int(handleIni.get_value('request_data', 'Excel_column'))]
            if request_data:#发送参数为空
                request_data = json.loads(data[int(handleIni.get_value('request_data', 'Excel_column'))])

            res = baseRequest.run_main(method,url,request_data,cookie,get_cookie,header)
            # print(res)

            expect_method =  data[int(handleIni.get_value('expect_method', 'Excel_column'))]
            expect_result =  data[int(handleIni.get_value('expect_result', 'Excel_column'))]

            execute_result =  int(handleIni.get_value('execute_result', 'Excel_column'))
            result_data =  int(handleIni.get_value('result_data', 'Excel_column'))
            row = handleExcel.get_rows_number(case_id)

            if expect_method == 'text':

                try:
                    self.assertIn(expect_result,res)
                    # print('case验证通过')
                    handleExcel.write_data(row, execute_result + 1, '通过')
                    handleExcel.write_data(row, result_data + 1, res)
                except Exception as e:
                    # print('case验证失败')
                    handleExcel.write_data(row, execute_result + 1, '失败')
                    handleExcel.write_data(row, result_data + 1, res)
                    raise e



if __name__ == '__main__':
    # unittest.main()
    import time
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    base_path = os.path.dirname(os.path.dirname(__file__))
    case_path = base_path + '/Run/'
    report_file = base_path + '/Report/report_' + now + '.html'
    print(report_file)
    dicover = unittest.defaultTestLoader.discover(case_path,pattern="run_main.py")
    with open(report_file,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='RouterInterface',description=u'用例执行情况：')
        runner.run(dicover)
    f.close()

