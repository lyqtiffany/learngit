# 每隔2s随机生成10个数字,范围是0到10
import time
import random

for j in range(1,10): #会打印9次
    number = []
    time.sleep(2)
    for i in range(0, 10):
        num = random.randint(0,10)
        number.append(num)
    print(number)