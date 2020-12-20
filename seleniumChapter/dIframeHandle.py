#iframe处理
#handle 打开其他网页标签

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()



#handle
driver.get("http://www.baidu.com")
ele = driver.find_element_by_css_selector('a[name="tj_briicon"]') #更多
ActionChains(driver).move_to_element(ele).perform()
driver.find_element_by_css_selector('a[name="tj_wangpan"]').click() #网盘
driver.maximize_window()

#获取当前所有的标签页的句柄,#句柄，就是操作系统中的唯一资源标识符
#句柄（Handle）是一个是用来标识对象或者项目的标识符，可以用来描述窗体、文件等，值得注意的是句柄不能是常量
all_handles = driver.window_handles #driver的属性，结果返回一个列表
for handle in all_handles:
    driver.switch_to.window(handle)
    if driver.title == '百度网盘，让美好永远陪伴':
        break

#在新打开的百度网盘的用户名输入内容
driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys('123')
time.sleep(1)
driver.quit()


# #iframe相关
# driver.get("file:///C:/Users/Administrator/PycharmProjects/pythonLearnFrist/seleniumChapter/dFrame.html")
# ifa = driver.find_element_by_css_selector('iframe:nth-child(3)') #为什么是3, css直接数标签数量，但是不是非得是iframe类型才计数
# #切入到iframe, 酒楼的包间
# driver.switch_to.frame(ifa)
# driver.find_element_by_id('kw').send_keys('林黛玉')
# #一下子切回到主页面
# driver.switch_to.default_content()


