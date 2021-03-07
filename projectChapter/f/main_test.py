'''
@author: haiwen
@date: 2021/1/13
@file: main_test.py
'''
import os

import pytest

if __name__ == '__main__':
    pytest.main(['tc', '-s','--alluredir=tmp/report','--clean-alluredir'])
    #Jenkins执行的时候不需要此行代码
    #os.system('allure serve tmp/report')