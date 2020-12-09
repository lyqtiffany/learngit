#数组的值从小到大排序
class Solution:
    def bubbleSort(self, nums):
        count = 0
        for i in range(0, len(nums)): # i = 0， 最大下标是只到n-1， 数组8个元素，下标是0-7
            for j in range(0, len(nums) -1 - i ): #j = 0-第1个数要和后面的7个数比较大小，range就是0-6,第一次遍历完，找到了最大的数
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                else:
                    continue
                print(nums)
                count += 1
        return nums, count
        #print('count times', count)
numsA = [53, 49, 34, 26, 19, 11, 2, 0]
aaNums = Solution()
print(aaNums.bubbleSort(numsA))




