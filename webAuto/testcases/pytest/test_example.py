# pip intsall pytest 安装pytest
# https://docs.pytest.org/en/stable/ 官网
'''
编写规则，
测试文件用test开头(use test结尾也可以)，
测试类用Test开头，并且不能带有init方法
测试函数以test开头
断言使用基本的assect即可
'''

import pytest

class TestLoginCase(object): #测试类用test开头，并且不能带有init方法
    # def __init__(self): 不能定义Init方法

    def test01(self): #测试函数以test开头
        print('test01hhh')
        assert 1 == 1


    @pytest.mark.undo
    def test02(self): #测试函数以test开头
        print('test02d')
        assert 1 == 1  #asert 1 = 2

    def add(self): #不需要执行的用例，直接不用test开头或者结尾命名
        print('3add')

    @pytest.mark.do
    def test03(self): #测试函数以test开头
        print('test03 result')
        #asert 1 = 2

if __name__ == '__main__':
    pytest.main(['-vs', 'test_example.py']) #模块名称 pytest.main(['-v', '-s', 'test_example.py']) #模块名称

'''
控制台console参数介绍， 
-v 用于显示每个函数的执行结果
-q 只显示整体测试结果
-s 用于显示测试函数中print()函数输出   main加上'-s' 参数才可以控制台输出
-x --exitfirst,在第一个错误或者测试失败时，立即退出
-h 帮助

'''

'''
执行pytest测试，
配置pycharm执行：settings->tools->python integrated tools -> default test runner
main方法执行: pytest.main(['-vs', 'test_example.py'])
命令行执行，进入到项目所在目录: pytest -s -v test.py #cd 到webAuto/testcases/pytest
'''


'''
pytest里面的标记，标记某些用例可以执行或者不执行
pytest查找测试策略：默认会递归查找当前目录下所有用test开始或者结尾的python脚本，执行文件内(包括子文件)所有用test开始或者结束的函数或者方法
标记测试函数：
由于某种原因，比如test_func2的功能尚未完成，我们只想执行指定的测试函数。pytest中有几种方式可以解决
第一种： 显示指定函数名，通过::标记
test_no_mark.py::test_func1  #在test_no_mark.py文件里面只执行test_func1 (命令行执行)
第二种，使用模糊匹配，使用 -k 选项标识
pytest -k func1 test_no_mark.py  #在test_no_mark.py文件里面只执行func1(模糊匹配可以找到test_func1)  (命令行执行)
第三种，使用配置文件，pytest.mark在函数是进行标记
需要创建pytest.ini文件
格式
[pytest]
markers = 
    do:do
    undo:undo
在用例上打标记， pytest -m do test_example.py 在命令行执行，这样只运行标记为do的文件
'''

'''
pytest参数化处理
在pytest中，也可以使用参数化测试，即每组参数都独立执行一次测试
使用的工具就是pytest.mark.parametrize(argnames, argvalues).

'''


