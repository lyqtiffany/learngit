from day7XinBao.utils.mysettings import URL,password,username
# from day7.utils.mysettings import driverpath, URL,password,username
from selenium import webdriver


class Driver:
    _driver=None
    @classmethod
    def get_driver(cls,browser_name="chrome"):
        if cls._driver is None:
            if browser_name=="chrome":
                # cls._driver=webdriver.Chrome(driverpath[browser_name])
                cls._driver = webdriver.Chrome()
            elif browser_name=="Firefox":
                # cls._driver=webdriver.Firefox(driverpath[browser_name])
                pass
            else:

                print(f"未配置此{browser_name}浏览器驱动")
                return
            #隐式等待10秒
            cls._driver.implicitly_wait(10)
            #最大化窗口
            cls._driver.maximize_window()
            #启动浏览器
            cls._driver.get(URL)
            #执行登录操作
            cls.__login()
        return cls._driver
    @classmethod
    def __login(cls):
        cls._driver.find_element_by_name("username").send_keys(username)
        cls._driver.find_element_by_name("password").send_keys(password)
        cls._driver.find_element_by_css_selector("button").click()
        cookieSli = [{'domain': '127.0.0.1',
                      'httpOnly': False,
                      'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436',
                      'path': '/',
                      'secure': False,
                      'value': '1605619212'},
                     {'domain': '127.0.0.1',
                      # 'expiry': 1637155211,
                      'httpOnly': False,
                      'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436',
                      'path': '/',
                      'secure': False,
                      'value': '1605619212'},
                     {'domain': '127.0.0.1',
                      # 'expiry': 1637155211,
                      'httpOnly': True,
                      'name': 'beegosessionID',
                      'path': '/',
                      'secure': False,
                      'value': 'bc6fb7bc29eafc3f64479b7e53ec2e9c'}]
        cls._driver.delete_all_cookies()
        for cookie in cookieSli:
            cls._driver.add_cookie(cookie)
        cls._driver.refresh()
if __name__ == '__main__':
    driver=Driver.get_driver()
