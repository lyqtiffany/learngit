'''
@author: haiwen
@date: 2021/3/5
@file: common.py
'''
from selenium import webdriver

#定义公共功能
from selenium.webdriver.remote.webelement import WebElement

from pylibs.plugins.config import read_yml
from pylibs.plugins.demo import Single


#BasePage定义一些和业务无关的基础操作
class BasePage():
    def __init__(self):
        super().__init__() # 手动调用父类初始化
        # 方式1：从外面传入driver对象，
        # 方式2：采用单例模式
        self.driver = WebdriverCreater().get_browser()
        # 根据当前page类名读取元素定位
        current_cls = self.__class__.__name__
        self.locators = read_yml('conf/locators.yml')[current_cls]
        # 初始化提前准备好待操作的元素定位
        # 取元素定位
        # 动态赋值  setattr(对象, 属性名, 属性值)
        for key, value in self.locators.items():
            setattr(self, key, value)

    #1. 点击
    def click(self,locator):  #locator =['id','kw']
        # 如果传入的参数是元素对象
        # if type(locator) == WebElement:
        #     locator.click()
        ele = self.driver.find_element(*locator)
        ele.click()

    #2. 输入
    def input_text(self,locator,text):  # 假设locator =['xpath','kw']
        ele = self.driver.find_element(*locator)
        ele.send_keys(text)

    #3. 其他
#确保这个对象的唯一
class WebdriverCreater(Single):
    #该方法的对象是单例模式
    def get_browser(self):
        #先判断当前对象有没有driver属性,
        if hasattr(self,'driver'):
            # 有就直接返回
            return self.driver
        #没有 创建一个再返回
        self.driver = webdriver.Chrome()
        #隐士等待
        self.driver.implicitly_wait(10)
        return self.driver