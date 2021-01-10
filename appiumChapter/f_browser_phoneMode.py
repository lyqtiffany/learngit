#利用浏览器的手机模式打开页面

#app 上的web类型怎么定位元素？
#不能用appium来定位手机上的web,
# 可以在电脑浏览器上面打开网页，F12后，左上角切换成手机端
# 打开电脑上的浏览器，用手机模式运行

#电脑上模拟手机模式页面不会用到appium和手机没有关系
from selenium import webdriver

#创建chromeoptions对象，用于配置浏览器打开模式
chromesoptions = webdriver.ChromeOptions()
#添加手机模式，选择浏览器存在的设备
chromesoptions.add_experimental_option("mobileEmulation",{"deviceName":"iPhone X"})
#设备名称需要和浏览器的默认支持设备名字一样

driver = webdriver.Chrome(chrome_options=chromesoptions)

driver.get('http://www.baidu.com')

#设置浏览器的大小(分辨率)
driver.set_window_size(400,600) #设置宽度不会低于480

driver.find_element_by_id('index-kw').send_keys('selenium\n')
res = driver.find_element_by_css_selector('[class="c-title-text"]').text
print(res)

assert 'selenium' in res

driver.quit()#



