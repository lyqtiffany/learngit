# 26. 删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:  # 单独判断列表长度为1的情况，因为之后的for循环从下标1开始
            return 1
        temp_num = nums[0]
        count = 0  # for循环中动态删除列表元素，列表缩短，为了防止下标溢出需要用count标记删除元素个数
        for index, num in enumerate(nums[1:]):
            if temp_num == num:  # 元素相等就删除
                del nums[index - count]
                count += 1
            else:
                temp_num = num
        return len(nums)

    def removeDuplicatesB(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        while (j < len(nums)):
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1



aa = [1, 2, 4, 4, 5, 6, 7]
print(Solution().removeDuplicates(aa))
print(Solution().removeDuplicatesB(aa))