# 暂停一秒输出。 使用 time 模块的 sleep() 函数。

import time


myD = {1: 'a', 2: 'b', 3: 'c'}
for key, value in myD.items():
    print(key, value)
    time.sleep(1) #暂停1秒