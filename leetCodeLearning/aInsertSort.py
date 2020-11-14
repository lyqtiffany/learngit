'''插入排序原理
1、构建有序序列
2、选择无序队列的第一个元素，先放在有序队列末尾，然后进行冒泡排序，放到指定的位置
3、循环2步，直到无序队列中所有元素全部进入有序队列的合适位置
特点：
插入vs冒泡：
插入排序的有序队列用到了冒泡算法，

区别：
升序情况下：
冒泡：有序队列在后，无序队列在前，
插入：有序队列在前，无序队列在后
# 插入和冒泡其时间复杂度:
# 最优时间复杂度: O(n²)
# 最坏时间复杂度: O(n²)

插入vs选择：
选择是遍历未排序队列，将最小的元素移动到有序队列的末尾
插入是把无序队列第一个元素放到有序队列，通过使用冒泡算法，移动到合适的位置'''

# 1、刚开始有序队列为空，直接把无序队列的第一个元素放到有序队列里即可
# 2、如果有序队列有内容，那么把无序队列的第一个元素放到有序队列最后面，然后有序队列进行冒泡排序
# 3、需要进行多少次冒泡排序呢？无序队列有几个元素，就进行n-1次有序队列的冒泡排序

# 5 3 1 2 7 6 #指定5
# 3 5 1 2 7 6 #3跟5对比， 3小于5， 3 插入到5前面去
# 1 3 5 2 7 6 # 1跟排好序的3 5 比较，1 插入到合适的位置

def insert_sort(alist):
    n = len(alist)
    for j in range(0, n): #选定一个未排序元素
        for i in range(j, 0, -1): #把新加入有序队列的元素和其他有序队列的元素冒泡排序
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            else:
                break
    return alist


if __name__ == '__main__':
    alist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    insert_sort(alist)
    print("排序后：", alist)