from selenium import webdriver
import unittest  #Alt+Enter导入包
from time import sleep

from selenium.webdriver.common.by import By
from webAuto.testcases.pom.pages.basePage import BasePage

class SearchPage(BasePage):
    search_input = (By.ID, u'kw')
    search_btn = (By.ID, u'su')

    def __init__(self):
        BasePage.__init__(self, driver)
        self.driver.maximize_window()

    def goto_baidu_home(self):
        self.driver.get('http://www.baidu.com')

    def input_kw(self):
        self.type_text('selenium', *self.search_input)

    def click_search_btn(self):
        self.click(*self.search_input)
        sleep(2)

class TestBaidu(unittest.TestCase):

    # def setup(self) -> None:
    #     self.baiduPage = BaiduPage()

    def test_search1(self):
        self.baiduPage = BaiduPage()
        self.baiduPage.test_search('http://www.baidu.com', 'selenium')

if __name__ == '__main__':
    unittest.main()

