# 找到1 到100 的质数
#如果一个数只能被 1 和它本身整除，这个数就是质数



num = []
for i in range(2, 101):
    flag = 0
    for j in range(1, i+1):
        if i % j == 0:
            flag += 1
    if flag == 2:
        num.append(i)
print(num)

# !/usr/bin/python
# -*- coding: UTF-8 -*-
num = [];
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        num.append(i)
print(num)