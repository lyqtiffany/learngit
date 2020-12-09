#函数就是将一段代码封装起来，在有需要的时候调用

# def sumdata(a,b):#a,b是形参
#     print(a+b)
# sumdata(10,11)#实参，简略写法


#函数的缺省值，默认参数
# def sumdata2(a=1,b=2):#a,b是形参
#     print(a+b)
# sumdata2()#实参,都使用默认参数
# sumdata2(10)#a用用户输入的值10，b用默认值2
# sumdata2(a=3,b=4)#a用3，b用4，完整写法，完整写法可以调换顺序写成b=4,a=3
# sumdata2(3,b=7)#也是正确写法，可以先简略写法，后完整写法，但是不能反过来
# # sumdata2(a=4,1)#不可以这样写

#函数的返回值
# def sumdata(a,b):#a,b是形参
#     print(a+b)

# print(sumdata(10,11))#此时再返回None, sumdata函数内部没有定义返回值


# def sumdata(a,b):#a,b是形参
#     return a+b   #return执行后，直接跳出函数
#     return 'Hello'  #第一个return以后的行，是不可达语句
# print(sumdata(10,11))

# def absFunc(n):
#     if n >= 0:
#         return n
#     else:
#         return -n
# print(absFunc(-12))

#h函数返回多个值时，用逗号隔开，其返回结果，放在一个元组里
# def sumdata(a=1,b=2):
#     return a+b, a-b, a*b, a**b  #返回结果在一个元组里面
# print(sumdata(3,2))
#
# def sumdata3(a=1,b=2):
#     return [a+b, a-b, a*b, a**b] #返回结果是一个列表
# print(sumdata3(3,2))
#
# def sumdata4(a=1,b=2):
#     return [a+b, a-b], [a*b, a**b] #返回结果是一个元组里面包含两个列表
# print(sumdata4(3,2))


# 可变长度参数*args允许0到n个参数
# print(1,22,33) #print函数的定义就用到了可变长度参数
def sumdata5(a=1, *args):
    return a, *args  #*args可以是0到n个参数，带*的不需要额外解包
    #return a, args #args里面的参数会额外多一层元组，称之为包
# print(sumdata5(1,2,2))
# print(sumdata5(1,3))
# print(sumdata5(1))


#**kwargs关键字参数,允许用户输入0到无限个参数，参数必须是赋值的形式，显示出来的效果是字典
def func2(a,**kwargs):
    return a, kwargs
# print(func2(35, x=20, y=30, z=100))





'''A girl come in, the name is Jack, level 955;
其中包含的 the name is 后面会跟着人名，随后紧跟一个逗号， 这是固定的格式。
其它部分可能都是会变化的，比如，可能是下面这些
A old lady come in, the name is Mary, level 94454
A pretty boy come in, the name is Patrick, level 194
请大家实现一个函数，名为getName，如下所示
def getName(srcStr):
    函数体
该函数的参数srcStr 是上面所描述的格式字符串（只处理一行），该函数需要将其中的人名获取出来，并返回
比如 调用 getName('A old lady come in, the name is Mary, level 94454')
返回结果应该是 'Mary'''


testStr = 'this is a man, the name is Jack, level 101'
def getName(srcStr):
    a = srcStr.split('the name is')[-1]
    b = a.split(',')[0]
    b = b.strip()
    return b
print(getName(testStr))


import re
def getName(string):
    name = re.findall(r"the name is ([a-zA-Z]*),", string)
    return name[0]

string = "A girl s come in, the name is Jack, level 955"
print(getName(string))

# def e1():
#     print('in e1')
#     return False
# print(False and e1()) #False # False and,一假直接假，and后面的不会执行
# print(e1() and False) #in e1  False
# print(True or e1()) #True #True or一真为真，后面的不会执行
# print(False or e1()) #in e1  False

#值引用，当函数调用一个不可变对象（字符串，元组），如果修改了值，不会影响被调用对象本身的值
# def t2(para):
#     para =3
# b = 'a'
# t2(b)
# print(b) # a

# 当函数调用一个可变对象（列表），如果修改了值，会影响被调用对象本身的值
# def t2(para):
#     para[0] =3
# b = ['a']
# t2(b)
# print(b) # [3]

#函数重新赋值了一个变量，跟原来的变量没什么关系
# def t2(para):
#     para =3
# b = [1]
# t2(b)
# print(b) # [1]


