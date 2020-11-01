from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui
from webAuto.util import util
from time import sleep

class TestWriteArticle(object):
    def __init__(self, login):
        self.login = login

    def test_add_article_error(self):
        title = ''
        body = ''
        expected = '标题不能为空'

        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a').click() #点击我的文章
        sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[2]/a').click() #点击投稿

        self.login.driver.find_element_by_name('article.title').send_keys(title)  # 输入文章标题
        self.login.driver.find_element_by_xpath('/html').send_keys(body)
        self.login.driver.find_element_by_id('submit').click()

        loc = (By.CLASS_NAME, 'toast-message')
        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_all_elements_located(loc))  # 验证弹框出现
        msg = self.login.driver.find_element(*loc).text
        sleep(3)

        assert msg == expected

    def test_add_article_pass(self):
        title = 'test001我的文章'
        body = 'test001我的文章内容'
        expected = '文章保存成功。'

        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a').click() #点击我的文章
        sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[2]/a').click() #点击投稿

        self.login.driver.find_element_by_name('article.title').send_keys(title)  # 输入文章标题

        #切入iframe
        sleep(2)
        frame1 = self.login.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe')

        self.login.driver.switch_to.frame(frame1)
        sleep(2)

        self.login.driver.find_element_by_xpath('/html/body').send_keys(body)
        # 切出frame
        self.login.driver.switch_to.default_content()

        sleep(2)
        self.login.driver.find_element_by_id('submit').click()


        loc = (By.CLASS_NAME, 'toast-message')
        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))  # 验证弹框出现
        msg = self.login.driver.find_element(*loc).text
        sleep(3)

        assert msg == expected

    def test_delete_article_pass(self):
        expected = '确定要删除该文章吗？删除后不可恢复'

        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()  # 点击文章列表
        article = self.login.driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div[2]/table/tbody/tr[2]/td[1]/strong/a')
        ActionChains(self.login.driver).move_to_element(article).perform()

        sleep(1)

        #删除前文章数
        article_num = len(self.login.driver.find_elements_by_class_name('jp-actiontr'))
        print(article_num)

        del_elem = self.login.driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div[2]/table/tbody/tr[2]/td[1]/div/div/a[2]')
        del_elem.click()

        sleep(1)
        #等待提示框
        WebDriverWait(self.login.driver, 5).until(EC.alert_is_present()) #验证弹框出现
        alert = self.login.driver.switch_to.alert

        sleep(3)
        #验证
        assert alert.text == expected
        alert.accept()

        #删除后文章数
        sleep(3)
        article_num2 = len(self.login.driver.find_elements_by_class_name('jp-actiontr'))
        print(article_num2)

        assert article_num == article_num2 + 1
