from selenium import  webdriver
from time import sleep

#http://sahitest.com/demo/
from selenium.webdriver.remote.webelement import WebElement


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')

    def test_webelement_prop(self):
        e = self.driver.find_element_by_id('t1')
        e1 = WebElement
        print(type(e))
        print(e.id) #id是唯一的
        print(e.tag_name)  #名字input
        print(e.rect) #矩形框大小, 元素宽度高度 x y 坐标值
        print(e.size)#宽度高度
        print(e.text)

    def test_webelement_method(self):
        e = self.driver.find_element_by_id('t1')
        e.send_keys('hello world')
        sleep(2)


        print(e.get_attribute('type')) #text类型
        print(e.get_attribute('name'))
        print(e.get_attribute('value')) #取到文本内容hello world
        print(e.value_of_css_property('color')) #颜色

        sleep(2)
        e.clear()
    def test_method2(self):
        #form表单也有定位元素的方法
        form_element = self.driver.find_element_by_xpath('/html/body/form[1]')
        form_element.find_element_by_id('t1').send_keys('balabala')



if __name__ == '__main__':
    case = TestCase()
    #case.test_webelement_prop()
    # case.test_webelement_method()
    case.test_method2()
