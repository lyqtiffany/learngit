# Python的装饰器本质上是一个嵌套函数，它接受被装饰的函数(func)作为参数，并返回一个包装过的函数。
# 这样我们可以在不改变被装饰函数的代码的情况下给被装饰函数或程序添加新的功能。
# Python的装饰器广泛应用于缓存、权限校验、性能测试(比如统计一段程序的运行时间)和插入日志等应用场景。
# 有了装饰器，我们就可以抽离出大量与函数功能本身无关的代码，增加一个函数的重用性。



# 试想你写了很多程序，一直运行也没啥问题。有一天老板突然让你统计每个程序都运行了多长时间并比较下运行效率。
# 此时如果你去手动修改每个程序的代码一定会让你抓狂，而且还破坏了那些程序的重用性
# 。聪明的程序员是绝不能干这种蠢事的。此时你可以编写一个 @ time_it的装饰器(代码如下所示)。
# 如果你想打印出某个函数或程序运行时间，只需在函数前面 @ 一下，是不是很帅?

import time

def time_it(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('用时:{}秒'.format(end-start))
    return inner

@time_it
def func1():
    time.sleep(2)
    print("Func1 is running.")

if __name__ == '__main__':
    func1()
