from appiumChapter.dchange_boss_pwd import change_pwd,start_app,end_app
from appium import webdriver
from appiumChapter.config import boss_caps

import pytest

def setup():
    start_app(4723,boss_caps)

def test_change_pwd():
    change_pwd("test1234","test12345")

def teardown():
    pass
   # end_app()

if __name__ == '__main__':
    pytest.main(['-s','dtest_change_pwd.py'])