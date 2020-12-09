#文件的读取与写入

#读取文件
filepath = 'd:/note1.txt'
#'d:\note1.txt'
#方案一，改成 'd:/note1.txt'
#方案二，改成r'd:\note1.txt''
#方案三，改成 'd:\\note1.txt'

# file1 = open(filepath) #读取整个文件 file1 = open(filepath, 'r'),默认读取,可以省略r
# print(file1.read())  #读取文件内容
# file1.close()

#设置编码file--settings--file encodings
#另外可以把文件的utf-8格式改成ANSI格式

# file1 = open(filepath, 'a') #追加写入
# file1.write('欲穷千里目，更上一层楼。') #写入到文件中的内容
# file1.close() #使用open方法时，在语句结束时应该加上close方法，避免浪费内存

# file1 = open(filepath, 'w') #清空之前的内容，重新写入
# file1.write('危楼高百尺，手可摘星辰，不敢高声语，恐惊天上人。') #写入到文件中的内容
# file1.close() #使用open方法时，在语句结束时应该加上close方法，避免浪费内存

#同时读和写
file1 = open(filepath, 'w+')
#r+,可以同时读取与写入,如果文件不存在，则报错，写入时覆盖    #只改了第一句
#w+,可以同时读取与写入，如果文件不存在，会生成一个文件，写入时是清空写入   #清空原来的内容，只留下新的
#a+,可以同时读取与写入，如果文件不存在，会生成一个文件，写入时是追加写入   #接在后面写，不换行

# file1.write('曹操关羽张飞')
# file1.close()

filepath2 = 'd:/note2.txt'
# file2 = open(filepath2, 'w+')
# file2.write('file2测试')
# file2.seek(0) #将光标移动到文件首位
# print(file2.read()) #w+时，写入后，光标在最后，直接读取，是没有内容打印的
# file2.close()
#seek(参数1，参数2) 参数1用例控制光标偏移几位，参数2缺省为0，如果写1或者2，只能用于2进制模式
#参数2，0表示从文件开头开始计算  1 表示从光标的当前位置开始计算偏移值，2表示文件末尾开始计算
#read()读取整个文件的内容
#readlines()读取整个文件的内容，返回列表，每一行是一个元素，存到列表里面，打印出来
#readline() #一次读取一行，

#除了open之外，python可以使用with open
# with open(filepath2, 'w+') as file2:  #with open不需要close文件了
#     file2.write('起舞弄清影，何似在人间')
#     file2.seek(0)
#     print(file2.read())

#with open可以同时读写多个文件
# with open(filepath2, 'w+')as file2, open('d:/note3.txt','w+') as file3:
#     file2.write('note2')
#     file3.write('note3文件三')

#场景1，将1到100的数字写入文件
# with open(filepath2, 'w+') as file2:
#     for i in range(101):
#         if i == 100:
#             file2.write(str(i))
#         else:
#             file2.write(str(i)+',') #write()方法是传字符串,不能直接写入数字
#     file2.seek(0)
#     print(file2.read())


# #思考题：将九九乘法表写入到文件中
# # with open(filepath2, 'w+') as file2:
# #
# #     for i in range(10):
# #         j = 1
# #         while j <= i: #for j in range(1,i+1)
# #             file2.write('{}*{}={} '.format(j, i, i*j))
# #             j += 1
# #         file2.write('\n')
# #     file2.seek(0)
# #     print(file2.read())

#九九乘法表
# for i in range(1,10):
#     for j in range(1, i+1):
#         print(f'{j}*{i}={i*j}\t', end='') #加上end= ''，不会每次换行，会遍历完j的值再换行
#     print()

#用列表推导式写九九乘法表

#print('\n'.join(['\t'.join([f'{j}*{i}={i*j}\t' for j in range(1,i+1)]) for i in range(1,10)]))

print('传球给'.join('ABC'))





