#basePage
#所有页面都能用到的
from seleniumChapter.f.basePageVersion.myDriver import Driver
from seleniumChapter.f.basePageVersion.settings import time_out, poll_time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    '''
    basepage是将一些页面通用的方法，抽离出来，封装起来
    '''
    def __init__(self):
        #获取浏览器驱动对象
        self.driver = Driver.get_driver("Chrome")

    def get_element(self, locator):
        '''
        #显式等待，查找元素,返回单个的元素对象
        :param locator: 要求传入的参数是一个元组，定位方式和定位表达式
        :return: 单个的元素对象
        '''

        WebDriverWait(
            driver=self.driver,
            timeout=time_out,
            poll_frequency=poll_time
        ).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        '''
        #显式等待，查找元素,返回单个的元素对象
        :param locator: 要求传入的参数是一个元组，定位方式和定位表达式
        :return: 单个的元素对象
        '''

        WebDriverWait(
            driver=self.driver,
            timeout=time_out,
            poll_frequency=poll_time
        ).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_elements(*locator) #*解包

    #BasePage类里面的get_elements找元素列表，until中不用写成EC.visibility_of_all_elements_located