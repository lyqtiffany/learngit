from selenium import webdriver
from time import sleep

# from .chrome.webdriver import WebDriver as Chrome #
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.maximize_window()
# sleep(1)
#
# element = driver.find_element_by_id('kw')
# element.send_keys('selenium')
# print(type(element))
# #<class 'selenium.webdriver.remote.webelement.WebElement'>
#
# driver.find_element_by_id('su').click()
# sleep(3)
# driver.quit()
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome() # from .chrome.webdriver import WebDriver as Chrome #
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()

    def test_id(self):
        #find_element_by_id返回结果是唯一的
        element = self.driver.find_element_by_id('kw')
        element.send_keys('selenium')
        print(type(element))

        self.driver.find_element_by_id('su').click()
        sleep(3)
        #self.driver.quit()

    def test_name(self):
        #find_element_by_name 可能返回多个元素,默认返回第一个
        #find_elements_by_name 返回一个集合
        self.driver.find_element_by_name('wd').send_keys('selenium2')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_linktext(self):
        self.test_id()
        self.driver.find_element_by_link_text('百度首页').click()
        sleep(3)

    def test_partial_link_text(self):
        self.test_id()
        self.driver.find_element_by_partial_link_text('首页').click()
        sleep(3)

    def test_xpath(self):
        #F12识别元素后，直接选中元素行右键，copy--copy xpath,粘贴到xpath下
        #//是相对路径,需要再了解下xpath的具体语法
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('极客时间')
        self.driver.find_element_by_id('su').click()
        sleep(3)

    def test_tag(self):
        input = self.driver.find_element_by_tag_name('input')[0] #list下标0
        print(input)

    def test_css_selector(self):
        #课后补充，识别元素后右键，copy copy selector
        self.driver.find_element_by_css_selector('#kw').send_keys('极客时间')
        self.driver.find_element_by_id('su').click()
        sleep(3)

    def test_class_name(self):
        self.driver.find_element_by_class_name('s_ipt').send_keys('test')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_all(self):
        self.driver.find_element(By.ID, value='kw').send_keys('400')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    #case.test_id()
    #case.test_name()
    #case.test_linktext()
    #case.test_partial_link_text()
    #case.test_xpath()
    #case.test_tag()
    # case.test_css_selector()
    # case.test_class_name()
    case.test_all()
