listA = [1, 'a', 2, 3, 4, 5]
#查找
print('find first value in list a[0]',listA[0])
#增加一个元素
listA.append(6)
print('added a value in listA',listA)
#改listA下标0处的值
listA[0]=8
print( 'after update a[0]',listA )
#删除list的元素
listA.pop(1)
print(listA)
listA.pop()  #不加下标默认删除list的最后一个元素
print(listA)


len(listA)  #list的长度
max(listA)  #list中的最大值
min(listA)   #list中的最小值

print('len(listA): ',len(listA), 'min(listA): ',min(listA), 'max(listA): ',max(listA))
listA.reverse()
print('reverse the element in list : ',listA)
#listA.clear()  # a =[]  清空list



b = (1,)  #一个元素的tuple元组