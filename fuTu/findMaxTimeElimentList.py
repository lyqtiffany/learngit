#python 返回一个列表中出现次数最多的元素

def max_list(lt):
    temp = 0
    for i in lt:
        if lt.count(i) > temp:
            max_str = i
            temp = lt.count(i)
    return max_str


n = [1, 2, 2, 2, 3, 3, 3, 3, 4]
m = 'asdfddgfgsdaaaaa'
print(max_list(n))
print(max_list(m))