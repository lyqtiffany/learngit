#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

a = int(input('enter a number'))
x = str(a)
flag = True
for i in range(len(x)//2):
    if x[i] != x[-i-1]:
        flag = False
        break
if flag:
    print('it is huiwen')
else:
    print('not huiwen')

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

    # 方法二: 将int转化成str类型: 双指针 (指针的性能一直都挺高的)
    # 复杂度: O(n)
    def isPalindrome(x: int) -> bool:
        lst = list(str(x))
        L, R = 0, len(lst)-1
        while L <= R:
            if lst[L] != lst[R]:
                return  False
            L += 1
            R -= 1
        return True

