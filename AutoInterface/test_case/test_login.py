#1获取excel数据, body, 请求体，预期结果
#2传入接口代码  #请求体
#3写入测试结果，pass/fail 预期结果与实际结果对比

import pytest
import os
from AutoInterface.lib.apiLib.login import Login
from AutoInterface.tools.ExcelData import get_excel_data


#1获取excel数据, body, 请求体，预期结果
# resList = get_excel_data('1-登录模块','login')
#testData = {'username':'20154084', 'password':'123456'}
#2传入接口代码  #请求体

#1登录的测试类
#从excel获取请求头、响应的预期结果



class TestLogin:
    #get_excel_data('1-登录模块','login')返回[(),()]列表套元组格式
    @pytest.mark.parametrize('inBody,expData',get_excel_data('1-登录模块','login')) #[(1,2),(3,4)]数据驱动，如果自己开发，写个for循环
    def test_login(self, inBody, expData):
        #调用登陆的接口代码
        res = Login().login(inBody, getToken=False)
        #预期结果和实际结果对比
        assert res['message'] == expData['message']

if __name__ == '__main__':
    #1-框架执行后的结果数据， --alluredir
    #2 使用allure打开结果数据
    #3浏览器查看报告
    pytest.main(['test_login.py', '-s', '--alluredir', '../report/tmp']) #-s是输出打印信息
    #2 使用allure打开结果数据  #3浏览器查看报告,设置谷歌为默认浏览器
    os.system('allure serve ../report/tmp')


#项目执行都通过了，但是allure的结果没有生成，report里面还是空的，要怎么解决呢
#改一下setting-tools-python integrated tools里面的Testing，换成unittests


'''
swwager
项目业务-》接口文档-》接口用例-python脚本-python框架
-调试&执行

业务层,-登陆模块。留言模块
用例层
数据层
配置层
日志层
报告层
执行层

'''

'''
pytest执行测试需要遵循的规则
py测试文件需要以test_开头，或者_test结尾
测试类必须用test开头，并且不能有Init方法
测试方法需要用test_开头
断言必须使用assert
'''

'''
pytest结合allure执行测试
'''

#pytest+allure-->Gitlab-->jenkens-->邮件，日志,报告

# 仓库GitLab, GitHub, Gitee
'''
docker实现GitLab与Jenkins自动化流程
镜像
  静态的模板Images
容器
  镜像创建的实例
仓库
   存储镜像的地方

'''
#pycharm,Git都安装好，改动了代码之后，点击项目，右键-->Git-->Commit Directory-->提交到本地仓库
#commit + comment提交->master->找到分支，推送到远程仓库

#用webhook 触发jenkins构建执行项目


