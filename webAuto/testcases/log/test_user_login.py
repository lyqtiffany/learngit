from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui
from webAuto.util import util
import pytest


#http://jpress.io/user/login

class TestUserLogin(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://jpress.io/user/login')
        self.driver.maximize_window()
        self.logger = util.get_logger()
        self.logger.info('测试用户登录')

    def test_user_login_username_error(self):
        #用户名为空
        username = ''
        pwd = '12345'
        expected = '账号不能为空'

        self.driver.find_element_by_name('user').send_keys(username)#输入用户名
        self.logger.debug('输入用户名： %s', username)
        self.driver.find_element_by_name('pwd').send_keys(pwd)#输入密码
        self.logger.debug('输入密码： %s', pwd)
        self.driver.find_element_by_xpath('/html/body/main/div/div/form/div[3]/button').click() #点击登陆
        self.logger.debug('点击登陆')
        sleep(2)

        #等待提示框
        WebDriverWait(self.driver, 5).until(EC.alert_is_present()) #验证弹框出现
        alert = self.driver.switch_to.alert

        sleep(3)
        #验证
        try:
            assert alert.text == expected
        except AssertionError as ae:
            self.logger.error("tryA catch exception: %s", "报错了", exc_info=1)
        print(alert.text)
        alert.accept()

        # self.driver.quit()

    def test_user_login_ok(self):
        username = 'lyqtiffany'
        pwd = 'lyq1994811'
        expected = '用户中心'


        self.driver.find_element_by_name('user').send_keys(username)#输入用户名
        self.logger.debug('输入用户名： %s', username)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)#输入密码
        self.logger.debug('输入密码： %s', pwd)
        self.driver.find_element_by_xpath('/html/body/main/div/div/form/div[3]/button').click() #点击登陆
        self.logger.debug('点击登陆')

        WebDriverWait(self.driver, 5).until(EC.title_is(expected)) #验证浏览器标题是用户中心
        sleep(3)

        try:
            assert self.driver.title == expected + "dd"
        except AssertionError as ae:
            self.logger.error("报错 %s", "登录", exc_info=1)

        self.driver.quit()
if __name__ == '__main__':
    pytest.main(['test_user_login.py'])

