'''
@author: haiwen
@date: 2021/3/5
@file: bussiness.py
'''
from selenium import webdriver

from pylibs.webui.common import BasePage
from pylibs.plugins.config import read_yml
from conf.env import host
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        #进入登录页面
        self.driver.get(host)
    #     # 静态赋值
    #     # self.email_input = self.locators['email_input']
    #     # self.psw_input = self.locators['psw_input']
    #     # self.login_btn = self.locators['login_btn']
    #     # setattr(self,'email_input','locatorsxxxx')
    # def to_login_page(self):
    #     self.driver.get(host)
    #     return self  # 返回登录页面

    def login(self,email,psw):
        # 输入邮箱
        self.input_text(self.email_input,'tester44@test.com')
        # 输入密码
        self.input_text(self.psw_input, 'devops')
        # 点击登录
        self.click(self.login_btn)
        return HomePage()

#主页
class HomePage(BasePage):
    #到日程界面
    def to_schedule_page(self):
        #操作进入日程界面
        self.click(self.schedule_btn)
        return SchedulePage()  #返回日程页面

#日程页面
class SchedulePage(BasePage):
    def new_schedule(self,summary,target_user):
        #点击新建
        self.click(self.new_btn)
        #填写日程名称
        self.input_text(self.summary_input,summary)
        pass


if __name__ == '__main__':
    pass
