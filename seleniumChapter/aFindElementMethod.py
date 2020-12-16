from selenium import webdriver

#创建浏览器驱动对象，这里是打开浏览器
#如果driver路径添加到了环境变量，就不用写driver路径了。
driver = webdriver.Chrome()
#访问网址
driver.get('file:///C:/Users/Administrator/PycharmProjects/pythonLearnFrist/seleniumChapter/test.html')

#根据ID属性进行定位
ele = driver.find_element_by_id('abc')
#获取元素的文本值，并打印出来
print(ele.text)

'''#根据name属性定位
ele = driver.find_element_by_name('abd')
print(ele.text)'''

'''#根据链接文本进行定位
ele = driver.find_element_by_link_text('点击进入百度')#完全匹配
ele.click()'''

'''#根据标签tag_name进行定位
ele = driver.find_element_by_tag_name('span')
print(ele.text)'''

'''#根据链接文本进行定位,模糊定位
ele = driver.find_element_by_partial_link_text('点击进入')#部分匹配
ele.click()'''

'''#根据class属性进行定位,只返回找到的第一个元素，如果要找多个，需要find_elements
ele = driver.find_element_by_class_name('xyz') #多个class属性html有空格隔开,但是定位只用其中一个
print(ele.text)'''

#根据xpath进行元素定位,xpath从1 开始
ele = driver.find_element_by_xpath('/html/body/div/ul/li[2]') #元素的路径
print(ele.text)

#根据css表达式进行定位
ele = driver.find_element_by_css_selector('html > body > div>ul>li:nth-child(2)')
print(ele.text)

driver.quit()


