#找出数组中第二大的数
class Solution:
    def findSecondValue(self, numList):
        n = len(numList)
        if n == 0:
            return 0
        max_num = numList[0]
        sec_num = 0
        for i in range(n):
            if numList[i] > max_num:
                sec_num = max_num
                max_num = numList[i]
            elif numList[i] > sec_num and numList[i] != max_num:
                sec_num = numList[i]
        #print('second number is:', sec_num)
        return sec_num
aa = [100, 99, 22, 2, 1]
Solution().findSecondValue(aa)







# find max number in list
list1 = [10, 20, 4, 45, 99]
list1.sort() #排序后，最后一位是最大数
print("最大元素为:", list1[-1])

#用max 或者sort方法
list1 = [10, 20, 1, 45, 99]
print("最大元素为:", max(list1))






















