from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from webAuto.testcases.pom.ddt.pages.userRegisterPage import UserRegisterPage
from time import sleep
from webAuto.util import util
import pytest

class TestUserRegister(object):

    login_data = [
        ('test001', 'test001@qq.com', '123456', '123456', '666', '验证码不正确')
    ]

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.registerPage = UserRegisterPage(self.driver)
        self.registerPage.goto_register_page()

    @pytest.mark.parametrize('username, email, pwd, confirmPwd, captcha, expected', login_data)
    def test1_register(self, username, email, pwd, confirmPwd, captcha, expected):

        self.registerPage.input_username(username)
        self.registerPage.input_email(email)
        self.registerPage.input_pwd(pwd)
        self.registerPage.input_confirmPwd(confirmPwd)

        if captcha != '666':
            captcha = util.get_code(self.driver, 'captchaimg')
        self.registerPage.input_captcha(captcha)
        self.registerPage.click_register_btn()
        sleep(2)

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())  # 最长等待5秒，超出即超时
        alert = self.driver.switch_to.alert
        print(alert)
        sleep(2)

        assert alert.text == expected
        alert.accept()
        sleep(5)

if __name__ == '__main__':
    pytest.main(['-sv','testUserRegister.py'])