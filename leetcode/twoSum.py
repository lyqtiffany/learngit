class Solution:  #hashmap
    def twoSum(self, num, target):
        mapping = {} # dictionary, 字典 #key=element, value= index
        for i in range(len(num)): #for 遍历一次，
            diff = target - num[i]
            if diff in mapping.keys(): #查询差值在mapping中吗？  # if diff in mapping:
                return [mapping[diff], i]   #差值和遍历值的下标
            else:
                mapping[num[i]] = i

    def twoSumb( self, num, target):  #暴力解法
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                if num[i] + num[j] == target and i != j:
                    return i, j


if __name__ == '__main__':
    num = [2, 71, 13, 7]
    print(Solution().twoSum(num, 9))
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([3, 3], 6))
    print(Solution().twoSumb(num, 9))
    print(Solution().twoSumb([3, 2, 4], 6))
    print(Solution().twoSumb([3, 3], 6))

# 数据结构
# 数组 array 1、268  78、90
# 链表 linkedlist 344/21  2/24
# 队列 queue 933、255   622、641
# 栈 stack 20、232   71、394
# 堆 heap  703/1046  215/692
# 哈希表 hashmap 217/389  49/560

# 算法
# 二分法 dinary search 704/35  74/162
# 双指针 two pointer 27/344/125   287
# 滑动窗口 sliding window  3/424
# 回溯法 backtracking 401  46/77/78
# 分治法divide conquer 53/169 215/240
# 广度优先搜索BFS 559/690  200/207
# 深度优先搜索 100、101   200、721
# 拓扑排序 topologic sort  207/210
# trie: 211/720 692/676
# 动态规划dynamic programming 70/121  5/91
