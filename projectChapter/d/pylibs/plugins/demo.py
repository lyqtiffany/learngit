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

if __name__ == '__main__':
    print(hello.__name__)