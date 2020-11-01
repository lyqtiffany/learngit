# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。


for item in range(2, 1001):
    k = []
    sum = item # 6
    for j in range(1, item):
        if item % j == 0: # 6 chu 1, 2 3
            sum -= j   # sum= 6 -1-2 -3
            k.append(j)  #k =1 2 3
    if sum == 0:
        print(item, k)
