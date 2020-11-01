#pip install allure-pytest
#下载解压，配置到环境变量 https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/
#!!!还没有下载完成

import allure
import pytest

@pytest.fixture(scope="session")
def login():
    print('用例先登录')

@allure.step("步骤1：点xxx")
def step_1():
    print("111")

@allure.step("步骤2：点xxx")
def step_2():
    print("222")

@allure.feature("编辑页面")
class TestEditPage():
    ''' 编辑页面 '''
    @allure.story("这是一个xx的用例")
    def test_1(self, login):
        '''用例描述： 先登录，再去执行xxx'''
        step_1()
        step_2()
        print("xxx")

    @allure.story("打开a页面")
    def test_2(self, login):
        '''用例描述： 先登录，再去执行yyy'''
        print("yyy")

if __name__ == '__main__':
    #注意生成测试报告，必须在命令行执行
    #terminal 进入到python项目级别
    #pytest --alluredir ./report test_allure.py
    #allure serve ./reports 启动allure查看报告,执行

    #目录\pythonLearnFrist\webAuto>pytest --alluredir ./reports testcases/pytest/test_allure.py

    pytest.main(['--alluredir','./reports', 'test_allure.py'])
    pytest.main(['--alluredir', './reports', 'test_allure.py'])

'''
pytest
继承unittest.TestCase修改继承为object
unittest setup方法修改为pytest setup
unittest的断言修改成Pytest的断言
使用pytest依赖插件, 用pytest解决用例之间的依赖关系
pip install pytest-dependency
'''
