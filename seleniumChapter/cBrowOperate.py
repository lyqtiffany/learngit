from selenium import webdriver
import time

driver = webdriver.Chrome() #一个driver,只有一个浏览器
driver.get("https://www.baidu.com/") #访问网址
driver.get("http://m.weibo.cn") #get没有打开浏览器的功能，只能控制浏览器访问网址

#webdriver提供了set_window_size控制浏览器大小
# driver.set_window_size(700, 700) #int类型的参数，控制宽和高,像素点
#
# #在PC端执行用例的时候，一般浏览器全屏
# driver.maximize_window() #自动匹配电脑的分辨率
# #最小化
# driver.minimize_window()


#控制浏览器的前进，后退，刷新
driver.back()#后退
time.sleep(1)
driver.forward()#前进
time.sleep(1)
driver.refresh() #刷新

driver.quit()


