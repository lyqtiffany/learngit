#实现一个  免登陆的 po框架
from selenium import webdriver
from seleniumChapter.f.basePageVersion.settings import driverPath, url

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
            cls.remove_login()

        return cls.driver

    @classmethod
    def remove_login(cls):
        pass
        cookieSli = [{'domain': '127.0.0.1',
                      'httpOnly': False,
                      'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436',
                      'path': '/',
                      'secure': False,
                      'value': '1608555856'},
                     {'domain': '127.0.0.1',
                      # 'expiry': 1640091856,
                      'httpOnly': False,
                      'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436',
                      'path': '/',
                      'secure': False,
                      'value': '1608555856'},
                     {'domain': '127.0.0.1',
                      # 'expiry': 1640091852,
                      'httpOnly': True,
                      'name': 'beegosessionID',
                      'path': '/',
                      'secure': False,
                      'value': '139e3b8514aa1808a6dd414b3df811e2'}]
        cls.driver.delete_all_cookies()

        for cookie in cookieSli:
            # 添加cookie
            cls.driver.add_cookie(cookie)  # 一次添加一个cookie
        cls.driver.refresh()


if __name__ == '__main__':
    Driver.get_driver("Chrome")