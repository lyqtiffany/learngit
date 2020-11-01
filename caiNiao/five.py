# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#冒泡排序

l = []
for i in range(3):
    x = int(input('ineteger: \n'))
    l.append(x)
for i in range(3):
    for j in range(i+1, 3):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
#l.sort()
print(l)