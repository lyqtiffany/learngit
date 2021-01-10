#pytest并行插件
#提前装好pytest-xdist插件 pip install pytest-xdist,

from appiumChapter.dchange_boss_pwd import change_pwd,start_app,end_app,get_login_text,login, load_yml, dump_yml,after_change
from appium import webdriver
from appiumChapter.config import boss_caps,xiaomi_caps,meizu_caps

import pytest

#初始化，启动被测app,创建session
@pytest.fixture(params=[('4723',xiaomi_caps),('4725',meizu_caps)])
def before_change_pwd(request):
    port = request.param[0]
    caps = request.param[1] #取元组里面的第2个元素，配置项

    start_app(port, caps)
    yield #这个关键字相当于代码执行过程中的断点，它执行后面的清除动作

    after_change_pwd() #清除动作

def test_change_pwd(before_change_pwd):
    psw = load_yml()
    new_pwd = psw['new']
    old_pwd = psw['old']
    change_pwd(old_pwd, new_pwd)

    text = get_login_text()
    assert text == "微信登录"

    #交换密码
    after_change(old_pwd, new_pwd)

    login(new_pwd)

#清除，终止
def after_change_pwd():
    pass
   # end_app()




if __name__ == '__main__':
    #'-n 2 是pytest-xdist的并行参数，表示同时跑两个进程来启动测试脚本，因为有两组参数'
    pytest.main(['-s','eboss_TwoDevice_test.py', '-n 2'])