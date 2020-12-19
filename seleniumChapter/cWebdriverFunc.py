from selenium import webdriver
import time

driver = webdriver.Chrome() #一个driver,只有一个浏览器
driver.get("https://www.baidu.com/") #访问网址

'''
1.点击，输入，
我们定位元素对象之后要去操作元素，比如单击，输入文字
click方法提供元素点击操作
send_keys方法模拟按键文本输入，要求被操作元素是文本框
clear提供分本框内容清空的功能
2.其他方法：
size获取元素尺寸
text获取元素标签对之间的内容,(子孙后代元素标签对里面的内容，也可以获取到)
get_attribute 获取元素属性值
is_displayed #检查元素是否可见
'''

# driver.find_element_by_id("kw").send_keys('test tf') #send_keys方法模拟按键文本输入
# time.sleep(1)
# driver.find_element_by_id("kw").clear() #clear提供分本框内容清空的功能
# time.sleep(1)
# driver.find_element_by_id("kw").send_keys('selenium')
# driver.find_element_by_id("su").click()# click方法提供元素点击操作
#
# driver.quit()

# ele = driver.find_element_by_id("kw")
# print(ele.size) #打印元素尺寸
# print(ele.text) #打印元素文本
# print(ele.get_attribute("class")) #打印元素的class属性
# print(ele.is_displayed()) #检查元素是否可见

# driver.quit()
