listA = [1, 'a', 2, 3, 4, 5]
#查找列表
print('find first value in list a[0]',listA[0])
#增加一个元素
listA.append(6)
print('added a value in listA',listA)
#改listA下标0处的值
listA[0]=8
print( 'after update a[0]',listA )
#删除list的元素
listA.pop(1) #删除下标为1的元素
print(listA)
listA.pop()  #不加下标默认删除list的最后一个元素
print(listA)


len(listA)  #list的长度
max(listA)  #list中的最大值
min(listA)   #list中的最小值

print('len(listA): ',len(listA), '  min(listA): ',min(listA), '   max(listA): ',max(listA))
listA.reverse()
print('reverse the element in list : ',listA)
#listA.clear()  # a =[]  清空list


#遍历列表中的元素
for item in listA:
    print('item in listA is', item)

for index in range(len(listA)):
    print('find list element by index',listA[index])

#list comprehension, 高级操作,切片
#[expression for element in iteration]
a = [1, 2, 3, 4, 5]
b = [i*i for i in a]
print(a, b)

#[expression if condition else statement for i in iteration]
c = [i*i if i < 3 else i for i in a] #如果小于3就是平方，大于就附上原来的值
print(c)


m = 3 in a
print(m)  #true

#slice #切片
print('a is: ', a)
n = a[0:3]  #0, 1, 2下标, 左包右不包
print('a[0:3] is: ', n)
a[-1] #最后一个元素
a[1:] #最后一个数字不写的话，默认是下标1到最后一个元素
a[:]# 最前面的元素到最后的元素


