
#po模式，简单来说，就是page object
'''
页面对象
我们做ui自动化的时候，会遇到很多的页面
未来维护方便，我们可以将每个页面封装成一个class
融入了面向对象的思想
PO模式，每一页都要封装一个类，但是这样便于维护

'''

'''
staleElementReferenceException
陈旧的元素引用异常，
这个异常发生在获取元素赋值给变量，再通过变量操作元素，两个步骤之间，若产生了界面刷新
则会在通过变量操作元素的时候，抛出此异常
解决方法：
  每次操作元素前，实时获取元素，赋值给变量
  也就是说，若在获取元素复制给变量，与通过变量操作之间发生了页面刷新。
  那么在界面刷新后，元素操作前，重新获取元素

    def username_box(self):
        return self.driver.find_element_by_name('username')
        
'''

from selenium import webdriver



class loginPage:
    def __init__(self, url):
        #创建浏览器驱动对象
        self.driver = webdriver.Chrome()
        #访问网址
        self.driver.get(url)
        #用户名输入框
        self.username_input = self.driver.find_element_by_name('username')
        #密码输入框,#密码input标签,把type改成text,密码就会可见了
        self.password_input = self.driver.find_element_by_name('password')
        #登陆按钮
        self.login_button = self.driver.find_element_by_css_selector('button')

    def username_box(self):
        return self.driver.find_element_by_name('username')

    def password_box(self):
        return self.driver.find_element_by_name('password')

    def login_but(self):
        return self.driver.find_element_by_css_selector('button')

    def login(self):

        self.username_input.send_keys('libai')
        self.password_input.send_keys('opmsopms123')
        self.login_button.click()

        #解决方式：在获取元素赋值给变量，再通过变量操作元素，两个步骤之间，若产生了界面刷新
        self.driver.refresh()
        self.username_box().send_keys('libai')
        self.password_box().send_keys('opmsopms123')
        self.login_but().click()


LP = loginPage('http://127.0.0.1:8088/')
LP.login()




