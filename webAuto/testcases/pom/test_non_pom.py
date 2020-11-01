from selenium import webdriver
import unittest
from time import sleep

class TestBaidu(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None: #ctrl + O 引入setup, teardown
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_baidu(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(5)

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()

if __name__ == 'main':
    unittest.main()