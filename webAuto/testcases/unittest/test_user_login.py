from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui
from webAuto.util import util
import unittest
import pytest

#http://jpress.io/user/login

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://jpress.io/user/login')
        cls.driver.maximize_window()

    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://jpress.io/user/login')
    #     self.driver.maximize_window()


    def test_user_login_username_error(self):
        #用户名为空
        username = ''
        pwd = '12345'
        expected = '账号不能为空'

        self.driver.find_element_by_name('user').send_keys(username)#输入用户名
        self.driver.find_element_by_name('pwd').send_keys(pwd)#输入密码
        self.driver.find_element_by_xpath('/html/body/main/div/div/form/div[3]/button').click() #点击登陆
        sleep(2)

        #等待提示框
        WebDriverWait(self.driver, 5).until(EC.alert_is_present()) #验证弹框出现
        alert = self.driver.switch_to.alert

        sleep(3)
        #验证 self.assertEqual(alert.text, expected)
        assert alert.text == expected
        print(alert.text)
        alert.accept()

        # self.driver.quit()

    def test_user_login_ok(self):
        username = 'lyqtiffany'
        pwd = 'lyq1994811'
        expected = '用户中心'

        self.driver.find_element_by_name('user').send_keys(username)#输入用户名
        self.driver.find_element_by_name('pwd').send_keys(pwd)#输入密码
        self.driver.find_element_by_xpath('/html/body/main/div/div/form/div[3]/button').click() #点击登陆

        WebDriverWait(self.driver, 5).until(EC.title_is(expected)) #验证浏览器标题是用户中心
        sleep(3)

        assert self.driver.title == expected

        self.driver.quit()

if __name__ == '__main__': #unittest,在此处执行用例
    unittest.main()

