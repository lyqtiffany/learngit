#难题 55 学习使用按位取反~。 #~x等于-x-1   # 二进制数在内存中以补码的形式存储。
# 按位取反：二进制每一位取反，0 变 1，1 变 0。
# 最高位为符号位，正数的符号位为 0，负数为 1。
# 对正数来说，计算补码，最高位为 0，其余各位代表数值本身(以二进制表示)，如 +42 的补码为 00101010。
# 对负数而言，把该数绝对值的补码按位取反，然后对整个数加1，即得该数的补码。如 -42 的补码为 11010110(00101010 按位取反 11010101+1 即 11010110)。
#
# ~9 的计算步骤：

# 转二进制：0 1001
# 计算补码：0 1001
# 按位取反：1 0110
# 转为原码：
# 按位取反：1 1001
# 末位加 1：1 1010
# 符号位为 1 是负数，即 -10

a = 7
b = ~a  #~x等于-x-1
c = -7
d = ~c  #~x等于-x-1
print('变量 a 取反结果为： %d' % b)  #-8
print('变量 c 取反结果为： %d' % d)  #6
# ～7，对 7 进行取反，7的原码是0000 0111。取反得到1111 1000，是负数。某个数x的补码是1111 1000（由补码求原码），
# 取反0000 0111, +1->0000 1000=8,加上标点符号得到-8
#
# ~-7 对-7进行取反，-7是负数，所以它是7的补码表示的，所以转为已知7的补码，求对应的原码，然后取反，7的补码是 00000111 对补码取反得到 11111000，
# 加1,11111001，得到原码，取反00000110加上标点正号得到6。
'''首先你要明白的几个知识点: 
(1)在计算机里面,负数是以补码存储的 
(2)原码求补码:取反,+1 
(3)补码求原码:取反,+1 
(4)取反操作是在原码上进行的!
实际的计算结果: ~4 = -5, ~-5 = 4
依据上述第四条,我们的解释思路是,确定原码===> 取反 
(1) 求~4, 我们用八进制来表示4: 
4的原码: 0000 0100  取反得到: 1111 1011, 观察符号,是负数,因为负数以补码存储的,所以问题转化为: 
某个数x的补码是1111 1011,求x的值(由补码求原码) 取反: 0000 0100  +1: 0000 0101 = 5, 加上标点符号(负号) 得到结果: -5
(2) 求 ~-5,同理用八进制表示-5: 
因为-5是负数,所以它是以5的补码表示的,所以转化为已知5的补码,求对应的原码,然后在取反. 
5补码: 0000 0101, 
取反: 1111 1010 
+1: 1111 1011, 得到原码 
取反: 0000 0100 = 4 ,加上标点负号(正号)得到结果:4'''