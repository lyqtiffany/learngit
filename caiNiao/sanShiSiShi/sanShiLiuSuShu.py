#题目：求100之内的素数。

for num in range(1,100):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break  #break之后测试下一个num
        else:
            print(num)

num = []
for i in range(2, 101):
    flag = 0
    for j in range(1, i+1):
        if i % j == 0:
            flag += 1
    if flag == 2:
        num.append(i)
print(num)