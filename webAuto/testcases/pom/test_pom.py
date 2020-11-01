from selenium import webdriver
import unittest  #Alt+Enter导入包
from time import sleep

from selenium.webdriver.common.by import By


class BaiduPage(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.input_element = (By.ID, 'kw')
        self.btn_element = (By.ID, 'su')

    def goto_baidu(self, url):
        self.driver.get(url)

    def test_search(self, url, kw):
        self.goto_baidu(url)
        self.driver.find_element(*self.input_element).send_keys(kw)
        self.driver.find_element(*self.btn_element).click()
        sleep(4)

class TestBaidu(unittest.TestCase):

    # def setup(self) -> None:
    #     self.baiduPage = BaiduPage()

    def test_search1(self):
        self.baiduPage = BaiduPage()
        self.baiduPage.test_search('http://www.baidu.com', 'selenium')

if __name__ == '__main__':
    unittest.main()

