#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
from functools import reduce

Tn = 0
Sn = 0
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    #Sn.append(Tn)
    Sn = Sn + Tn
    print(Tn)
#Sn = reduce(lambda x, y : x+y, Sn)
print(Sn)