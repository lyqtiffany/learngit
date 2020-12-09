import re
import requests
import os

url = 'https://www.xs4.cc/0_5/' #需要进行爬虫的网站
url2 = re.findall('https://www.xs4.cc/(.*?)/', url)[0] #提取书名网址的最后一段
req = requests.get(url)
req.encoding = 'gbk'
book_name = re.findall('<h1>(.*?)</h1>', req.text)[0]
chapter = re.findall('html">(.*?)</a>', req.text) #获取目录
chapter_url = re.findall(f'/{url2}/(.*?).html">', req.text)
dict1 = {}
for i in range(9, len(chapter)):
    dict1[chapter[i]] = f'{url}{chapter_url[i]}.html'

if os.path.exists(f'd:/pythonCourse/{book_name}'): #如果目录存在，不创建文件夹
    pass
else:
    os.mkdir(f'd:/pythonCourse/{book_name}')

count = 0
for k, v in dict1.items():
    if count >= 3: #去掉if, 爬虫整本书
        break
    else:
        content = requests.get(v) #网址里再获取内容
        content.encoding = 'gbk'
        contentGet = re.findall('<div id="content">(.*?)</div>', content.text, re.S)[0]
        contentGet = contentGet.replace('&nbsp;', '').replace('<br />', '')
        with open(f'd:/pythonCourse/{book_name}/{k}.txt', 'w+') as file1:
            file1.write(contentGet)
        count += 1

