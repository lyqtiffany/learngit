#字典 {:} 键值对  无序性

dict = {'name':'learning', 'age': 18}
print(dict)

# #查
print(dict['name']) #learning
#增
dict['platform'] = 'bilibili' #加入新的key
print(dict)
# 改
dict['platform'] = 'youtube' #修改已有的key对应的值
print(dict)
# 删
dict.pop('platform')#删除已有的key，值也会一起删除
print(dict)


# 遍历字典
atest = 'name' in dict  #判断key是否存在于字典
print(atest)

for key in dict: #只打印key
    print('只打印key:', key)

for keykey in dict.keys(): #只打印value
    print('只打印keykey:',keykey)

for value in dict.values(): #只打印value
    print('只打印value:',value)



dictB = {'name':'learning', 'age': 18}
for k,v in dict.items(): #打印key and value
    print(k,v)
    for kk, vv in dictB.items():   #遍历字典，比较两个字典是否相等
        if k== kk and v == vv:
            print('tttture')



import operator
print(operator.eq(dict, dictB))






