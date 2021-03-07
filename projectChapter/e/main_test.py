'''
@author: haiwen
@date: 2021/2/26
@file: main_test.py.py
'''
import os

import pytest
from pylibs.webui.bussiness import LoginPage,HomePage

if __name__ == '__main__':
    #pytest.main(['-s','testcase/webapi','--alluredir=tmp/report','--clean-alluredir'])
    #os.system('allure serve tmp/report')  用jenkins执行的时候不要有这行代码，

    LoginPage().login('xx','xxxx').to_schedule_page().new_schedule('发布会','小明')