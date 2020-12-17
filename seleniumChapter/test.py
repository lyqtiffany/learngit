import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.vmall.com/') #访问网址
driver.maximize_window()
'''
定位//ol[@class="category-list"]，网页上只匹配到一个元素，
但是遍历find_elements_by_xpath('//ol[@class="category-list"]')的结果，依然可以打印出所有的一级菜单，是为什么呢？
#为什么一级菜单，不定位到li,也能打印出一级菜单？
'''
category = driver.find_elements_by_xpath('//ol[@class="category-list"]')
for first_Cate in category:
    #获取每个大类的标题，比如手机，笔记本，平板等
    print(f"一级菜单： {first_Cate.text}")  #打印一级菜单的内容