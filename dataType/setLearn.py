#set {}组成, 一般集合里面放相同类型的元素，支持增删改查
#集合里面所有的元素都是唯一的，无序性，不方便用查
#一般用in 操作


z = {1, 1, 1.5, 'abc'}
print(z) # 打印出来是 {1, 'abc', 1.5}
y = 'abc' in z  #查找某个元素是不是在集合里面
print("'abc' in z  or not: ", y)
z.add(3)
print('after add 3 for z: ', z) #增加元素也是无序的 {1, 3, 'abc', 1.5}
z.update({4,5}) #一次性加两个值
print('z.update({4,5}) #一次性加两个值: ', z)

xx = {'apple', 'banana', 'cherry'}
yy = {'google', 'microsoft', 'apple'}
xx.update(yy) #把一个集合插入当前集合
print(xx)

#删除指定元素用remove
z.remove(1.5) ##删除指定元素用remove
print('z.remove(1.5): ',z)
z.pop()#删除随机元素用pop
print('z.pop(): ',z)

#set可以用min max min
#set 常用 减法 - ， 与&      或 |    a^b
a = {1, 2, 3}
b = {2, 5, 9}
# a - b: a有b没有的元素 {1,3}
# a | b : a有或者b有的元素 {1, 2, 3, 5, 9}
# a & b : a有并且b有的元素 {2}
# a ^ b: a和b不同时有的元素，只存在a b其中一个集合的元素{1, 3, 5, 9}
print('a-b: ', a - b)
print('a|b: ', a | b)
print('a&b: ', a & b)
print('a^b: ', a ^ b)


