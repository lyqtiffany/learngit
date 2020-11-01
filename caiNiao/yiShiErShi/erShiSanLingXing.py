#print 会调用 sys.stdout 的 write 方法
#例如以下两行在事实上等价：
#stdout.write('hello Python'+'\n')
#print 'hello Python

#打印出如下图案（菱形）:

from sys import  stdout
for i in range(4):
    for j in range(2 - i + 1):  # i=0, j=012, k=0-- i=1, j=01, k=012-- i=2, j=0,k=01234,--i=3,j=0,k=0123456
                                # 3 1--2 3-- 1 5-- 0 7
        stdout.write(' ')
    for k in range(2 * i +1):
        stdout.write('*')
    print()
for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print()

#方法2
for i in range(-4,5):
    if i<0:       #if..else..条件可以写成三木运算符形式
        j=-i      #  j=-i if i<0 else j=i
    else:
        j=i
    #先是j个空格，然后打印（9-2j）个* ，后面的都是空格，在屏幕上不显示，可以不打印#
    print(' '*j+'*'*(9-2*j))
# 行号	    前置空格数	*数	后置空格数
# 1 (-4)	4	        1	 4
# 2 (-3)	3	        3	 3
# 3 (-2)	2	        5	 2
# 4 (-1)	1	        7	 1
# 5 ( 0)	0	        9	 0
# 6 ( 1)	1	        7	 1
# 7 ( 2)	2	        5	 2
# 8 ( 3)	3	        3	 3
# 9 ( 4)	4	        1	 4

