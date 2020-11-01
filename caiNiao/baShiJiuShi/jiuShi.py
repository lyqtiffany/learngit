#90 题目：列表使用实例。

# list
# 新建列表
testList = [10086, '中国移动', [1, 2, 4, 5]]
print('length of testList is ',len(testList))  # 访问列表长度 3
print('testList[1:]下标1到列表结尾', testList[1:]) # 下标1到列表结尾
testList.append('i\'m new here!') # 向列表添加元素
print('# 向列表添加元素', len(testList), testList)
print('testList[-1]',testList[-1] )
print('弹出列表的最后一个元素',testList.pop(1)) # 弹出列表的下标为1的元素
print(len(testList))

print(testList)

# list comprehension
# 后面有介绍，暂时掠过
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix)
print(matrix[1])
col2 = [row[1] for row in matrix]  # get a  column from a matrix
print(col2)
col2even = [row[1] for row in matrix if row[1] % 2 == 0]  # filter odd item
print('   h',col2even)
