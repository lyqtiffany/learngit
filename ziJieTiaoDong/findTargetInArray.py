#讲思路在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序，给定一个目标数，判断是否在矩阵中。

# 先看target是不是大于第一行最右边的（最大值），
# 大于然后对比往下一行的最大值，
# 小于就跟当前一列的值往左对比。。

def find(target, array):
    i = 0
    j = len(array[0]) - 1

    while i < len(array) and j >= 0:
        base = array[i][j]
        if target == base:
            return True
        elif target > base:
            i += 1
        else:
            j -= 1
    return False


print(find(11212, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]))