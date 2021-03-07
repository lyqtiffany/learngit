'''
@author: haiwen
@date: 2021/1/20
@file: common.py
'''
from selenium import webdriver

#页面的基类 --封装公共操作
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from pylib.plugins.config import read_yaml, current_time
from pylib.plugins.tools import Single


class BasePage:
    def __init__(self):
        #如何实现只打开一次浏览器
        self._driver = WebDriverCreater().get_driver()

        #1配置文件读取元素定位方式
        conf = read_yaml('conf/locators.yml')
        #2当前类（当前页面）的名称
        # current_class = self.__class__.__name__

        # 获取当前页面和父类的元素定位方式
        classnames = [ancestor.__name__ for ancestor in self.__class__.mro()][:-2]  #排除BasePage 和object
        for classname in classnames:
            self.locators = conf[classname]  #当前页面的元素定位方式
            # 3批量赋值--动态赋值
            for key in self.locators:
                self.__setattr__(key, self.locators[key])


    #常用操作-点击？
    def click(self,locator):
        # self.driver.find_element(locator[0],locator[1])
        self._driver.find_element(*locator).click()  #locator是列表 第一个元素是定位方式，第二个元素是具体的表达式

    #输入操作--1.输入框定位方式   2 文本
    def input_text(self,locator,text):
        #locator是列表类型，如果是元组类型无法解包
        self._driver.find_element(*locator).send_keys(text)

    # 点击多个元素
    def click_multi(self,locators):
        eles = self._driver.find_elements(*locators)  #获取多个目标元素然后挨个点击
        for ele in eles:
            ele.click()

    # 根据目标特征选择元素
    def selecte_target(self,target,locators):
        # 获取多个目标元素 再一堆目标元素根据特征寻找目标
        eles = self._driver.find_elements(*locators)
        for ele in eles:
            # 根据元素文本进行选择
            if ele.text == target:
                ele.click()
                break

    def eles_text(self,locators):  #返回多个元素的文本
        eles = self._driver.find_elements(*locators)
        return [ele.text for ele in eles]

    def close_browser(self):
        self._driver.quit()  # 仅关闭浏览器 退出chromedriver
        self._driver = None  #置空driver对象，方便下次初始化页面打开浏览器

    def auto_screen(self, func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except WebDriverException as e:
                print(e)
                filename = current_time('%Y_%m_%dT%H_%M_%S')
                self._driver.save_screenshot(filename + '.png')
                raise e
        return inner

    #定义一个专门工具类生成唯一浏览器
class WebDriverCreater(Single):
    #要求该方法不管调用多少次，都只返回一个实例（对象）
    def get_driver(self):
        #判断当前对象是否创建了driver,创建了直接返回
        if hasattr(self,'driver'):
            return self.driver
        # 没有创建就新建一个返回
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        #配置页面加载超时时间
        self.driver.set_page_load_timeout(60)
        self.driver.set_script_timeout(60)  # js执行超时时间
        return self.driver


basePage=BasePage()