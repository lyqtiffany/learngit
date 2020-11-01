# leetcode 78
# [1, 2, 3] 返回不重复的子集[], [1], [2], [3], [1, 2], [1,3], [2,3], [1,2,3]

class Solution:
    def subsets( nums):
        res = [[]]
        for num in nums:
            #res += [cur+[num] for cur in res]
            for cur in res:
                temp = [cur + [num]]
                res =res + temp
        return res
if __name__ == '__main__':
    aa = [1, 2, 3]
    print(Solution.subsets(aa))
