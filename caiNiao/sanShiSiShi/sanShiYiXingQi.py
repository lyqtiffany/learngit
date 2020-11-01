# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
#
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。

letter = input('please input a letter')

if letter == 'S':  #大小写有影响
    print('please input second letter: ')
    letterA = input('please input the second letter:')
    if letterA == 'a':
        print('Saturday')
    elif letterA == 'u':
        print('Sunday')
    else:
        print('data error')
elif letter == 'F':
    print('Friday')
elif letter == 'M':
    print('Monday')
elif letter == 'T':
    print('please input second letter')
    letterB = input('pleae input second letter')
    if letterB == 'u':
        print('Tuesday')
    elif letterB == 'h':
        print('Thursday')
    else:
        print('data error')
elif letter == 'W':
    print('Wednesday')
else:
    print('data error')