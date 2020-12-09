#pycharm使用技巧

#settings->editor->file and code templates, 悬着python script
#举例，输入#${NAME}表示新建文件时生成一行注释，记录当前文件名
#输入#${DATE}表示记录当前日期

#自动补齐
#如果要快速输入if __name__ == '__main__':语句，先输入main,然后按tab

#一般函数都可以用Tab键补齐

#自动补齐段落
#settings->editor->live templates,在页面右侧点击加号，新增自定义的内容
#之后在下发填写内容，并选择python

#改函数的颜色
#setts-->editor->color scheme->python-》function definition

#取消语法检查，或者用右下角小侦探图标，左右移动
#setts-->editor->inspection->python 去掉勾号

#设置分屏
#file->settings->keymap->search split

#常见的快捷键
#先输入Main，再输入CTRL + J,然后回车
#shift + 回车--》快速跳转到下一行
#ctrl+/, 快速注释、取消注释
#快速缩进4个空格,tab,取消缩进shift+tab

#编码问题
# settings-editor-file encoding- GBK/UTF-8切换

import json #加载json模块
data1 = '''{
"a":"Apple",
"b":"Cat"
}'''
# json一般有3引号，常用单引号，本质的类型是字符串
# print(type(data1)) #<class 'str'>
# #将json格式转为字典
# data2 = json.loads(data1) #loads方法将字符串转化为字典
# print(data2['a'])

# #字典转为字符串
# data3=json.dumps(data2) #dumps方法将变量中的字典转换为json格式字符串
# print(type(data3))

#load方法，读取文件，将文件中的json格式字符串转换为字典

# with open('d:/json3.txt') as file1:
#     data2 = json.load(file1) #从文件中将json格式字符串转换为字典
#     print(type(data2))

#dump方法，将字典转化为json格式并写入到文件中
# with open('d:/json3_2.txt', 'w+') as file2:
#     json.dump(data2, file2)






#冒泡排序
list1 = [12, 600, 33, -1, 9, 87, 106] #7个数，需要比6次
#两两比较，将较大的数往后排, 内层循环，将当前最大的数沉底，外层循环，决定比较次数
for i in range(len(list1)):  #第一次找出了最大的数
    for j in range(len(list1)-1-i): #每一轮可以少比一次 #-i可以不写
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
# print(list1)

#列表有自带排序
list1.sort(reverse=True) #列表永久排序，先排序再翻转
print(list1)
print(sorted(list1))#列表临时排序
print(list1[::-1])#翻转



