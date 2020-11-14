
'''class Solution:
    def twoSum(self, nums, target):
        num = nums.copy()
        n = 0
        while len(num):
            i = num.pop(0)
            n += 1
            if target-i in num:
                a = nums.index(i)
                b = num.index(target-i)+n
                return [a,b]'''



#两数之和用最简单的遍历来求
#要注意第一个for循环的i从0开始，第二个for循环要从i+1开始
'''class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]'''

'''
class Solution:
	def twoSum(self,nums,target):
		n = len(nums)
		for x in range(n):
			a = target - nums[x]
			if a in nums: # 判断a有没有在nums数组里
				y = nums.index(a) # 有的话，那么用index获取到该数字的下标
				if x == y:
					continue # 同样的数字不能重复用，所以这里如果是一样的数字，那么就不满足条件，跳过
				else: # 否则就返回结果
					return x,y
					break
			else:
				continue # 上面的条件都不满足就跳过，进行下一次循环'''

'''numsA = [2, 7, 11, 15, 12]
targetA = 23
aa = Solution()
print(aa.twoSum(numsA, targetA))'''


'''if __name__ == '__main__':
    numsA = [2, 7, 11, 15, 12]
    targetA = 23
    print(Solution().twoSum(numsA, targetA))'''


'''class Solution:
	def twoSum(self, nums, target):
		n = len(nums)
		for i in range(n):
			for j in range(i+1, n):
				if target == nums[i] + nums[j]:
					return [i, j]


if __name__ == '__main__':
    numsA = [2, 7, 11, 15, 12]
    targetA = 23
    print(Solution().twoSum(numsA, targetA))'''


#通过创建字典，将nums里的值和序号对应起来，并创建另一个字典存储目标值（Target）-nums的值，通过判断该值是否在nums内进行判断并返回其对应索引值
def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 创建字典一，存储输入列表的元素值和对应索引
        num_dict = {nums[i]:i for i in range(len(nums))}
        print(num_dict)
        # 创建另一个字典，存储target-列表中的元素的值，小詹称为num_r吧，好表达
        num_dict2 = {i:target-nums[i] for i in range(len(nums))}
        print(num_dict2)
        # 判断num_r是否是输入列表中的元素，如果是返回索引值，不是则往下进行
        result = []
        for i in range(len(nums)):
            j = num_dict.get(num_dict2.get(i))
            if (j is not None) and (j!=i):
                result = [i,j]
                break
        return result
numsA = [2, 7, 11, 15, 12]
targetA = 23
print(twoSum(numsA, targetA))








