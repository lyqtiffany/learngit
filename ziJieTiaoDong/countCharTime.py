str = 'abaaacasddddfdf'
#找出字符串中出现指定次数的字符
def countCharTime(str, n):
    for s in str:
        if str.count(s) == n:
            return s

#找出字符串中首个达到指定次数的字符
def countCharTimeB(str, n):
    for s in str:
        if str.count(s) == n:
            return s
        break
    return s

print(countCharTime('aaabbbccdwef', 2))
print(countCharTimeB('aaabbbccdwef', 2))