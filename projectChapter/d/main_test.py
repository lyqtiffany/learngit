'''
@author: haiwen
@date: 2021/2/26
@file: main_test.py.py
'''
import os

import pytest

if __name__ == '__main__':
    pytest.main(['-s','testcase/webapi','--alluredir=tmp/report','--clean-alluredir','-k test_tc003001'])
    #os.system('allure serve tmp/report')  用jenkins执行的时候不要有这行代码，