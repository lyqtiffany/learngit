from time import sleep

from selenium import webdriver


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()

    def test_prop(self):
        print(self.driver.name) #浏览器名称
        print(self.driver.current_url) #当前url
        print(self.driver.title) #当前页面标题
        print(self.driver.window_handles) #句柄，当前打开的窗口
        #print(self.driver.page_source) #html 源码

        self.driver.quit()

    def test_method(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.back() #返回，后退
        sleep(2)
        self.driver.refresh() #刷新
        sleep(2)
        self.driver.forward() #向前

        self.driver.close() #关闭当前tab
        self.driver.quit() #关闭浏览器


    def test_windows(self):
        self.driver.find_element_by_link_text('新闻').click()
        windows = self.driver.window_handles

        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                sleep(2)


if __name__ == '__main__':
    case = TestCase()
    #case.test_prop()
    #case.test_method()
    case.test_windows()




