from selenium.webdriver.common.by import By
from time import sleep
from webAuto.testcases.pom.pages.basePage import BasePage


class ArticlePage(BasePage):

    def __init__(self, login):
        BasePage.__init__(self, login.driver)
        self.login = login

    click_myarticle_loc = (By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a')  # 点击我的文章
    click_newarticle_loc = (By.NAME, '//*[@id="sidebar-menu"]/li[4]/ul/li[2]/a')  #点击投稿

    article_title_loc = (By.ID, 'article.title')

    #进入iframe
    iframe_loc = (By.XPATH, '//*[@id="cke_1_contents"]/iframe')

    body_loc = (By.XPATH, '/html/body')

    click_add_article_btn_loc = (By.ID, 'submit')  # 点击发布投稿



    def goto_register_page(self):
        self.driver.get('http://jpress.io/user/login')
        self.driver.maximize_window()

    def click_myarticle(self):
        self.click(*self.click_myarticle_loc)

    def click_newarticle(self):
        self.click(*self.click_newarticle_loc)

    def input_article_title(self, title):
        self.type_text(title, *self.article_title_loc)

    def input_article_body(self, body):
        frame1 = self.find_element(*self.iframe_loc)
        self.login.driver.switch_to.frame(frame1)
        self.type_text(body, *self.body_loc)
        self.login.driver.switch_to.default_content()

    def click_add_btn(self):
        self.click(*self.click_add_article_btn_loc)
        sleep(2)




