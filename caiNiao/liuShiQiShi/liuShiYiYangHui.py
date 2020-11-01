#61 难点 题目：打印出杨辉三角形（要求打印出10行如下图）。　

# if __name__ == '__main__':
#     from sys import stdout
#     a =[]
#     for i in range(10):
#         a.append([])
#         for j in range(10):
#             a[i].append(0)
#     for i in range(10):
#         a[i][0] = 1
#         a[i][i] = 1
#     for i in range(2,10):
#         for j in range(1,i):
#             a[i][j] = a[i-1][j-1] + a[i-1][j]
#     for i in range(10):
#         for j in range(i +1):
#             stdout.write(str(a[i][j]))
#             stdout.write(' ')
#         print()


# n = 10
# list1 = []
# for n in range(n):
#     row = [1]
#     list1.append(row)
#
#     if n == 0:
#         for num in row:  #为输出的格式做处理
#             print(num, end=' ')
#             print()
#         continue
#     for m in range(1, n):
#         row.append(list1[n-1][m-1] + list1[n-1][m])
#     row.append(1)
#
#     for num in row:
#         print(num, end=' ')
#     print()

def generate(numRows):
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        a = [[1], [1, 1]]
        for i in range(2, numRows):
            c = []
            c.append(1)
            for j in range(1, i):
                c.append(a[i - 1][j - 1] + a[i - 1][j])
            c.append(1)
            a.append(c)

        return a

print(generate(10))
