#面向对象基础
#面向对象，java python
#面向过程，c

#类，实例
class Rectangle: #新建一个长方形类
    def __init__(self, length, width): #写一个初始化方法
        self.length = length #实例属性
        self. width = width
        self.jiaodu = 90 #静态属性，一般是固定值
    def permeter(self): #实例方法，只能用实例来调用，类不能直接调用实例方法
        return (self.length+self.width)*2
    def area(self): #实例方法，面积的方法
        return self.width*self.length

    @classmethod #装饰器，表示下面的方法是类方法
    def features(cls): #提到类就已经明确的，可以写成类方法，类方法可以由实例调用，也能由类调用
        print('两边的长相等，宽也相等')

    @staticmethod #声明下面的方法是静态方法
    def sumdata(a,b): #静态方法，本质上是函数，与类没有任何关系
        return a+b

rec = Rectangle(5,4) #实例
print(rec.__dict__) #打印实例的属性

# print(rec.area())  #由实例来调用实例方法
# print(rec.permeter())
# Rectangle.features() #类来调用类方法
# print(Rectangle.sumdata(1, 2)) #调用静态方法
# print(type(Rectangle.sumdata)) #<class 'function'>
# print(type(rec.features)) #<class 'method'>

#inspect模块，python的自检模块，可以判断一个对象是否是某种属性
# import inspect
# print(inspect.ismethod(rec.permeter)) #说明实例方法是方法
# print(inspect.ismethod(rec.features)) #说明类方法是方法
# print(inspect.isfunction(rec.sumdata)) #说明静态方法是函数

#继承
#1.完全继承，所有方法直接继承
# class Square(Rectangle):
#     pass
# squ = Square(6,6)
# print(squ.permeter())
# print(squ.area())

#部分继承，比如重写初始化方法,其他方法保留
# class Square(Rectangle):
#     def __init__(self, side): #修改了继承rectangle的初始化方法
#         self.length = side
#         self.width = side
# squ = Square(9)
# print(squ.permeter())
# print(squ.area())

#有时候，想在完全继承的基础上增加一些内容，用super
# class Square(Rectangle):
#     def __init__(self, side): #修改了继承rectangle的初始化方法
#         self.length = side
#         self.width = side
#
#     @classmethod
#     def features(cls):
#         super().features() #继承父类这个方法中的内容
#         #Rectangle.features() #继承父类这个方法中的内容,跟super二选一
#         print('长和宽也相等')
#
# squ = Square(9)
# print(squ.permeter())
# print(squ.area())
# squ.features()












#思考题，写一个三角形的类，里面有周长方法，面积方法，可以用海伦公式
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def permeter(self):
#         return self.a + self.b+ self.c
#     def area(self):
#         p = self.permeter()*0.5
#         s = (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
#         return s



















