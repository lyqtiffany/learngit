#找出回文字符串

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #将字符串全部变为小写
        s = s.lower()
        a = []
        #如果是字母或者数字，添加到数组元素中
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                a.append(i)
        #比较顺序跟逆序，返回结果
        return(a[::1]==a[::-1])


if __name__ == '__main__':
    test = Solution()
    string1 = 'abccbA'
    print(test.isPalindrome(string1))