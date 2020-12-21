#针对select里面下拉框的内容
from selenium.webdriver.support.select import Select
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Administrator/PycharmProjects/pythonLearnFrist/seleniumChapter/ddropdownl.html')

#定位到下拉框元素
ele = driver.find_element_by_id('abc')


#根据下拉框文本(标签对)里面的内容
Select(ele).select_by_visible_text('月薪三千')
#根据下标选择，下标是0开始
Select(ele).select_by_index(3)
#根据value属性选择,必须是option标签有value属性才行
Select(ele).select_by_value('p1')








