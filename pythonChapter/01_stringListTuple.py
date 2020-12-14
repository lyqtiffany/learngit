mm = '''危楼高百尺，   #时候需要换行的情况
手可摘星辰
 '''
# print(mm)
#三引号，可以表达字符串中的换行符，制表符等


#字符串的拼接
a1 = 'h1'
a2 = 'h2'
# print(a1 + 'aaa' + a2)
# print(1+2)
# print('1'+ 2) #会报错，不能拼接字符串加整数
# print('1'*2) #把1这个字符串打印两次

#float类型，15位之后的精度就不是很准确了
#type()函数，返回对象的数据类型
# print(2*1.0) #int型跟float型进行算术运算，结果一般是float类型
#int()将对象转化为整数型 #str()将对象转化为字符串类型

# print(int('12.6')) #int 型不能转字符串类型的小数
# print(int(12.6))  #int转化小数（不带括号）成功
# print(int('13'))  #int转化字符串（里面是整数）成功

#转义符\n 表示换行符， \t表示制表符
# print('d:\note.txt')
# print('d:\\note.txt') #让转义符不生效的方式1.前面再加一个\,让后面的\不产生特殊含义
# print(r'd:\note.txt')  #让转义符不生效的方式2，字符串前面加r,后面字符串的转义符都不生效
# print('d:/note.txt')  #让转义符不生效的方式3，改成/,指向路径时，可以使用/代替\

#字符串的下标从0开始
str6 = 'abcde'
# print(str6[2])
#len()函数，返回字符串的长度
# print(len(str6))
# str6[0] = 'p' #字符串是不可变对象，不能通过下标修改其中的某一位
# str6='p' #相当于给str6重新赋值

#字符串的切片
#切片不影响原来数据
# print(str6[0:3])
# print(str6[0:]) #从下标的第二位开始取值，后面的全取
# print(str6[:]) #完整的切片，相当于str6的复制体
# #id()函数返回对象在内存中的编号
# print(id(str6), id(str6[:])) #id()函数查看到完整的切片跟原来字符串指向同一个地址
# print(id(str6), id(str6[:3])) #不是指向同一个地址了

# print(str6[::2]) # 'abcde' 取到里面的ace

# 倒着取str6
# print(str6[::-1])
str9 ='上海自来水来自海上' #回文字符串
# print(str9)
# print(str9[::-1])
# print(str6)
# print(str6[4:2:-1]) #ed，#取到下标4和3,2是取不到的。从后向前取，步长必须为负数才可以取值，终止值始终取不到






# list列表
#list可以存放任意数据类型
list1 = [102, 'forloop', [10,20], (11,22), {'A': 'apple'}]
# print(list1)
#排序需要是同一类型的列表才能排序

#list是可变对象，可以通过下标修改某个位置的值
list2 = [10, 20, 30, 40, 50]
# list2[0] = 99 #把第0位改成99
# print(list2)

#增
#append 的方式，添加到列表最后
# list2.append(60)
# print(list2)
#
# #insert的方式，添加到指定位置
# list2.insert(2,66)
# print(list2)
# list2.insert(999,77) #超过下标，添加到列表最后，同append
# print(list2)

#extend,list 的拼接
list2.extend([123]) #list2 and [123]拼接 #[10, 20, 66, 30, 40, 50, 60, 77, 123]
# print(list2)

list2.extend('123') #会将'123'拆分成['1', '2', '3'],再拼接到list2的最后面
# print(list2)

#列表的删除
# pop的方式，不填下标时，删除最后一位
# list2.pop()
# print(list2)
# # pop的方式, 加上下标，删除指定位置的元素
# list2.pop(1)
# print(list2)

#remove根据列表的值来删除
list2.remove(30) #根据列表的值来删除，有相同的值，值删除碰到的第一个

#del
#del list2[0] #删除指定下标
#del 删除整个列表
# del list2

#列表的切片 [起始值：终止值：步长]
list3 = [11, 22, 33, 44, 55, 66]
# print(list3[1:3]) # 取 22, 33
# print(list3[2:0:-1]) # 取 33, 22 #-1的时候才能从起始值往左走
# print(list3[-4:-6:-1]) # 取 33, 22
# print(list3[-4:0:-1]) # 取 33, 22

#列表的切片不会影响原来的列表
# print(id(list3))
# print(id(list3[:])) #原数据的复制体，内存中存放的位置不同
# 列表中同一个位置的正下标的绝对值+它负下标的绝对值=列表长度



#元组，元组跟列表类似，都可以使用下标和切片，都可以存放各种类型的数据
#元组是不可变对象，不能通过下标修改元组里面的值
#元组没有唯一性的限制
# tuple1 = (10,20,[30,36,72])
# #元组的切片，类似列表
# #tuple1[0] = 90 #这样写会报错
# tuple1[2][1]=99
# print(tuple1) #可以修改元组里面的子列表
#
# fake_tuple2 = (110)
# print(type(fake_tuple2)) #int
#
# tuple3 = (113, )
# print(type(tuple3)) #tuple只有一个值时，需要加逗号来确定是元组

# tuple1 = (100,)
# print(type(100,))
# print(type((100,)))
# print(type(tuple1))


#斐波那契数列
# 1,1,2,3,5,8,13,21,34,55
# list1 = []
# for i in range(20):
#     if len(list1) < 2:
#         list1.append(1)
#     else:
#         list1.append(list1[-2]+list1[-1])
# print(list1)
#
# tupleD = (1, (2, 3))
# print(tupleD)

# import time
# for i in range(10, -1, -1):
#     if i != 0:
#         print('\r', f'倒计时{i}秒', end='', flush=True)
#         time.sleep(1)
#         #\r 光标回到行首
#         #end = '' 每次print之后不换行
#     else:
#         print('\r', '倒计时结束')

import math
#
# print(int(5.6)) #5 向下取整 #
# print(round(5.66)) # 6 向上取整
# print(math.ceil(4.85))  # 5向上取整

info = 'name is tom'
# print(info[8:10]) #to
# print(info[-1:-4]) #空
# print(info[8:-1]) #to
# print(info[-3:]) #tom

# print('a'.join(info)) #naaamaea aiasa ataoam
# print(info.index('m',10))

st5 = 'agcadssadjkl'
print(st5.index('a',3))
# print(st5.find('x')) #find通过元素找索引，可切片，找不到报错，index，找不到返回-1
# print(st5.startswith('a')) #startswith 判断以什么为开头，endswith 判断以什么为结尾返回的是布尔量。



#7、find()通过元素找索引,可以整体找,可以切片,找不到则返回-1
# str = "hi Alex"
# print(str.find('l'))          #4
# print(str.find('Alex'))       #3
# print(str.find('i',1,4))      #1
# print(str.find('L'))          #-1
#
# #8、index()通过元素找索引,可以整体找,可以切片,找不到会报错
# str = "hi Alex"
# print(str.index('x'))   #6

# with open('d:/pythonCourse/file1.txt') as file1:
#     # print(file1.readlines()) # 返回列表
#     # print(file1.read()) #返回str
#     print(file1.read().splitlines()) #返回列表

# print(int("5"))
# print(float(6))


# for i in range(1, 6):
#     if i % 3 == 0:
#         break
#     else:
#         print(i, end=',')


# str1 = "Runoob example....wow!!!"
# str2 = "exam"
# print(str1.find(str2, 4))
#
# dict1 = {}
# dict2 = {('sad', 5):456}

