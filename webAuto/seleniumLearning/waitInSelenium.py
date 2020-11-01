# 网络慢的时候，如果不做任何处理，代码会由于找不到元素而报错。另外如果页面使用到ajax异步加载机制，这时我们就要用到wait
#sleep适合调试时候使用，但是如果用到实际项目，如果网络好，依然等待就不合适了，项目里去掉所有sleep
#隐式等待，实际上是设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间结束，然后执行下一步。
#有个坑，javascript一般都是放在我们的body的最后进行加载，实际这时页面上的元素都已经加载完毕，我们却还在等待全部页面加载结束。
#隐式等待对整个driver周期都起作用，在最开始设置一次就可以了，不要当作固定等待来使用，到哪都来一下隐式等待。

#显式等待，webdriverwait是selenium提供得到显式等待模块引入路径，
#webdriverwait参数，driver实例, timeout等待的超时时间, poll_frequency(轮询默认0.5秒),ignored_execeptions忽略的异常
#方法until until -->method, message

import os

from selenium import webdriver
from time import sleep
from selenium.webdriver.support import  expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        # sleep(2)

    def test_sleep(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        # sleep(2) #线程阻塞，blocking wait
        self.driver.find_element_by_id('su').click()
        # sleep(3)
        self.driver.quit()

    def test_implicity(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        self.driver.quit()

    def test_wait(self):
        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.title_is('百度一下，你就知道')) #直到获取到百度title页面，才进行后续步骤
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_sleep()
    # case.test_implicity()
    case.test_wait()
