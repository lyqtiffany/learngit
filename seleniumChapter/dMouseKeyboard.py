'''
1找后台开接口，直接获取哦验证码
2测试环境设置万能验证码
3.测试环境取消验证码的正确性识别，输入任何内容都通过
'''

#鼠标事件
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

ele = driver.find_element_by_css_selector('a[name="tj_briicon"]')
ActionChains(driver).move_to_element(ele).perform()
driver.find_element_by_css_selector('a[name="tj_wangpan"]').click()




'''#鼠标悬停到更多
#想要对某个元素进行鼠标操作，首先要定位到这个元素
# ele = driver.find_element_by_css_selector('a[name="tj_briicon"]')
#对定位到的元素执行鼠标悬停的操作
# ActionChains(driver).move_to_element(ele).perform()
#鼠标事件有个特殊之处，我们所调用的函数只是注册动作，不会执行
#如果想要执行，需要在之后加上perform函数

# ActionChains(driver).context_click(ele).perform() #右击
# ActionChains(driver).double_click(ele).perform() #双击
# ActionChains(driver).click(ele).perform()#单击
# ActionChains(driver).drag_and_drop(ele1, ele2).perform()#ele1拖到ele2

#点击藏在更多里面的网盘按钮，需要先悬停到更多
# driver.find_element_by_css_selector('a[name="tj_wangpan"]').click()'''


'''# 键盘事件
ele = driver.find_element_by_id('kw')
#输入内容
ele.send_keys('selenium')
#删除最后一个多余的n
ele.send_keys(Keys.BACKSPACE)
#输入一个空格，再输入教程
ele.send_keys(Keys.SPACE)
ele.send_keys('教程')

#全选输入框内容
ele.send_keys(Keys.CONTROL, "a")
#剪切
ele.send_keys(Keys.CONTROL, "x")
#粘贴剪切板里的内容
ele.send_keys(Keys.CONTROL, "v")'''



