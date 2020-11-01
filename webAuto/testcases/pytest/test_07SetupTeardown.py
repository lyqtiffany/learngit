'''
学过unittest的都知道里面用前置和后置steup和teardown非常好用，
在每次用例开始前和结束后都去执行一次
当然，还有更高级一点的steupClass和teardownClass, 需要配合@classmethon装饰器一起使用
在做selenium自动化的时候，它的效率尤为突出，可以只启动一次浏览器执行多个用例

pytest setup和teardown简介
模块级（setup_module/teardown_module），开始与模块始末，全局的
函数级（setup_function/teardown_function），只对函数用例生效（不在类中）
类级(setup_class/teardown_class)只在类中前后运行一次（在类中）
方法级（setup_method/teardown_method）开始于方法始末（在类中）
类里面的（setup/teardown）运行在调用方法的前后
'''


import pytest

class TestCase01(object):
    @classmethod  #在类里面只执行一次
    def setup_class(cls): #cls的名称无所谓？ #初始化driver
        print('setup_class')

    @classmethod
    def teardown_class(cls): #cls的名称无所谓？
        print('teardown_class')

    def test01(self):
        print('test01 in class')

    def test02(self):
        print('test02 in class')



def setup_function(): #此时所谓的函数不是在类里面
    print('setup_function')

def teardown_function():
    print('teardown_function')

def setup_module():  #不能只有Module，需要有测试用例才能执行
    print('setup_module')

def teardown_module(): #名字必须写对，否则不会生效
    print('teardown_module')

def test1(): #test_07SetupTeardown.py::test1 setup_module  PASSED    [100%]test1 teardown_module
    print('test1')

def test2(): #run test1 and test2的时候，module级别的只执行一次，function级别的每次都执行
    print('test2...')

if __name__ == '__main__':
    pytest.main(['test_07SetupTeardown.py', '-sv'])




