#键盘和鼠标的操作，
# webdriver同步执行javascript  用execute_script
#take screenshot,  save screenshot to dictionary

import os

from selenium import webdriver
from time import sleep, strftime, localtime, time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# http://sahitest.com/demo

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()


    def test_mouse(self):
        self.driver.maximize_window()
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        #导入actionChain类完成鼠标操作
        btn = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        ActionChains(self.driver).double_click(btn).perform()  #双击

        sleep(2)
        btn = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        ActionChains(self.driver).click(btn).perform()  #单击
        sleep(2)

        btn = self.driver.find_element_by_xpath('/html/body/form/input[4]')
        ActionChains(self.driver).context_click(btn).perform()  #右击，类似right click
        sleep(5)

    def test_keyboard(self):
        # 导入Keys类完成键盘操作
        self.driver.get('http://www.baidu.com')
        # kw = self.driver.find_element_by_id('kw')
        # kw.send_keys('selenium')
        # kw.send_keys(Keys.CONTROL,'a')
        # sleep(2)
        # kw.send_keys(Keys.CONTROL,'x')
        # sleep(2)
        # kw.send_keys(Keys.CONTROL,'v')
        # sleep(2)

        e = self.driver.find_element_by_link_text('新闻')
        ActionChains(self.driver).move_to_element(e).click(e).perform()
        sleep(2)

    def test1(self): #通过javascript
        self.driver.get('http://www.baidu.com')
        self.driver.execute_script("alert('test')") #通过javascript接收弹出框
        sleep(2)
        self.driver.switch_to.alert.accept()

    def test2(self):
        self.driver.get('http://www.baidu.com')
        js = 'return document.title'
        title = self.driver.execute_script(js)  #通过javascript返回页面标题
        print(title)

    def test3(self):
        self.driver.get('http://www.baidu.com')# 通过javascript修改搜索框样式
        js = 'var q = document.getElementById("kw"); q.style.border="2px solid red"'
        self.driver.execute_script(js)

    def test4(self):#通过javascript 让滚动条滚动到底部
        self.driver.get('http://www.baidu.com')  # 通过javascript修改搜索框样式
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js)
        sleep(2)

    def test_takeScreenshot(self):
        self.driver.get('http://www.baidu.com')  # selenium实现屏幕截图
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)

        # self.driver.save_screenshot('baidu.png')#会保存在当前目录
        # st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time)) #截图时间戳命名
        # file_name = st + '.png'
        # # self.driver.save_screenshot(file_name)

        st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time())) #截图时间戳命名
        file_name = st + '.png'
        path = os.path.abspath('../screenshot')
        file_path = path + '/' + file_name
        self.driver.get_screenshot_as_file(file_path)

    def test_frame(self): #切换到frame
        self.driver.get('http://sahitest.com/demo/framesTest.htm')
        self.driver.maximize_window()

        top = self.driver.find_element_by_name('top')# 定位到frame,进入frame
        self.driver.switch_to.frame(top)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[1]').click()

        self.driver.switch_to.default_content()  #跳出frame
        sleep(3)

        secondFrame = self.driver.find_element_by_xpath('/html/frameset/frame[2]')
        self.driver.switch_to.frame(secondFrame) #进入第二个frame
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[2]').click()

        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    # case.test_mouse()
    #case.test_keyboard()
    # case.test1()  #execute_script for javascript
    # case.test2()
    # case.test3()
    # case.test4()
    # case.test_takeScreenshot()
    case.test_frame()