#文件上传
'''
对于通过input 实现的文件上传，我们可以将其看作是一个输入框，
即通过send_keys的方式，即可实现文件上传

对于非input标签实现的上传功能，我们可以通过模拟键盘敲击的方式去实现
'''

import time
from selenium import webdriver
import win32com.client #需要pip install pywin32
# pip --no-cache-dir install pypiwin32 --ignore-installed


driver = webdriver.Chrome()

#对于通过input 实现的文件上传，我们可以将其看作是一个输入框，
# 即通过send_keys的方式，即可实现文件上传
driver.get('https://tinypng.com/')
# #定位到文件上传的input标签
# ele = driver.find_element_by_css_selector('input[type="file"]')
# ele.send_keys('C:\\Users\\Administrator\\PycharmProjects\\pythonLearnFrist\\seleniumChapter\\dele.png')
#


#对于非input标签实现的上传功能
# 我们通过模拟键盘敲击的功能来实现
driver.find_element_by_css_selector("figure.icon").click()
time.sleep(3)

#模拟键盘敲击，会不管不顾的敲击，只要代码运行到这里，就敲击
#声明shell对象
sh = win32com.client.Dispatch("WScript.shell")
sh.Sendkeys("C:\\Users\Administrator\PycharmProjects\pythonLearnFrist\seleniumChapter\dele.png\r\n") #文件末尾加\n,代表回车键

#注意代码运行过程，不要去操作鼠标，输入法保持英文

#注意，keys类，是针对input标签来操作的，此处不能用Keys类



