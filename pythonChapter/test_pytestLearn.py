#pytest 是一种自动化测试框架，是unittest的升级版
#pytest是第三方库，需要安装后使用

# py测试文件必须test_开头，或者_test结尾
# 类必须Test开头,且类当中不能有__init__方法
# 方法或者函数必须用test_开头
# 断言必须使用assert

# assert 1 == 2 #判断等式的左边与右边是否相等
# assert 3 > 2 #判断语句是否为真
# assert 10 in [10, 20] #判断某个值是否属于某个对象
# assert not True #判断某个值是否不为真
# assert 1!= 2 #判断某个值是否不等于另一个值

#pytest中有4种setup和teardown
# 1.setup_module 和teardown_module 在整个测试用例所在的文件中所有的方法运行前和运行后执行，只会执行一次
# 2.setup_class 和teardown_class 则在整个文件中的一个class中所有用例的前后执行
# 3.setup_method 和teardown_method 每个方法
# 4.setup_method 和teardown_function 每个函数（不在类里面的就是函数）




import os
import allure
import pytest #加载pytest模块
# class Test1:
#     # def setup_method(self): #1
#     #     print('这是一个setup method')
#
#     def setup_class(self):#1
#         print('class setup 开始')
#
#     def test_01(self): #2
#         print('开始执行01')
#         assert 1 == 2
#
#     def test_02(self): #3
#         print('开始执行02')
#         assert 2 == 2
#
#     def teardown_class(self):#4
#         print('teardown结束')

    # def teardown_method(self): #4
    #     print('这是一个teardown method')
#setup_method, teardown_method 顺序124,134
#setup_class. teardown_class 顺序1234

#分层级
@allure.feature('层级1') #分层的1级标签
class Test2:
    @allure.story('层级2') ##分层的2级标签
    @allure.title('层级3') ##分层的3级标签

    # @pytest.mark.parametrize('x, y', ([3, 3], [9, 10])) #一个值进行比较就是元组，多个就是元组里面装列表
    # @pytest.mark.parametrize('x, y', [[3, 6], [9, 10]]) #两层列表嵌套也可以
    # @pytest.mark.parametrize('x, y', [[3, 6]]) #单组参数
    # @pytest.mark.parametrize('x, y', ([3, 6],)) #单组参数
    def test_09(self):
        assert 1 == 1





if __name__ == '__main__':
    pytest.main(['test_pytestLearn.py', '-s', '--alluredir', '../report'])
    os.system('allure generate ../report -o ../report/report --clean')
    os.system('allure server ../report')


    # pytest.main(['--alluredir', '../reportA', 'test_pytestLearn.py'])
    #cmd 执行 pytest --alluredir ../reportA test_pytestLearn.py
    #allure serve ../reportA 启动allure查看报告,执行

# pytest.main(['test_pytestLearn.py']) #如果要执行文件里面的print语句，需要加-s的参数
# ./ 当前目录下
# ../当前目录的上一层目录下
#基本命令结构：allure generate 测试数据位置  -o 报告生成位置

#思考题，写一个函数，可以计算某数的阶乘，最好不用循环语句


















