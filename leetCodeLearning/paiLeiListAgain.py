# 给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
# 请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。
# 示例 1：

# 输入：nums = [2,5,1,3,4,7], n = 3
# 输出：[2,3,5,4,1,7]
# 解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]

'''class Solution:
	def shuffle(self,nums,n):
		nums[::2],nums[1::2]=nums[:n],nums[n:]
		return nums'''

'''class Solution:
    def shuffle(self, nums, n) :
        x = nums[:n]
        y = nums[n:]
        result = []
        for i in range(n):
            result.append(x[i])
            result.append(y[i])
        return result'''

'''class Solution:
    def shuffle(self, nums, n) :
        i,j=0,n
        c=[]
        while i<n:
            c.append(nums[i])
            c.append(nums[j])
            i+=1
            j+=1
        return c'''

class Solution(object):
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result

nums = [2,5,1,3,4,7]
aa = Solution()
print(aa.shuffle(nums,3))
