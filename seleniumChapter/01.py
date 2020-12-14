#什么是自动化测试？
# 简单来说，就是用代码模仿手工操作

#不是所有项目都时候做UI自动化

#UI自动化测试有哪些需要注意的？
 # 1.UI的文件
 # 2.交互逻辑的正确性
 # 3.UI上用户行为的正确性（不做逆向，异常场景测试）

#UI自动化难点
#对比手工测试：
 # 1，UI自动化难以发现非预期的bug
 # 2,UI的复杂多变带来巨大的成本
 # 3,UI的测试用例，多是关于用户交互方面的，

#什么是selenium?
 #web测试工具，运行在浏览器当中，像真正的用户在手工操作一样
 #支持主流的浏览器，其功能包括：
  #1.测试浏览器的兼容性，
  #2，创建回归测试

#什么是webdriver?
 #对浏览器提供的原生API进行封装，用这套API可以操作浏览器

 #selenium是python的一个库，我们写selenium代码，也是在写python代码
 #python代码不能直接操作浏览器，但是可以操作webdriver
 #webdriver可以操作浏览器，所以，我们间接地可以，用Python操作浏览器

#<br>换行，空元素，开始标签后面没有结束标签

#UI自动化操作流程
  #选择界面元素
    #根据元素的特征进行选择：ID, Name, Class, TagName
    #根据元素的特征及关系：css,xpath
  #操作界面元素
    #输入操作：点击，输入文字，拖拽元素
    #输出操作，获取元素的各种属性

#元素定位注意事项
 #1，当你想要操作某个确定的元素的时候，一定保持自己的表达式唯一定位
 #2，需要操作一组元素的时候，必须保持自己的表达式:
   #a.能匹配到所有想要操作的元素
   #b.并且不会匹配到任何其他不想操作的元素

#selenium没有给我们提供判断元素是否存在的方法，所以我们可以用匹配元素列表的方式判断。
#先根据表达式匹配元素列表，然后判断列表是否为空。
#如果列表为空，表示元素不存在。元素不为空，则元素存在





from selenium import webdriver

#创建浏览器驱动对象，这里是打开浏览器
#如果driver路径添加到了环境变量，就不用写driver路径了。
driver = webdriver.Chrome()
#访问网址
driver.get('http://www.baidu.com')

#找到文本输入框
# driver.find_element_by_id('kw').send_keys('test selenium')
ele = driver.find_element_by_id('kw')
ele.send_keys('test selenium')

#找到百度一下按钮
ele = driver.find_element_by_id('su')
ele.click()

driver.quit()