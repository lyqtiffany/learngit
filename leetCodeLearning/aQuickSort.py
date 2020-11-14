'''快速排序
步骤为：

从数列中挑出一个元素，称为"基准"（pivot），
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。虽然一直递归下去，但是这个算法总会结束，因为在每次的迭代（iteration）中，
它至少会把一个元素摆到它最后的位置去。
串联每一个基准值

时间复杂度:
最优时间复杂度：O(nlogn)
最坏时间复杂度：O(n2)
稳定性：不稳定

第一个基准值可以选择数组的最后一个数
'''


# def quick_sort(a_list, start, end):
#     """快速排序"""
#     if start >= end:
#         return
#     mid = a_list[start]  # 定义一个基准
#     left = start
#     right = end
#
#     while left < right:  # 如果left与right未重合, left就向中间(右)移动
#         while left < right and a_list[right] >= mid:
#             right -= 1
#         a_list[left] = a_list[right]  #如果比基准元素小，就跳出循环，并且把它放在基准元素左边
#         while left < right and a_list[left] < mid:
#             left += 1 #如果left和right 没有重合，left比基准元素小，就把左指针向右移动
#         a_list[right] = a_list[left] #如果比基准元素大，就跳出循环，并且放到基准元素的右边
#     a_list[left] = mid  # 从循环退出后, left与right相遇, 即 left==right
#     quick_sort(a_list, start, left - 1)  # 用递归对左边部分执行快速排序
#     quick_sort(a_list, left + 1, end)  # 用递归对右边部分执行快速排序
#
# if __name__ == '__main__':
#     li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#     print(li)
#     quick_sort(li, 0, len(li) - 1)
#     print(li)

def quick_sort(data):  #递归
    """quick_sort"""
    if len(data) >= 2:
        mid = data[len(data)//2]
        left,right = [], []
        data.remove(mid)
        for num in data:
            if num >= mid: #mid 77--
                right.append(num) #left 54 26 17 31 44 55 20--
            else:
                left.append(num)  # right 93,--
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data
a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(quick_sort(a))



