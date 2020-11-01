from selenium.webdriver.common.by import By
from time import sleep
from webAuto.testcases.pom.pages.basePage import BasePage


class UserLoginPage(BasePage):
    username_input = (By.NAME, 'user')  # 定位器
    pwd_input = (By.NAME, 'pwd')
    register_btn = (By.CLASS_NAME, 'btn')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_login_page(self):
        self.driver.get('http://jpress.io/user/login')
        self.driver.maximize_window()

    def input_username(self, username):
        self.clear(*self.username_input)
        self.type_text(username, *self.username_input)

    def input_pwd(self, pwd):
        self.clear(*self.pwd_input)
        self.type_text(pwd, *self.pwd_input)

    def click_register_btn(self):
        self.click(*self.login_btn)
        sleep(2)




