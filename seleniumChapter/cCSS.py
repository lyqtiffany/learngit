'''
推荐的元素定位优先级
优先级：ID > name > CSS selector > xpath

为什么优先选择css?
1.css是配合HTML工作的，css的实现原理是匹配对象。
xpath是配合xml工作的，xpath的实现原理是遍历
2.大部分人认为，css的语法更加简洁明了
3.前段开发主要用css,不适用xpath

css的语法是怎样的呢？
css的规则由两部分构成：选择器，以及1条或者多条声明
选择器用来匹配标签，匹配到标签以后，声明才起作用.主要找选择器
/*css中的id选择器用#来定义*/
 #abc {color: #0044bb}

 ：nth-child（1）是css的下标

 # css复合的写法，不用写.开头， 单写组合选择符必须前面有元素
 #driver.get('http://www.51job.com') #访问网址
 #job= driver.find_element_by_css_selector('div.j_joblist div.e')
 #直接从job处开始找
 #job_title = job.find_element_by_css_selector('span[class="jname at"]')
'''

import time
from selenium import webdriver


driver = webdriver.Chrome()
#右键html文件，copy，copy path,绝对路径，然后粘贴到浏览器访问，在浏览器拷贝地址
driver.get('file:///C:/Users/Administrator/PycharmProjects/pythonLearnFrist/seleniumChapter/ctest.html') #访问网址

ele = driver.find_element_by_css_selector('#abc') #id=abc的元素
print(ele.text)
