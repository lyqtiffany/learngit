# listA = [1, 'a', 2, 3, 4, 5]
# #查找列表
# print('find first value in list a[0]',listA[0])
# #增加一个元素
# listA.append(6)
# print('added a value in listA',listA)
# #改listA下标0处的值
# listA[0]=8
# print( 'after update a[0]',listA )
# #删除list的元素
# listA.pop(1) #删除下标为1的元素
# print(listA)
# listA.pop()  #不加下标默认删除list的最后一个元素
# print(listA)
#
#
# len(listA)  #list的长度
# max(listA)  #list中的最大值
# min(listA)   #list中的最小值
#
# print('len(listA): ',len(listA), '  min(listA): ',min(listA), '   max(listA): ',max(listA))
# listA.reverse()
# print('reverse the element in list : ',listA)
# #listA.clear()  # a =[]  清空list
#
#
# #遍历列表中的元素
# for item in listA:
#     print('item in listA is', item)
#
# for index in range(len(listA)):
#     print('find list element by index',listA[index])
#
# #list comprehension, 高级操作,切片
# #[expression for element in iteration]
# a = [1, 2, 3, 4, 5]
# b = [i*i for i in a]
# print(a, b)
#
# #[expression if condition else statement for i in iteration]
# c = [i*i if i < 3 else i for i in a] #如果小于3就是平方，大于就附上原来的值
# print(c)
#
#
# m = 3 in a
# print(m)  #true
#
# #slice #切片
# print('a is: ', a)
# n = a[0:3]  #0, 1, 2下标, 左包右不包
# print('a[0:3] is: ', n)
# a[-1] #最后一个元素
# a[1:] #最后一个数字不写的话，默认是下标1到最后一个元素
# a[:]# 最前面的元素到最后的元素
#
#
#
#列表和元组
# 列表可以存放任意类型数据，存放数字，字符串，列表，元组，字典
list1 = [10, 20, 30, 40, 50]
list2 = ['A', 'B', 'C']
list3 = ['a', 33, [10, 20], {'name':'Bob', 'age': 30}, (1, 2)]
print(list1)
print(list2)
print(list3)

#修改列表，列表属于可变对象，它的值是可以修改的，字符串属于不可变对象，不能修改其中的值。
list1[0] = 98
print(list1)
str1 = 'abc'
#str1[0] = 'q' #'str' object does not support item assignment
list3[2][0] = 96 #如果需要修改子列表中的值，多用一次下标
print(list3)

#增加列表中的值
#append 添加值到列表的末尾
list1.append(99)
print(list1)
#insert 添加值到指定的位置
list1.insert(1,36) #第一个参数是添加的下标位置，第二个参数是添加的值
list1.insert(999,750) #如果下标的值超过了列表的最大下标，默认添加到末尾，此时相当于append的作用
print(list1)
#extend 这种方式其实是进行列表的拼接
list1.extend([33, 99])
list1.extend('abc')
print(list1)

#列表的删除
#pop
list1.pop() #pop不加参数时候，默认删除最后一位
list1.pop(1)#pop指定下标位置的值
a = list1.pop() #pop方式删除的值，可以用变量进行接收
print(a)
print(list1)
#remove
list1.remove(50) #根据值进行删除，效率比较低，当有多个相同的值，remove方法只删除第一个遇到的值
print(list1)
#del
del list1[0]
print(list1)

#列表中的切片
print(list1[0:2])
#切片不会改变原来列表
print(list1)
#翻转列表
print(list1[::-1])
#列表的排序
list2 = [34, 6, -1, 90, 102, 87, 99]
print(sorted(list2)) #临时排序
list2.sort() #永久排序
list2.sort(reverse=True) #倒序
print(list2[::-1])
print(list2)

#元组 元组是不可变对象，其他用法与列表一致，它不能新增、修改，删除元素
tuple1 = (10, 20, 30, 40, 50)
print(tuple1[0:2]) #元组可以使用下标或切片
#如果元组中只有一个值
tuple2 = (10,)
print(type(tuple2)) #可以用type()函数查看数据类型
#如果元组中有子列表，子列表中的值是可以修改的
tuple3 = (10, 20, [30, 40, 50])
tuple3[2][0] = 900
print(tuple3)







