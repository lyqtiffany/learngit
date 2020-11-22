#分支语句

#input读取用户的输入，返回字符串类型
# score = int(input('please input score, then press Enter'))
#
# #分支语句在任何情况下，只会执行其中一个分支
# if score >= 90:
#     print('优秀')
# elif score >= 80:
#     print('良好')
# elif score >= 60:
#     print('及格')
# else:
#     print('不及格')


# if-if-if 与if-elif-elif的区别，多个if之间没有互斥性，所以使用分支语句时，要用if-elif

# if True and True:
#     print('hello')

# if 1: #0不打印，''不打印，None不打印，[]不打印，False不打印
#     print('hi') #if语句中的语句，必须要缩进，默认缩进4个空格，至少1个空格

#分支语句的嵌套
#如果一个人的年龄大于等于60，并且为男性，称他老先生
# age = 60
# gender = 'male'
# if age >=60 and gender == 'male':
#     print('old gentleman')

# if age >= 60:
#     if gender == 'male':
#         print('old gentleman')



#需求，用户输入手机号，移动(130-150)，联通(151-170)，电信(171-199)
#输入位数不对，提示用户位数错误
#输入非数字，提示有非法字符，

phoneNumber = input('please input a phone number')
if len(phoneNumber) == 11:
    if phoneNumber.isdigit():
        num = int(phoneNumber[0:3])
        if 130 <= num <= 150:
            print('移动号码:', phoneNumber)
        elif 151 <= num <= 170:
            print('联通号码:', phoneNumber)
        elif 171 <= num <= 199:
            print('电信号码:', phoneNumber)
        else:
            print('电话号码不属于三大运营商: ', phoneNumber)
    else:
        print('only numeric character allowed')
else:
    print('please input the phone number for 11 digits')



