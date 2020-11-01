#题目：判断101-200之间有多少个素数，并输出所有素数。

#程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　

# num = []
# for m in range(101, 201):
#     count = 0
#     for n in range(1, m+1):
#         if m % n == 0:
#             count += 1
#     if count == 2:
#         num.append(m)
# print(num)

from math import sqrt

num = []
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, int(sqrt(i))):
        if i % j == 0:
            break
    else:
        num.append(i)
print(num)

