#正则表达式
#正则表达式，其实就是从一段字符串中提取出需要的字符串
#re.findall #无论有多少返回值，都是列表
#re.findall(参数1，参数2) #参数1表示用什么规则进行提取，参数2表示从哪里提取
#第三个参数，re.I, re.S
import re #加载正则表达式模块
str1 = 'abcadebf'

# .表示匹配某个字符后面的任意一个字符
# print(re.findall('ab.', str1)) #结果是列表 #['abc']
#如果只想显示.代表的字符，怎么办？ . 的外面加括号
# print(re.findall('ab(.)', str1)) #['c']

#  * 匹配0个或多个的表达式。 表示匹配某个字符后面的若干个字符  0到多个，也包括0个
# print(re.findall('ab*', str1)) #匹配a后面有若干个b #str1 = 'abcadebf'   ['ab', 'a']
# print(re.findall('a(b*)', str1))  #括号表示匹配a后面有若干个b, 匹配到的内容['b', '']

# ? 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式 表示匹配某个字符后面有0个或者1个字符,最多匹配一个
# print(re.findall('ab?', str1)) #匹配a后面有0个或者1个b   str1 = 'abbcadebf'  ['ab', 'a']

# + 匹配1个或多个的表达式。表示a后面有若干个b,不包括0个的情况
# print(re.findall('ab+', str1))  #匹配a后面有1个或者多个b  str1 = 'abcadebf'  ['ab']


#.*? #提取两端之间的内容
# print(re.findall('a(.*?)e', str1))  #str1 = 'abcadebf'  ['bcad']
# print(re.findall('a.*?e', str1))  #str1 = 'abcadebf' ['abcade']
str2 = '我欲乘风归去，又恐琼楼玉宇，高处不胜寒'
#如果提取条件，只写前面的一端，会提取出什么？懒惰匹配 实际上是不取任何值
# print(re.findall('又恐(.*?)', str2))   #懒惰匹配，尽量少的匹配， ['']
# print(re.findall('又恐(.*)', str2))   #谈论匹配，尽量多的匹配，['琼楼玉宇，高处不胜寒']
#
# print(re.findall('又恐(.*?)，', str2))   #因为后面一个字符已经确定，无法懒惰 #['琼楼玉宇']
# print(re.findall('又恐(.*)，', str2))  #因为后面一个字符已经确定，只能到，的位置 #['琼楼玉宇']


# \w{n} #匹配字母，数字，下划线，n表示连续多少位
str3 = 'ybr&nb%yt_qty043545y'
# print(re.findall('\w', str3)) #['y', 'b', 'r', 'n', 'b', 'y', 't', '_', 'q', 't', 'y', '0', '4', '3', '5', '4', '5', 'y']
# print(re.findall('\w{6}', str3)) #['yt_qty', '043545']
# print(re.findall('\w{3}', str3)) #['ybr', 'yt_', 'qty', '043', '545']

#\W{n}匹配字母，数字，下划线以外的值
# print(re.findall('\W{1}', str3)) #['&', '%']

#\s 匹配字符串，以及\t制表符，以及\n换行符
str6 = '''空  山不见人
但闻人语    响
返景入  深林
复照青苔  上'''
# print(re.findall('\s', str6))  #[' ', ' ', '\n', ' ', ' ', ' ', ' ', '\n', ' ', ' ', '\n', ' ', ' ']

#\S 匹配空字符串，或者\t制表符以外的值，\n换行符以外的值
# print(re.findall('\S', str6)) #['空', '山', '不', '见', '人', '但', '闻', '人', '语', '响', '返', '景', '入', '深', '林', '复', '照', '青', '苔', '上']

#\d 匹配数字
str7 = '23hy69kjmj'
# print(re.findall('\d', str7)) #['2', '3', '6', '9']
# print(re.findall('\d{2}', str7)) #['23', '69']

#\D 匹配数字以外的值
# print(re.findall('\D', str7)) #['h', 'y', 'k', 'j', 'm', 'j']

#^匹配开头，$匹配结尾
# list1 = ['abcde', 'dfabc', 'eabcg']
# for one in list1:
#     if re.findall('^abc', one):
#         print(one, '以abc开头')
#     elif re.findall('abc$', one):
#         print(one, '以abc结尾')
#abcde 以abc开头
# dfabc 以abc结尾


#re.I, 不区分大小写
str9 = 'ABCabcABC'
# print(re.findall('abc', str9)) #['abc']
# print(re.findall('abc', str9, re.I)) #['ABC', 'abc', 'ABC']

#re.S, 允许换行 匹配多行中符合条件的值
a = '''hellogervdc
sdffworld'''

# print(re.findall('hello(.*?)world', a, re.S)) #['gervdc\nsdff']
# print(re.findall('hello(.*?)world', a)) #[]

str1 = '<html>a="asfsdf"</html>'
print(re.findall('<html>a="(.*)"', str1))
# A: <html>a=”（.+？）”</html> 正常匹配出a里面的字符
# B. <html>a=”（.+）”</html> 正常匹配出a里面的字符
# C. <html>a=”（.*？）”</html> 正常匹配出a里面的字符
# D. <html>a=”（.*）”正常匹配出a里面的字符