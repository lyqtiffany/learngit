#合并两个数组
#思路3. 从大遍历到小，直接操作num1，这个比较喜欢。

#解释一下：两个数组合并后一定使得nums1有效部分变成m+n的长度（这个视角下问题就简单了），那么就比较两个数组的尾巴，
# 谁大谁就被放在n+m-1的位置上，被放的那个数组的当前指针往前挪一个，直到其中一个数组被遍历光，如果nums2还有剩余，就将剩下的全放在nums1的最前面。

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n >0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m = m -1
            else :
                nums1[m+n-1] = nums2[n-1]
                n = n-1
        if n > 0 :
            nums1[:n] = nums2[:n]


#简单粗暴，先合并再排序
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:m + n] = nums2[:n]
        nums1.sort()