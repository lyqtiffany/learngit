from appiumChapter.dchange_boss_pwd import change_pwd,start_app,end_app,get_login_text,login, load_yml, dump_yml,after_change
from appium import webdriver
from appiumChapter.config import boss_caps

import pytest

def setup():
    start_app(4723,boss_caps)

def test_change_pwd():
    psw = load_yml()
    new_pwd = psw['new']
    old_pwd = psw['old']
    change_pwd(old_pwd, new_pwd)

    text = get_login_text()
    assert text == "微信登录"

    #交换密码
    after_change(old_pwd, new_pwd)

    login(new_pwd)

def teardown():
    pass
   # end_app()




if __name__ == '__main__':
    pytest.main(['-s','dtest_change_pwd.py'])