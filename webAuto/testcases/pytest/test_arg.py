'''
pytest参数化处理，比如登陆页面的用户名密码，就有4种组合，适合一条用例，执行几种不同的数据
在pytest中，也可以使用参数化测试，即每组参数都独立执行一次测试
使用的工具就是pytest.mark.parametrize(argnames, argvalues).
'''

'''  test login scenario
username ,password
1, admin xxx
2, xxx 123
3, admin 123
4, xxx xxx

实例
'''

import pytest
# 列表
data = ['123', '456']

@pytest.mark.parametrize('pwd', data) #只有一个参数，跟方法里面的名称要对应
def test1(pwd): #跟方法里面的名称要对应
    print(pwd)
# test_arg.py::test1[123] PASSED                                           [ 50%]123
# test_arg.py::test1[456] PASSED                                           [100%]456

#元组
data2 = [
    (1, 2, 3),
    (4, 5, 6)
]
@pytest.mark.parametrize('a, b, c', data2)
def test2(a, b, c):
    print(a, b, c)
# test_arg.py::test2[1-2-3] PASSED                                         [ 75%]1 2 3
# test_arg.py::test2[4-5-6] PASSED                                         [100%]4 5 6

#字典
data3 = (
    {
        'user': 1,
        'pwd': 2
    },
    {
        'age': 3,
        'email': 'tom@qq.com'
    }
)

@pytest.mark.parametrize('dic', data3)
def test3(dic): #通过字典的key获得value
    print(dic)

#通过pytest.param定义参数
data_1 = [
    pytest.param(1, 2, 3, id="(a+b): pass"), #id的值可以自定义，只要方便理解每个用例是干什么的即可
    pytest.param(4, 5, 10, id="(a+b): fail")
]

def add(a, b):
    return a + b

class TestParametrize(object): #可以单独运行这个class

    @pytest.mark.parametrize('a, b, expected', data_1) #从data_1取参数
    def test_parametrize_1(self, a, b, expected):
        assert add(a, b) == expected

'''
pytest fixture
定义fixyure跟定义普通函数差不多，唯一区别就是在函数上加个装饰器@pytest.fixture()
fixture命名不要以test开头，跟用例区分开。
fixture是有返回值的，没有返回值默认为none
用例调用fixture的返回值，直接就是把fixture的函数名称当做变量名称

'''


