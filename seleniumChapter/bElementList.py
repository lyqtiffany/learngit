from selenium import webdriver

#创建浏览器驱动对象，这里是打开浏览器
#如果driver路径添加到了环境变量，就不用写driver路径了。
driver = webdriver.Chrome()
#访问网址
driver.get('file:///C:/Users/Administrator/PycharmProjects/pythonLearnFrist/seleniumChapter/test.html')

'''#匹配元素列表，返回所有能匹配到的元素，存在一个列表里面
eleLi = driver.find_elements_by_class_name('xyz')
#获取元素的文本值，并打印出来
for ele in eleLi:
    print(ele.text)'''

#class属性有复合类,可以任意取里面的一个单词，用作class的匹配查找，但是结果可能不唯一
#如果要找到唯一定位，最好在F12里面ctrl F,输入匹配规则，只出现一个匹配结果
# #class属性中间的空格是间隔符号，表示这个元素有多个class属性


driver.quit()

# http://vip.ytesting.com/q.do?a&id=ff808081703da3a4017041c7a6ea00e3
