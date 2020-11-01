#93 题目：时间函数举例3。

if __name__ == '__main__':
    from time import process_time
    start = process_time()
    for i in range(10000):
        print(i)
    end = process_time()
    print('different is %6.3f' % (end - start))
