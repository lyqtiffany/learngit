
list = ['1', '3', '34', '33', '4', '45'] #返回454343331
tmp = 0
str = ''
for i in range(len(list)): #for i in range(len(list))
    for j in range(len(list)-i-1): #for j in range(len(list)-i-1,len(list)-1)
        if list[j]+list[j+1] < list[j+1]+list[j]: ##list[j]+list[j+1]把列表里面字符串的数字拼接成数字
            # print(list[j]+list[j+1])
            list[j], list[j+1] = list[j+1], list[j]

for i in range(len(list)):
    str = str + list[i]  #把排序后（由大到小）的列表，拼接成字符串

print(str)

# listA = ['5', '5', '6']
# print((listA[0] + listA[2]), (listA[2]+listA[0])) #56 65
# print((listA[0] + listA[2]) > (listA[2]+listA[0])) #False

str([1,3])
