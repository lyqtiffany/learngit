#字典，存放若干个键值对的一个对象，字典是可变对象


#字典永远以键值对的形式出现
#字典是无序的,列表是有序的
# dict1 = {'A': 'apple', 'B' : 'book'}
# dict2 = {'B': 'book', 'A': 'apple'}
# print(dict1 == dict2)
#
# list1 = [10, 20]
# list2 = [20, 10]
# print(list1 == list2)

#字典可以存放的数据类型
dict1 = {(1,2): 'apple', 'B' : 'book'} #键：数字，字符串，元组，键不能用列表，字典
#字典的键，只能用不可变对象， 值可以是任意对象

#字典是可变对象，可以进行新增，修改，删除
#新增,如果字典里面没有这个键，就新增,键是唯一的
dict1['C'] = 'cat'
#新增,如果字典里面有这个键，就修改,键是唯一的
dict1['B'] = 'B updated'
# print(dict1)

#新增或者修改可以用update方法
dict1.update({'E': 'eleven', 'D':'date'})
# print(dict1)

#删除字典中的键值对
del dict1['E']
# print(id(dict1))

#清空字典
# dict1 = {} #重新定义了一个字典，内存的地址发生了变化
# dict1.clear() #内存中的地址不变
# print(id(dict1))

#判断某个键是否在字典中，用In或者not in判断，判断的依据是键，不是值
# print('apple' in dict1)

#字典的遍历
#遍历列表里面的键
# print(dict1.keys()) #输出类列表，可以遍历，不能用下标 dict_keys([(1, 2), 'B', 'C', 'D'])
# for one in dict1.keys():
#     print(one)
# list1 = list(dict1.keys()) #使用list()函数类列表转换成列表
# print(list1)
##遍历列表里面的值
# print(dict1.values()) #输出类列表，可以遍历，不能用下标
# for one in dict1.values():
#     print(one)
#同时遍历列表里面的键和值
# print(dict1.items()) #输出类列表，可以遍历，不能用下标
# for key, value in dict1.items():
#     print(key, value)

#思考题，统计1000以内，有多少个数字包含3
count = 0
for i in range(1,34):
    if '3' in str(i):
        count = count+1 #3 13 23 30 31 32 33
        print(i)
print(count)
#列表推导式
print(len([i for i in range(1,10000) if '3' in str(i)]))