##给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

#不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


# 直接删除重复元素，pop(i)的时间复杂度为O(n)，再加上指针移动，总的时间复杂度达到O(N^2)，因此相比思路一效率偏低。

class Solution:
    def removeDuplicates(self, nums) -> int:
        a = 0
        b = 1
        while b < len(nums):
            if nums[a] == nums[b]:
                nums.pop(a)
            else:
                a += 1
                b += 1
        return len(nums),nums

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    test = Solution()
    print(test.removeDuplicates(nums))