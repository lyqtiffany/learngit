#32 按相反的顺序输出列表的值。

a = ['one', 'two', 'three']
for i in a[::-1]:
    print(i)

#33 题目：按逗号分隔列表。  #join()是一个字符串方法，它返回被子字符串连接的字符串。
L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print(s1)


list1 = ['1', '2', '3', '4']
s = "-"
s = s.join(list1)
print(s)