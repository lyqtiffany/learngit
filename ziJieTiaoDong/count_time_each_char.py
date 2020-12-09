# 统计字符串字符出现个数
def count_each_char_1(string):
    res = {}
    for i in string:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    return res


print(count_each_char_1('aenabsascd'))

