'''
@author: haiwen
@date: 2021/3/3
@file: demo.py
'''
import functools


def decorate(name):
    def outter(fun):
        @functools.wraps(fun)
        def inner(*args,**kwargs):
            print('自定义标题' +name)
            res = fun(*args,**kwargs)
            return res
        return inner
    return outter

@decorate('用例标题')
def hello(arg):
    print(arg)





class Single(object):  #所有python对象默认继承object
    #python生成对象的方法new
    def __new__(cls, *args, **kwargs):
        # 如果当前class有对象，就返回该对象，如果没有创建一个再返回
        # python的反射 hasattr(对象，属性名)--判断当前对象是否有xxxx属性
        if hasattr(cls,'_instance'):
            return cls._instance
        # object适用new方法创建对象
        cls._instance = object.__new__(cls)
        return cls._instance

    # init 方法是否生成对象？？？  否 不生成对象
    def __init__(self):
        #作为初始化
        pass

#单例模式是可以继承的
class ABC(Single):
    pass

if __name__ == '__main__':
    #print(hello.__name__)
    s1=ABC()
    s2=ABC()
    s1.driver='123'
    s2.driver ='234'
    print(s1.driver)
    print(s2.driver)
    assert s1.driver==s2.driver  # 如果是单例模式，两者就相等