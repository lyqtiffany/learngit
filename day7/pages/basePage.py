from day7.utils.mysettings import Timeout,PallFrequency
from day7.utils.mydriver import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self):
        self.driver=Driver.get_driver()
    def get_element(self,locator):
        WebDriverWait(
            #传入浏览器对象
            driver=self.driver,
            #传入超时时间
            timeout=Timeout,
            #传入轮循时间
            poll_frequency=PallFrequency
            ).until(
            # 检测定位元素是否存在
            EC.visibility_of_element_located(locator)
            )
        #返回元素对象,如果是元组就解包
        return self.driver.find_element(*locator)
    def get_elements(self,locator):
        WebDriverWait(
            #传入浏览器对象
            driver=self.driver,
            #传入超时时间
            timeout=Timeout,
            #传入轮循时间
            poll_frequency=PallFrequency
            ).until(
            # 检测定位元素是否存在
            EC.visibility_of_element_located(locator)
            )
        #返回元素对象,如果是列表就解包
        return self.driver.find_elements(*locator)
# if __name__ == '__main__':
#     BP=BasePage()