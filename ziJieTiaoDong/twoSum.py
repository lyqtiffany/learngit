# class Solution:
	# def twoSum(self,nums,target):
	# 	n = len(nums)
	# 	for x in range(n):
	# 		a = target - nums[x]
	# 		if a in nums: # 判断a有没有在nums数组里
	# 			y = nums.index(a) # 有的话，那么用index获取到该数字的下标
	# 			if x == y:
	# 				continue # 同样的数字不能重复用，所以这里如果是一样的数字，那么就不满足条件，跳过
	# 			else: # 否则就返回结果
	# 				return x,y
	# 				break
	# 		else:
	# 			continue # 上面的条件都不满足就跳过，进行下一次循环'''

class Solution(object): #过一遍，如果存在目标值就返回，不存在就存到字典里
    def twoSum(self, nums, target):
        target_dict = {}
        for i, num in enumerate(nums): #i=key/index num=value
            target_num = target - num
            if target_num in target_dict:
                return [target_dict[target_num], i]
            else:
                target_dict[num] = i

if __name__ == '__main__':
    numsA = [2, 7, 11, 15, 12]
    targetA = 23
    aa = Solution()
    print(aa.twoSum(numsA, targetA))