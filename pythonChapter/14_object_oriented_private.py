#私有属性，私有方法,不能被子类继承的属性、方法,在属性的前面加__就是私有了


class Cls1:
    __a = 10 #私有属性，前面有两个下划线，不能被子类继承

    def __init__(self):
        pass

    def __yincang(self):
        print('this is a private methon')

    def aabbcc(self):
        # print(self.__a)
        self.__yincang()


cls1 = Cls1()
# cls1.__yincang() #直接用实例，找不到私有方法
# cls1.__a #直接用实例，找不到私有属性
# cls1.aabbcc() #能够打印出10,__yincang里面的内容



# class Cls2(Cls1):
#     pass
# cls2 = Cls2()
# print(cls2.__a) #父类的私有属性，不能被子类继承
# cls2.__yincang() #父类的私有方法，不能被子类继承

#所有的类都是object的子类,无论是否声明，都继承了object
# class Class1:
#     '''
#     作业书风邹宇，
#     弄水
#     '''
# class Class2(object):
#     pass
#
# print(Class1.__base__) #显示父类的名称
# print(Class2.__base__)
# print(Class1.__doc__) #显示类的注释
# print(Class1.__name__)  #显示类的名称


#多继承
# class Youqian1:
#     def money(self):
#         print('1个亿')
# class Youqian2:
#     def money2(self):
#         print('2个亿')
# class Youqian(Youqian1,Youqian2): #同时继承多个类
#     pass
# qian = Youqian()
# qian.money() #同时继承多个类,可以使用多个类的方法
# qian.money2()
#当多个父类中有多个同名的方法，按照继承的顺序进行继承


#多态
#  通过参数的变化，确定调用的类
class Animal:
    def say(self):
        pass
class Dog(Animal):
    def say(self):
        print('wangwangwang')
class Cat(Animal):
    def say(self):
        print('miaomiaomaio')

def animal_say(obj): #定义一个函数，根据传入的实例调用各自的类的方法
    obj.say()

dog = Dog()
cat = Cat()
animal_say(dog)
animal_say(cat)

from random import randint
a = randint(0,100) #生成一个随机数



