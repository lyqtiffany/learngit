from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, *loc):
        return self.driver.find_element(*loc)

    def type_text(self, text, *loc): #多参的情况要让多参在最后面
        self.get_element(*loc).send_keys(text)

    def click(self, *loc):
        self.driver.find_element(*loc).click()

    def get_title(self):
        return self.driver.title

class BaiduPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        driver.get('http://www.baidu.com')

    def test_search(self):
        loc = (By.ID, 'kw')
        loc2 = (By.ID, 'su')
        self.type_text('selenium', *loc) #多参数要放到后面
        self.click(*loc2)

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    baiduPage = BaiduPage(driver)
    baiduPage.test_search()