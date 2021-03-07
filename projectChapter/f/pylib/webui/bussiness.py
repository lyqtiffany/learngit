'''
@author: haiwen
@date: 2021/1/20
@file: bussiness.py
'''
import time

from pylib.webui.common import BasePage
from conf.env import host

#公共区域_导航
class HeadLinePage(BasePage):
    def logout(self):
        #点击头像
        self.click(self.avatar)
        #点击退出
        self.click(self.logout_btn)
        #退出成功后--进入登录页
        return LoginPage()


    def to_schedule_page(self):
        self.click(self.schedule_link)
        #接下来干嘛？--进入日程界面
        return SchedulePage()

class LoginPage(BasePage):
    # def __init__(self):
    #     super().__init__()
    #     self.email_input = self.locators['email_input']  #取值 付给对象属性
    #     self.psw_input = self.locators['psw_input']
    #     #当前页面的元素定位方式？
    #     self.__setattr__('email_input',self.locators['email_input'])  #动态赋值参数1：属性名称,2:属性值
    def __init__(self):
        super().__init__()
        self._driver.get(host) #初始化默认访问进入登录页

    def login(self,email,password):
        #输入邮箱和密码
        self.input_text(self.email_input, email)
        self.input_text(self.psw_input, password)
        #点击确定
        self.click(['css selector','.MuiButton-containedPrimary'])
        return MainPage()  #登录成功后返回主页面对象


class MainPage(HeadLinePage):
    def get_title(self):
        return '主页标题'

    def list_schedules(self):
        return self.eles_text(self.schedules)

from pylib.webui.common import basePage
#日程界面
class SchedulePage(HeadLinePage):
    @basePage.auto_screen
    def new_schedule(self,summary,target_user):
        #新建日程
        self.click(self.new_btn)
        # 填写主题
        self.input_text(self.summary_input,summary)
        # 点击用户选择
        self.click(self.user_select)
        #time.sleep(2)  # 稳定页面
        # 选择人员.....
        #1.先取消选择
        self.click_multi(self.selected_users)
        #2. 根据用户名选择
        self.selecte_target(target_user,self.selectUser_box)
        #点击确认
        self.click(self.confirm_btn)
        #点击保存
        self.click(self.save_btn)

        #返回页面对象自身
        return self






if __name__ == '__main__':
    LoginPage().login('testuser43@test.com','123456').to_schedule_page().new_schedule('收个菜','小张').logout().login('xiaozhang@test.com','123456')  #链式调用
