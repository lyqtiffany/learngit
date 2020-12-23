# po模式，简单来说，就是page object

from selenium import webdriver
from seleniumChapter.f.firstPOVersion.myDriver import Driver
from seleniumChapter.f.firstPOVersion.settings import username,password


class LoginPage:
    def __init__(self):
        # 创建浏览器驱动对象,打开浏览器
        self.driver = Driver.get_driver("Chrome")


    def username_box(self):
        return self.driver.find_element_by_name('username')

    def password_box(self):
        return self.driver.find_element_by_name('password')

    def login_but(self):
        return self.driver.find_element_by_css_selector('button')


class LoginPageAction(LoginPage):
    '''
    我们一般会将页面当中一些常用的动作，会重复使用的动作。
    抽离出来，写成一个个的函数，封装在一个页面动作类中
    页面动作类，继承对应的页面类
    '''
    def login(self):
        self.driver.refresh()
        self.username_box().send_keys(username)
        self.password_box().send_keys(password)
        self.login_but().click()

'''
将页面分为页面元素类和页面动作类
若以后，只是逻辑修改了，只需要改动作类即可
若是元素定位发生了变化 ，只需要修改页面元素类即可

'''


if __name__ == '__main__':
    lp = LoginPageAction()
    lp.login()




