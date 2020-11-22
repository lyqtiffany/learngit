''' 下载selenium webdriver
https://www.selenium.dev/documentation/en/selenium_installation/installing_webdriver_binaries/
chrome webdriver download
https://chromedriver.storage.googleapis.com/index.html
'''

# from selenium import  webdriver
# from time import sleep
#
# def test1():
#
#     driver = webdriver.Chrome()
#     driver.get('https://www.baidu.com/')
#     driver.maximize_window()
#     driver.find_element_by_id("kw").send_keys("test tif")
#     driver.find_element_by_id("su").click()
#
#     sleep(3)
#     driver.quit()
#
# class TestCase(object):
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#
#     def test(self):
#         self.driver.get('https://www.baidu.com/')
#         self.driver.maximize_window()
#         self.driver.find_element_by_id("kw").send_keys("test tif")
#         self.driver.find_element_by_id("su").click()
#
#         sleep(3)
#         self.driver.quit()
#
#
# def test2():  # 实现driver = webdriver.Chrome()
#     import subprocess
#     p = subprocess.Popen("chromedriver")
#     p.communicate()
#
# if __name__ == '__main__':
#     #test2()
#     case = TestCase()
#     case.test()
#
#


# import re
# f = ('aabbadhbcb')
# test_str = ('aabbadhbcb')
# print(re.sub('[ab]','',f))
#
# str=test_str.replace('ab', '')
# print(str)