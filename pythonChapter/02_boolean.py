# 布尔表达式

# python中一个=表示赋值，两个==表示判断值等

# print(1 == 1)
# print('a' == 'A')#字符间的比较是比较ASCII码，a=97,A=65
# print('aA' == 'Aa')#字符串之间的比较，只比较第一位，只有第一位相同才比较后面的
# print('aA' > 'Aa') #true
#
# #true false 可以参与算术运算，True相当于1，False相当于0
# print(True+True)

list1 = [10, 20, [30, 40, 50]]
# print(30 in list1)
# print(10 in list1)
# print(30 in list1[2])

#逻辑运算符 and or
#and 有假则假，全真为真
# print(1 < 2 and 2 < 1 and 5 > 4) #False
# or 有真则真，全假则假
# print(1<2 or 2>1) #True

#逻辑运算符 and or的优先级 not > and > or
# print(3>2 and 2>3 and 7>5 or 1>0)
# print(3>2 and 2>3 and (7>5 or 1>0))

#isinstance 判断某个实例是否属于某个类，返回布尔值
# print(isinstance('12', int))
# print(isinstance(12, int))

#!=表示不等于
# print(1 != 2)
# print(not 1 > 2 or 4 > 3) #True





#思考题，python列表中浅拷贝，深拷贝的区别
import copy

listA = [1, 2, 3, 4, [66, 99]]
listD = listA #简单的赋值,不同的变量名指向同一个列表，相同的位置

listE = listA[:] #切片等价于浅拷贝

listB = copy.copy(listA) #浅拷贝

listC = copy.deepcopy(listA) #深拷贝,列表和子列表都是不同的

listA[0] = 98
listA[4][1] = 100

print('原始列表:', listA, id(listA), id(listA[-1]))
print('简单赋值:', listD, id(listD), id(listD[-1])) #打印的结果同ListA更新的值
print('切片:   ', listE, id(listE), id(listE[-1])) #浅拷贝，列表是两个不同的列表，子列表仍然指向的是同一个地址
print('浅拷贝: ', listB, id(listB), id(listB[-1]))
print('深拷贝: ', listC, id(listC), id(listC[-1]))

#在列表改变的时候，使用浅拷贝和深拷贝都可以不改变原来的列表，
#但是子列表改变的时候，使用深拷贝可以维持原来的列表，但浅拷贝不可以



# 浅拷贝
# 浅拷贝是对一个对象父级（外层）的拷贝，并不会拷贝子级（内部）。使用浅拷贝的时候，分为两种情况。
# 第一种，如果最外层的数据类型是可变的，比如说列表，字典等，浅拷贝会开启新的地址空间去存放。
# 第二种，如果最外层的数据类型是不可变的，比如元组，字符串等，浅拷贝对象的时候，还是引用对象的地址空间。
# 深拷贝
# 深拷贝对一个对象是所有层次的拷贝（递归），内部和外部都会被拷贝过来。
# 深拷贝也分两种情况：
# 第一种，最外层数据类型可变。这个时候，内部和外部的都会拷贝过来。
# 第二种，外层数据类型不可变，如果里面是可变数据类型，会新开辟地址空间存放。如果内部数据类型不可变，才会如同浅拷贝一样，是对地址的引用。
#







