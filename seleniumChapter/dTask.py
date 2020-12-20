# http://vip.ytesting.com/q.do?a&id=ff8080817345903c017348c7acac02ec

import time
from selenium import webdriver
from selenium.webdriver.common.by import By #设置元素定位使用哪种方法的
from selenium.webdriver.support.ui import WebDriverWait #元素等待类
from selenium.webdriver.support import expected_conditions as EC #提供条件判断函数

driver = webdriver.Chrome()

driver.get('http://127.0.0.1:8088/')
driver.maximize_window()

#输入用户名
driver.find_element_by_name('username').send_keys('libai')
#输入密码
driver.find_element_by_name('password').send_keys('opmsopms123')
#登陆按钮
driver.find_element_by_css_selector('button').click()

#找到项目管理
project_ele = WebDriverWait(driver, 5, 0.5).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[class="left-side-inner"] i[class="fa fa-book"] + span')
    )
)
#点击项目管理
project_ele.click()
time.sleep(1)

#点击新项目
new_project = WebDriverWait(driver, 10, 0.5).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'div[class="pull-right"]')
    )
)
new_project.click()
# driver.find_element_by_css_selector('div[class="pull-right"]').click()
# time.sleep(1)

#输入项目名称
project_name = WebDriverWait(driver, 5, 0.5).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'div[class="col-sm-10"] input[name="name"]')
    )
)
project_name.send_keys('新建项目1220')

#项目别名
driver.find_element_by_css_selector('div[class="col-sm-10"] input[name="aliasname"]').send_keys('1220项目别名')

#进入iframe才能输入描述
iframe1 = driver.find_element_by_css_selector('iframe[class="ke-edit-iframe"]')
driver.switch_to.frame(iframe1)

#描述
describe_msg = driver.find_element_by_css_selector('body[class="ke-content"]')
describe_msg.send_keys('项目描述语句')

driver.switch_to.default_content()

#点击提交
driver.find_element_by_css_selector('button[type="submit"]').click()

#新建项目成功
project_dialog = WebDriverWait(driver, 3, 0.5).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.modal-content')
    )
)
#关闭项目创建成功的提示
project_dialog.find_element_by_css_selector('button[class="close"]').click()