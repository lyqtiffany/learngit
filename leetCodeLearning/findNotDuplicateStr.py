#python算法：找出字符串中第一个不重复的字符
def first_char(str):
    dic = {}
    for i in range(len(str)):
        #累计字符的出现次数
        if str[i] in dic:
            dic[str[i]] += 1
        #只出现一次，key对应的value就记1次
        else:
            dic[str[i]] = 1
    for i in range(len(str)):
        if dic[str[i]] == 1:
            return str[i], i+1
        else:
            return ''
if __name__ == '__main__':
    str1 = ['a', 'b', 'c', 'd', 'a', 'b', 'c']
    print(first_char(str1))


'''在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:
s = "abaccdeff"
返回 "b"

s = "" 
返回 " "'''



'''初始化： 字典 (Python)、HashMap(Java)、map(C++)，记为 dic ；
字符统计： 遍历字符串 s 中的每个字符 c ；
若 dic 中 不包含 键(key) c ：则向 dic 中添加键值对 (c, True) ，代表字符 c 的数量为 1 ；
若 dic 中 包含 键(key) c ：则修改键 c 的键值对为 (c, False) ，代表字符 c 的数量 > 1>1 。
查找数量为 1 的字符： 遍历字符串 s 中的每个字符 c ；
若 dic中键 c 对应的值为 True ：，则返回 c 。
返回 ' ' ，代表字符串无数量为 11 的字符。

Python 代码中的 not c in dic 整体为一个布尔值； c in dic 为判断字典中是否含有键 c 。'''
# class Solution:
#     def firstUniqChar( s):
#         dic = {}
#         for c in s:
#             dic[c] = not c in dic
#         for c in s:
#             if dic[c]: return c
#         return ' '
# s = "abaccdeff "
# if __name__ == '__main__':
#     print(Solution.firstUniqChar(s))