# 选择排序(selection sort):
# 选择排序算法如下:
# 首先在未排序序列中找到最小(大)元素, 存放到排序序列的起始位置
# 然后再从剩余未排序元素中继续寻找最小(大)元素,放到已排序列的末尾
# 以此类推
# 其时间复杂度:
# 最优时间复杂度: O(n²)
# 最坏时间复杂度: O(n²)
# 选择排序稳定性: 不稳定( 考虑升序每次选择最大的情况 )


def select_sort(a_list):
    """选择排序"""
    n = len(a_list)
    for j in range(n - 1): #第一次选择列表的第一个元素
        min_index = j
        for i in range(j + 1, n): #选择当前元素之后的最小值
            if a_list[i] < a_list[min_index]:
                min_index = i
        if j != min_index: #如果最小值的索引跟当前选择元素的索引不一致，就把最小值和当前值替换
            a_list[j], a_list[min_index] = a_list[min_index], a_list[j]


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('排序前:%s' % li)
    select_sort(li)
    print('排序后:%s' % li)

