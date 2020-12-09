#网络爬虫
import re
import requests #加载requests 模块，需要安装后使用
import xlwt #加载excel的写入模块

url = 'https://www.xs4.cc/0_5/' #需要进行爬虫的网站
url2 = re.findall('https://www.xs4.cc/(.*?)/', url)[0]

req = requests.get(url) #打开需要爬虫的网站
req.encoding = 'gbk' #将编码转化为GBK,解决乱码问题
# print(req.text)

book_name = re.findall('<h1>(.*?)</h1>', req.text)[0] #获取书名
# <a href="/0_5/1899.html">第六十五章 红衣</a>

chapter = re.findall('html">(.*?)</a>', req.text) #获取目录
# for i in range(len(chapter)):
#     print(chapter[i])

#
chapter_url = re.findall(f'/{url2}/(.*?).html">', req.text)
# for i in range(9,len(chapter)):
#     print(chapter_url[i])


dict1 = {}
for i in range(9, len(chapter)):
    dict1[chapter[i]] = f'{url}{chapter_url[i]}.html' #将目录网址存放到字典

for k, v in dict1.items(): #打印目录和网址
    # print(k, v)
    if k == '第一章 惊蛰':
        req1 = requests.get(v)
        req1.encoding = 'gbk'
        chapter_content = re.findall(r'iv id="content">(.*?)</div>', req1.text,re.S)
        print(chapter_content)


#
# for childUrl in dict1.values():
#     print(childUrl)
#     req1 = requests.get(childUrl)
#     req1.encoding = 'gbk'
#     print(req1.text)
#     childContent = req1.text


#把查询结果里面的目录和每个章节网址放到excel
# excel1 = xlwt.Workbook() #实例化一个excel
# worksheet = excel1.add_sheet(f'{book_name}') #用书名作为sheet
#
# #第一行的第一列，第二列放标题和网址
# worksheet.write(0, 0, '目录') #行，列，值
# worksheet.write(0, 1, '网址') #行，列，值
#
# row = 1
# for k, v in dict1.items(): #遍历字典里面的键和值
#     worksheet.write(row, 0, k) #目录写入excel
#     worksheet.write(row, 1, v) #网址写入excel
#     row += 1
#
# excel1.save(f'd:/pythonCourse/{book_name}.xls')

#思考题，获取全书网，某一本书的所有正文，或者获取前5章

# re.findall('', XX, re.S) #换行
# %nsbp 去掉




