from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui
from webAuto.util import util

#http://jpress.io/admin/login
import unittest

class TestAdminLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://jpress.io/admin/login')
        cls.driver.maximize_window()

    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://jpress.io/admin/login')
    #     self.driver.maximize_window()

    #测试登陆管理员时，验证码错误
    def test_admin_login_username_error(self):
        #验证码错误
        username = 'lyqtiffany'
        pwd = 'lyq1994811'
        captcha = '2345'
        expected = '验证码不正确，请重新输入'

        self.driver.find_element_by_name('user').send_keys(username)#输入用户名
        self.driver.find_element_by_name('pwd').send_keys(pwd)#输入密码
        self.driver.find_element_by_name('captcha').send_keys(captcha)  # 输入验证码
        self.driver.find_element_by_xpath('//*[@id="form"]/div[4]/div/button').click() #点击登陆
        sleep(2)

        #等待提示框
        WebDriverWait(self.driver, 5).until(EC.alert_is_present()) #验证弹框出现
        alert = self.driver.switch_to.alert

        sleep(3)
        #验证
        assert alert.text == expected
        print(alert.text)
        alert.accept()

        self.driver.quit()

    def test_admin_login_ok(self):
        username = 'lyqtiffany'
        pwd = 'lyq1994811'
        expected = 'JPress后台'

        self.driver.find_element_by_name('user').send_keys(username)#输入用户名
        self.driver.find_element_by_name('pwd').send_keys(pwd)#输入密码
        captcha = util.get_code(self.driver, 'captchaImg')
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_xpath('//*[@id="form"]/div[4]/div/button').click() #点击登陆

        WebDriverWait(self.driver, 5).until(EC.title_is(expected)) #验证浏览器标题是用户中心
        sleep(3)

        assert self.driver.title == expected #验证当前页面的标题

        self.driver.quit()


