#数组中出现次数超过一半的数字
#数组排序法版本的Python 3代码：

# class Solution: #数组排序法版本的Python 3代码：
#     def majorityElement(self, nums):
#         """
#         组排序法
#         时间复杂度： O(NlogN)， Python内置排序算法Timsort的时间复杂度
#         空间复杂度：不需要用到额外的空间
#         :param nums:
#         :return:
#         """
#         nums.sort()
#         return nums[len(nums) // 2]

# 使用字典进行搜索
# 我们使用字典这种数据结构,也就是哈希表来进行查找.
# 开始遍历整个数组,如果当前数字没有在字典中,就把它加入进去,如果在字典中,则把它的数量加 1 ,接着判断下它的数量是否是大于整个数组的一半,
# 如果是的话,则直接返回当前数值,否则,继续遍历.
# 由于字典的查找时间复杂度为O(1),所以总的时间复杂度为O(n),空间复杂度为O(n)

class Solution(object): #使用字典进行搜索 #数组中出现次数超过一半的数字
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        write = {}
        for i in nums:
            if i not in write:
                write[i] = 1
            else:
                write[i] += 1
                if write[i] > (len(nums) // 2):
                    return i
        return None

if __name__ == '__main__':
    test = Solution()
    list1 = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(test.majorityElement(list1))