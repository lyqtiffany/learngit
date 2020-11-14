# 1234567891011121314
# 找到m位是哪个数字。 比如10 =1, 11 =0, 12=1

class Solution:
    def findNthDigit(self, n):
        digit, start, count = 1, 1, 9
        while n > count: # 23>9  23>9*10*2?no
            n -= count  # n = 23 - 9 = 14
            start *= 10  # 1, 10, 100, ... start = 1*10=10
            digit += 1   # 1,  2,  3, ...  digit = 1 +1 =2
            count = 9 * start * digit  # 9, 180, 2700, ...  count = 9 *10*2
            print('n=', n, 'digit=', digit, 'start=', start, 'count=', count)
        num = start + (n -1) // digit #2  num= 10 + (14 -1) // 2 = 16
        print('num=', num)
        # #所求数位 在从数字 start 开始的第 [(n - 1) / digit][(n−1)/digit] 个 数字 中（ start为第 0 个数字）
        print('str(num)', str(num)[(n - 1) % digit])
        return int(str(num)[(n - 1) % digit])  # 转化为 string # 获得 num 的 第 (n - 1) % digit 个数位，并转化为 int

aa = Solution()
print(aa.findNthDigit(23))
print(aa.findNthDigit(15))   #123456789 1011121314 1516

#确定 15 n 所在 数字 的 位数 ，记为 digit 2 ；  23  2
#确定 15  n所在的 数字 ，记为 num 12 ；   23 16
#确定 15 是 12 中的哪一数位，并返回结果  23 shi 12 zhong de 6

