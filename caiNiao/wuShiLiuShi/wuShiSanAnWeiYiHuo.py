#53 题目：学习使用按位异或 ^ 。
# 两位异则1，两位同则0
#程序分析：0^0=0; 0^1=1; 1^0=1; 1^1=0

if __name__ == '__main__':
    a = 77
    b = a ^ 3
    print('The a ^ 3 = %d' % b)
    b ^= 7
    print('The  ^ b = %d' % b)
    # 77 = 64 + 0*16 + 1*8+ 1*4+ 0*2+ 1*1
    #     101101  ^ 11= 101110 = 78
    # 101110 ^ 111 = 101001 = 64+8+1=73