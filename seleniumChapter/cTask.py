
#http://vip.ytesting.com/q.do?a&id=ff8080817238543f01723b6246cc011e
'''登录 http://www.51job.com
    点击高级搜索
    输入搜索关键词 python
    地区选择 杭州
    职能类别 选 计算机软件 -> 高级软件工程师
    工作年限选 1-3 年

搜索职位， 抓取页面信息。 得到如下的格式化信息

    Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
    Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
    on开发工程师 | 杭州新思维计算机有限公司 | 杭州-西湖区 | 1-1.5万/月 | 04-27'''


import time
from selenium import webdriver
#显示等待所需
from selenium.webdriver.common.by import By #设置元素定位使用哪种方法的
from selenium.webdriver.support.ui import WebDriverWait #元素等待类
from selenium.webdriver.support import expected_conditions as EC #提供条件判断函数

driver = webdriver.Chrome()
driver.get('http://www.51job.com') #访问网址
driver.maximize_window()

driver.find_element_by_css_selector('a.more').click() #点击高级搜索
#输入搜索关键词python
driver.find_element_by_css_selector('input#kwdselectid').send_keys('python')

#点击地区
driver.find_element_by_css_selector('input#work_position_input').click()
#点击热门城市
driver.find_element_by_css_selector('li#work_position_click_center_left_each_000000').click()

#清空原来选择的城市
pre_city = WebDriverWait(driver, 3, 0.5).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'div[class="de d1"]  em')
    )
)
pre_city.click()
# pre_city = driver.find_element_by_css_selector('div#work_position_click_multiple_selected > span >em')

#选择杭州
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()
#点击确定，确定城市为杭州
driver.find_element_by_css_selector('span#work_position_click_bottom_save').click()

#python相关关键字,此处会遮挡职业类别
driver.find_element_by_css_selector('span[class="bg b_key"]').click()
#点击职能类别的+号
driver.find_element_by_id('funtype_click').click()
#点击计算机/互联网/通信/电子
driver.find_element_by_id('funtype_click_center_left_each_0100').click()
#点击后端开发
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()
#点击高级软件工程师
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()
#点击确定
driver.find_element_by_id('funtype_click_bottom_save').click() #点击确定

#展开工作年限下拉框
driver.find_element_by_css_selector('#workyear_list span[class="ic i_arrow"]').click()
#1-3年
driver.find_element_by_css_selector('#workyear_list span:nth-child(3)').click()

#点击搜索按钮
driver.find_element_by_css_selector('div[class="btnbox p_sou"] .p_but').click()


#搜索列表结果
job_list = WebDriverWait(driver, 3, 0.5).until(
    EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "div.j_joblist div.e")
    )
)

# Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
for job in job_list:
    job_title = job.find_element_by_xpath('./a/p/span[1]')


    company = job.find_element_by_xpath('./div[@class="er"]/a[@class="cname at"]')
    salary = job.find_element_by_xpath('.//p[@class="info"]/span[@class="sal"]')
    location_info = job.find_element_by_xpath('.//p[@class="info"]/span[@class="d at"]')
    location = location_info.text.split('|')[0].strip()

    people_num = job.find_element_by_xpath('./div[@class="er"]/p[@class="dc at"]')
    people_num = people_num.text.split('|')[-1].strip()
    print(f'{job_title.text} | {company.text}  | {location} | {salary.text} | {people_num}')

driver.quit()