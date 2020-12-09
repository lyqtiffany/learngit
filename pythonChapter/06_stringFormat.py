#格式化字符串

#格式化字符串，方案一， #%s表示字符串，%d表示整数
#格式化字符串，其实就是字符串的拼接，只不过更加简便

# a = 2
# b = 3
# print('%d+%d=%d' % (a, b, a+b)) #%s表示字符串的占位符
#
# info = 'I am %s, You are %s, this year is %d' % ('Bob', 'Jerry', 2020)
# print(info)

#前后参数不一致的情况
# #前面的参数比后面的多会报错not enough arguments for format string
#前面参数比后面的少也会报错，not all arguments converted during string formatting

# info1 = 'I am %s, You are %s, this year is %d ' % ( 'Bob', 'Jerry', 2020)
# print(info1)

#至少显示5位，不足5位补空格，在%后面写一个数字n，如果实参超出位数，实参也能显示完整
#给数字补0，而不是补空格，在%号的后面写一个0
# info2 = 'I am %5s, You are %7s, this year is %05d ' % ( 'BobABCD', 'Jerry', 2020)
# print(info2)

#改为左对齐,%号的后面写个-号，就能变成左对齐，默认情况全部是右对齐
# info3 = 'I am %-5s, You are %-7s, this year is %-5d ' % ( 'Bob', 'Jerry', 2020)
# print(info3)

#浮点型%f,默认显示6位小数， %n.mf，n表示最少n位，m表示保留m为小数
number1 = 'you number is %3.5f'%(3.6)#输出3.60000
number2 = 'you number is %6.1f'%(3.6) #前面补空格
# print(number1)


#方案二 .format,前面的参数比后面少，不会报错
# str6 = 'my name is {}, your name is {}, age is {}'.format('Apple', 'Winnie', 'Gary', 18)
# print(str6)

# #方案二 .format,前面的参数比后面多，会报错，IndexError: Replacement index 2 out of range for positional args tuple
# str7 = 'my name is {}, your name is {}, age is {}'.format('Apple', 18)
# print(str7)

#补齐到至少N位，在大括号里面加上:n,参数超过形参数量n，也可以正常显示
# str6 = 'my name is {:>5}, your name is {:5}, age is {:<5}'.format('Apple',  'Gary', 18)
# print(str6) #my name is Apple, your name is Gary , age is    18

#方案2中，字符串默认左对齐，数字默认右对齐，如果需要强制左对齐，加上<, 右对齐>,中间对齐用^

#{}里面不写东西，属于顺序填值，取值的顺序是固定的，也可以使用下标填值法，手动选择要填的顺序
# str7 =  'my name is {}, your name is {}, age is {}'.format('Apple','Bob', 18)
# print(str7) #my name is Apple, your name is Bob, age is 18

#下标填值法不能填一半，必须都填
# str8 = 'my name is {1}, your name is {0}, age is {2}'.format('Apple','Bob', 18)
# print(str8) #my name is Bob, your name is Apple, age is 18



#python3.6以后的版本中，可以使用f''写法
name1 = '上海'
name2 = '功能'
name3 = '点点点'
str7 = f'My name is {name1}, your name is {name2}, her name is {name3}'
print(str7)


info2 = 'I am %5s, You are %7s, this year is %06x ' % ( 'BobABCD', 'Jerry', 10)
print(info2)



#作业题目

'''1.程序开始的时候提示用户输入学生年龄信息 格式如下：

Jack Green ,   21  ;  Mike Mos, 9;

我们假设 用户输入 上面的信息，必定会遵守下面的规则：
  学生信息之间用分号隔开（分号前后可能有不定数量的空格），
  每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格）

2. 程序随后将输入的学生信息分行显示，格式如下
Jack Green :   21;
Mike Mos   :   09;
学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零

'''
testStr = 'Jack Green ,   21  ;  Mike Mos, 9; Mary Chen , 18;'

count = testStr.count(';')   #统计学生的人数
testStr = testStr.split(';')  #根据;区分每个学生对应的信息
for i in range(count):
    testStr[i] = testStr[i].split(',') #第一个 ['Jack Green ', '   21  ']  第二个 ['  Mike Mos', ' 9']

    testStr[i][0] = testStr[i][0].strip()
    testStr[i][1] = testStr[i][1].strip()
    output = '{:<20}:{:>2};'.format(testStr[i][0],  testStr[i][1])
    print(output)


#老师的参考答案，打印学生信息
inputStr = input('Please input student age info:')
studentInfo = inputStr.split(';')
for one in studentInfo:
    # check if it is valid input
    if ',' not in one:
        continue

    name, age = one.split(',')
    name = name.strip()
    age = age.strip()

    #  check is age digit
    if not age.isdigit():
        continue

    age = int(age)

    print('%-20s :  %02d' % (name, age))
    # print('{:<20} :  {:>02}'.format(name, age))
    # print(f'{name:<20} :  {age:>02}')