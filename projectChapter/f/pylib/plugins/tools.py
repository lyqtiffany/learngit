'''
@author: haiwen
@date: 2021/1/18
@file: tools.py
'''
import allure
import functools
#装饰器
def decorate(fun):
    @functools.wraps(fun)  #保留被装饰函数的信息
    def inner(*args,**kwargs):
        print('执行附加指令')
        res = fun(*args,**kwargs)
        print('函数执行后')
        return res
    return inner

@decorate
def hello():
    print('hello')

# hello=decorate(hello)  被装饰函数的实际结果

#增强版allure装饰器
def dynamic_report(target):
    def decorate(fun):
        @functools.wraps(fun)
        def inner(*args,**kwargs):
            #执行测试方法
            res = fun(*args,**kwargs)
            #增加自定义测试用例标题
            print('增加自定义测试用例标题')
            # target指定使用什么参数来定义用例标题
            title =  kwargs.get(target,'未定义标题')
            allure.dynamic.title(title)
        return inner
    return decorate

#单例模式
class Single(object):
    #init方法是否产生对象？不产生对象,没有返回值
    def __init__(self):
        pass
    #产生对象的是？ 产生对象
    def __new__(cls, *args, **kwargs):
        #单例模式--判断当前类如果有实例---就直接返回，否则创建一个再返回
        if hasattr(cls,'_instance'):
            return cls._instance
        #否则创建一个再返回
        cls._instance = object.__new__(cls) # 产生实例
        return cls._instance

#单例模式可以继承
class Demo(Single):
    pass

if __name__ == '__main__':
    s1=Demo()
    s2=Demo()
    s1.driver='初始化浏览器'

    print(s2.driver)