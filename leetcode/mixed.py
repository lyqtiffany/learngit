
#1, 求两数之和
'''from typing import List
nums1 = [2, 7, 11, 15, 4, 5]
target1 = 9
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print('index of twoNum', i , j)
twoSum(nums1, target1)
'''

#2. 数字反转
from typing import List

'''aNum = -123
bNum = 4567
def reverse(num):
    if -10 < num < 10:
        return num
    str_num = str(num)
    if str_num[0] != '-':
        str_num = str_num[::-1]
        num = int(str_num)
        print(num)
    else:
        str_num = str_num[:0:-1]
        num = int(str_num)
        num = -num
        print(num)
    return num if -2147483648 < num < 2147483647 else 0

print(str(12345)[::1])
print(str(12345)[::-1])'''

'''def reverse(x) :
    num = abs(x)
    new_num = 0
    while num:
        new_num = new_num * 10 + num % 10
        num //= 10
    new_num = new_num if x > 0 else -new_num
    print(new_num)
    return new_num if - 2 ** 31 < new_num < 2 ** 31 - 1 else 0'''
'''reverse(aNum)
reverse(bNum)'''

#回转数字
'''numA= 121
numB= -10
def checkReverse(num):
    if num < 0:
        print('false')
    str_num = str(num)
    if str_num == str_num[::-1]:
        print('yes')
    else:
        print('false')
checkReverse(numB)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

defOb = Solution()
print(defOb.isPalindrome(numA))
print(defOb.isPalindrome(numB))'''

#!usr/bin/env python
#encoding:utf-8
'''''
功能：找出数组中第2大的数字
'''
'''def find_Second_large_num(num_list):
  #直接排序,输出倒数第二个数即可
  tmp_list=sorted(num_list)
  print('Second_large_num is:', tmp_list[-2])
  #设置两个标志位一个存储最大数一个存储次大数
  #two存储次大值，one存储最大值，遍历一次数组即可，先判断是否大于one，若大于将one的
  #值给two，将num_list[i]的值给one；否则比较是否大于two，若大于直接将num_list[i]的
  #值给two；否则pass
  one=num_list[0]
  two=num_list[0]
  for i in range(1,len(num_list)):
    if num_list[i]>one:
      two=one
      one=num_list[i]
    elif num_list[i]>two and num_list[i]!=one:
        two=num_list[i]
    else:
      pass
  print('Second_large_num is:', two)
if __name__ == '__main__':
  num_list=[34,11,23,56,78,0,9,12,3,7,5]
  find_Second_large_num(num_list)'''

##剑指 Offer 10- II. 青蛙跳台阶问题
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
'''class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

dd = Solution()
print(dd.numWays(5))

#在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]: return c
        return ' '
'''
#88. 合并两个有序数组
#给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 初始化ums1 和 nums2 的元素数量分别为m 和 n 。
# 你可以假设nums1有足够的空间（空间大小大于或等于m + n）来保存 nums2 中的元素。

'''class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if 0 == n:
      pass
    elif 0 == m:
      nums1[:n] = nums2[:n]
    else:
      a, b = m - 1, n - 1
      k = m + n - 1
      while (a >= 0) and (b >= 0):
        if nums1[a] <= nums2[b]:  # nums1 的元素尽量少动
          nums1[k] = nums2[b]
          k -= 1
          b -= 1
        else:
          nums1[k] = nums1[a]
          k -= 1
          a -= 1
      if (a >= 0):
        pass
      if (b >= 0):
        nums1[k - b:k + 1] = nums2[:b + 1]  # 必然有 k-b == 0，因为剩下的是最小的，必然是copy到最前面'''


'''class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)
        return nums1'''



'''class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of nums1.
        nums1_copy = nums1[:m]
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2.
        p1 = 0
        p2 = 0

        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
n1 = Solution()
print(n1.merge(nums1, 3, nums2, 2))'''


#index返回数组下标
'''l = [3, 2, 1, 0, 4, 5]
print(l.index(max(l)))  # 返回list最大值位置'''


#在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
# 请找出数组中任意一个重复的数字。
'''class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        n = len(nums)
        for index in range(1, n):
            if pre == nums[index]:
                return pre
            pre = nums[index]


aaa = [2, 3, 1, 0, 2, 5, 3, 5]
aaaS = Solution()
print(aaaS.findRepeatNumber(aaa))'''

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
'''class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
'''
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
'''class Solution:
    def numWays(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]%1000000007
aa = Solution()
bb = print(aa.numWays(7))'''


'''#合并两个数组
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)
        return nums1
numA = [1, 2, 5, 7, 9]
numB = [2, 4, 6, 7]
aa = Solution()
print(aa.merge(numA, 5, numB, 4))'''
'''
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        n = len(nums)
        for index in range(1, n):
            if pre == nums[index]:
                return pre
            pre = nums[index]'''


'''#判断是否是回文数字
class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
defOb = Solution()
print(defOb.isPalindrome(1521))'''

from selenium import  webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("test tif")
















