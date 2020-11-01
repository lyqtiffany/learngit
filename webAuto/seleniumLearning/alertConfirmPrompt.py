'''
页面上的弹框有三种，alert提示，confirm用来确认，prompt输入内容
'''

# accept() 接受
# dismiss（） 取消
# text（） 显示的文本
# send_keys() 输入内容



import os

from selenium import webdriver
from time import sleep

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' +path + '/test_alert.html'
        self.driver.get(file_path)

    def test_alert(self):
        self.driver.find_element_by_id('alert').click()
        #切换到alert
        alert = self.driver.switch_to.alert  #需要switch_to method
        print(alert.text)
        sleep(3)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element_by_id('confirm').click()
        confirm = self.driver.switch_to.alert  # also use alert
        print(confirm.text)
        sleep(3)
        confirm.dismiss()
        #confirm.accept()

    def test_prompt(self):
        self.driver.find_element_by_id('prompt').click()
        sleep(2)
        prompt = self.driver.switch_to.alert  #also use switch to then    alert
        print(prompt.text)
        sleep(3)
        # prompt.dismiss()
        prompt.accept()
        sleep(3)

if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()
    case.driver.quit()






