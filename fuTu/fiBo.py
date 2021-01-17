def fibo(x): #获取斐波那契序列
    """
    :param x: the x number in fibo
    :return:the x number in fibo
    """
    if x < 1 or type(x) != int:
        return None
    elif x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fibo(x-2) + fibo(x-1)

def getN_num_in_Fibo(nums):
    num_list = []
    for i in range(1, nums+1): #下标从1 开始，需要取到第n个则需要写到n+1
        num_list.append(fibo(i))
    return num_list

print(getN_num_in_Fibo(12)) #打印斐波那契数列里面的前12个数字