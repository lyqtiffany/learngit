from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui
from webAuto.util import util
import unittest
import pytest


#http://jpress.io/user/register
class TestUserRegister(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://jpress.io/user/register')
        self.driver.maximize_window()

    login_data = [
        ('test001', 'test001@qq.com', '123456', '123456', '666', '验证码不正确'),
        ('test001', 'test007@qq.com', '123456', '123456', '111', '注册成功，点击确定进行登录。'),
    ]


    @pytest.mark.parametrize('username, email, pwd, confirmPwd, captcha, expected', login_data)
    def test1_register(self, username, email, pwd, confirmPwd, captcha, expected):
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)

        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(email)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)

        if captcha != '666':
            captcha = util.get_code(self.driver, 'captchaimg')

        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_xpath('/html/body/main/div/div/form/div[7]/button').click()
        sleep(2)

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())  # 最长等待5秒，超出即超时
        alert = self.driver.switch_to.alert
        print(alert)
        sleep(2)

        assert alert.text == expected
        alert.accept()
        sleep(5)


if __name__ == '__main__':
    pytest.main(['test_user_register.py'])


# class TestUserRegister(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.driver = webdriver.Chrome()
#         cls.driver.get('http://jpress.io/user/register')
#         cls.driver.maximize_window()

#     #测试登陆验证码错误
#     def test_register_01code_error(self):
#         username = 'test001'
#         email = 'test001@qq.com'
#         pwd = '123456'
#         confirmPwd = '123456'
#         captcha = '666'
#         expected = '您还未同意本站注册条款，不能注册。'
#
#         self.driver.find_element_by_name('username').send_keys(username)
#         self.driver.find_element_by_name('email').send_keys(email)
#
#         self.driver.find_element_by_name('pwd').send_keys(pwd)
#         self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
#
#         self.driver.find_element_by_name('captcha').send_keys(captcha)
#         self.driver.find_element_by_xpath('/html/body/main/div/div/form/div[7]/button').click()
#         sleep(2)
#
#         WebDriverWait(self.driver,5).until(EC.alert_is_present()) #最长等待5秒，超出即超时
#         alert = self.driver.switch_to.alert
#         print(alert)
#         sleep(2)
#
#         #python的断言
#         # assert alert.text == expected
#
#         #修改成Unittest的断言
#         self.assertEqual(alert.text, expected)
#
#         alert.accept()
#
#         sleep(5)
#         # self.driver.quit()
#
#     def test_register_02pass(self): #
#         username = util.gen_random_str()
#         email = username + '@qq.com'
#         pwd = '123456'
#         confirmPwd = '123456'
#
#         #自动获取
#         captcha = ''
#         expected = '注册成功，点击确定进行登录。'
#
#         # 输入用户名
#         self.driver.find_element_by_name('username').clear()
#         self.driver.find_element_by_name('username').send_keys(username)
#         self.driver.find_element_by_name('email').clear()
#         self.driver.find_element_by_name('email').send_keys(email)
#
#         self.driver.find_element_by_name('pwd').clear()
#         self.driver.find_element_by_name('pwd').send_keys(pwd)
#         self.driver.find_element_by_name('confirmPwd').clear()
#         self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
#
#         captcha = util.get_code(self.driver, 'captchaimg') #自动识别验证码
#         self.driver.find_element_by_name('captcha').clear()
#         self.driver.find_element_by_name('captcha').send_keys(captcha) #输入验证码
#
#         elem = self.driver.find_element_by_id('agree')  # 同意协议的button只能通过xy 坐标点击，需要安装导入pytest
#         print(elem.rect)
#         rect = elem.rect
#         sleep(1)
#         pyautogui.moveTo(rect['x'] + 10, rect['y'] + 130)  # pyautogui.click(rect['x']+10, rect['y']+130) 也可以
#         pyautogui.click()
#
#         #点击注册
#         self.driver.find_element_by_xpath('/html/body/main/div/div/form/div[7]/button').click()
#         sleep(2)
#
#         WebDriverWait(self.driver,5).until(EC.alert_is_present()) #最长等待5秒，超出即超时
#         alert = self.driver.switch_to.alert
#         print(alert)
#
#         #python的断言
#         assert alert.text == expected
#         sleep(2)
#         alert.accept()
#
# if __name__ == '__main__':
#     unittest.main()