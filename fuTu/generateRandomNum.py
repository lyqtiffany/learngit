# 每隔2s随机生成100个数字

import random
number = []
for i in range(0, 100):
    num = random.randint(0,100)
    number.append(num)
print(number)