from selenium import webdriver
from seleniumChapter.f.basePageVersion.settings import driverPath, url, username, password

class Driver:
    """
    任何地方需要用到浏览器驱动对象，直接调用此类下的get_driver方法，获取返回值即可
    且get_driver保证了我们的driver唯一
    """
    #初始化为空
    driver = None #类成员是唯一的，实例类后的成员是不唯一的

    @classmethod
    def get_driver(cls, browser_name): #保证只有一个driver，(单例模式)
        #如果cls.driver 为none, 则证明不存在，进入If代码块
        #如果cls.driver 不为none，则证明存在，不需要进入if代码块创建，可以直接返回
        if cls.driver is None:
            if browser_name == "Chrome":
                cls.driver = webdriver.Chrome(driverPath["Chrome"])
            elif browser_name == "Firefox":
                cls.driver = webdriver.Chrome(driverPath["Firefox"])

            # 访问默认的网址
            cls.driver.get(url)
            #最大化窗口
            cls.driver.maximize_window()
            cls.login()
        return cls.driver

    @classmethod
    def login(cls):
        cls.driver.find_element_by_name("username").send_keys(username)
        cls.driver.find_element_by_name("password").send_keys(password)
        cls.driver.find_element_by_css_selector("button").click()

if __name__ == '__main__':
    Driver.get_driver("Chrome")