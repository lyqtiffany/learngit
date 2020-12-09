# 方法其实就是函数，只b不过它是由对象的实例调用的
str1 = 'abc'
# isdigit()是字符串str1这个对象的方法
str1.isdigit()  # 判断字符串是不是纯数字
str1.isalpha()  # 判断字符串是不是纯字母

str2 = '  are you ok ?   '
# print(str2.strip()) #不写参数的情况下，默认去掉字符串前后的空格
str2_1 = '*******test*****'
# print(str2_1.strip('*')) #把test前后的*去掉

# replace方法，替换指定的字符串,replace是全部替换，不是只替换一个
# print(str2.replace(' ', '')) #replace参数1是指需要被替换的值，参数2是替换后的值

# startswith, 判断字符串是否以某个或某些字符开头
# 判断某个身份证是否是南京的身份证
# id_card = '320104199909090909'
# if id_card.startswith('3201'):
#     print('南京的身份证')
#
# #endswith,判断身份证的最后一位是不是X
# if id_card.endswith('X'):
#     print('最后一位是X')
# else:
#     print('最后一位不是X')

#split()方法，分割字符串，以参数作为切割符，之后，切割符会消失，分割之后的返回值是列表
a = 'ABCDQCH'
# print(a.split('C')) #输出['AB', 'DQ', 'H']


#思考题，判断某个身份证号码的主人的性别,倒数第二位，偶数是女，奇数是男
id_card = '431127199901016714'
if int(id_card[-2]) % 2 == 0:
    print("female")
else:
    print('male')

