'''
函数可以作为对象来传递

闭包
在一个内部函数里面，对在外部作用域（但不是全局作用域）
的变量进行银行，那么这个内部函数就是闭包
def outer():
    x =10
    def inner():
        print(x)
        return inner
    return outer
outer()()

装饰器
不修改代码的前提下，增加额外的功能

闭包：外函数里面定义一个内部函数，外函数有一个临时变量被内函数调用，外函数的返回值是内函数的引用
'''


import time

def foo():
    print("execute test case")
    time.sleep(1)

# 需求1 ，统计foo()函数的运行时间
def time_count(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print("time run", end_time -  start_time)
    return inner

# foo = time_count(foo) #返回值inner,语法糖
# foo() # 相当于inner(). 也就是调用inner里面的统计时间

@time_count  #foo=time_count(foo)
def foo():
    print("execute test case")
    time.sleep(1)

foo()