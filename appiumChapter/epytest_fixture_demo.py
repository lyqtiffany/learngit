'''
@author: haiwen
@date: 2020/9/18
@file: pytest_fixtrue_demo.py
'''

#演示pytest参数化
import pytest

#以模块为作用域
# def setup_module():
#     print('启动被测app')
#     print(f'连接appium服务 {port}')

#以模块为作用域
# def teardown_module():
#     print('关闭被测app')
#     print(f'断开appium服务 {port}')


#重新定义初始化清除函数
@pytest.fixture(scope='module',params=[(4723,'xiaomi'),(4727,'meizu')])#作用域默认是Test
def before_test_module(request):
    port=request.param[0] #取元组的第一个元素作为参数
    device=request.param[1]
    print(f'在{device}启动被测app')
    print(f'连接appium服务{port}')
    yield #后面写清除动作
    print('关闭被测app')
    print(f'断开appium服务')

#清除函数
def after_test_module():
    print('关闭被测app')
    print(f'断开appium服务')


#测试用例的参数化
@pytest.mark.usefixtures('before_test_module')#使用某个初始化函数
@pytest.mark.parametrize('psw',['123','456'])
def test_app(psw):
    print('测试boss app')
    print(f'登录测试账号{psw}')




if __name__ == '__main__':
    pytest.main(['pytest_fixtrue_demo.py','-s'])