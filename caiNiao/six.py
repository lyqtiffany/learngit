#题目：斐波那契数列。

def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a
#print(fib(10))

#方法2，使用递归
def fibo(m):
    if m == 1 or m ==2:
        return 1
    else:
        return fibo(m-1) + fibo(m-2)
#print(fibo(10))

#输出制定个数的斐波那契数列
def fibonaqi(x):
    if x == 1:
        return [1]
    elif x == 2:
        return [1, 1]
    else:
        fibs = [1, 1]
        a, b = 1, 1
        for item in range(2, x):
            a, b = b, a + b
            fibs.append(b)
        return fibs
#print(fibonaqi(6))

#第7题: 将一个列表的数据复制到另一个列表中。

origin = [1, 2, 3, 4]
afterCopy = origin[:]
print(afterCopy)