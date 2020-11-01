#string字符串

s = "  hello   M world  " #空格也算入计数
print('s[0] ', s[0]) #字符串切片
print('s[-1]  ', s[-1])
print('s[:] ', s[:])
print('s[0:4] ', s[0:4])


print('len(s): ', len(s))
#s.max()
print('max(s) ', max(s))
#s.min()
print('min(s) ', min(s)) #?no result

print('s.count("l")', s.count('l')) #找有几个l,区分大小写
print('s.isupper()',s.isupper())#是不是都是大写字母
print('s.islower()  ', s.islower()) #是不是都是小写字母
print('s.isdigit()  ', s.isdigit()) #是不是都是数字
print('s.upper()  ', s.upper()) #转化为大写
print('s.lower()  ', s.lower())#转化为小写
print('s.strip()  ', s.strip()) #去掉前后空格
print('s.lstrip()  ', s.lstrip()) #去掉左边空格
print('s.rstrip()  ', s.rstrip()) #去掉右边空格
print('s.rstrip()  ', s.swapcase()) #把原来的大写转化成小写，小写的转化成大写
#replace(old, new)
print('s.replace("l  to E" )' , s.replace("l", "E")) #替换某个字母
print('s.split(' ')',s.split(' ')) #用空格分隔，返回list  ['', '', 'hello', '', '', 'M', 'world', '', '']

