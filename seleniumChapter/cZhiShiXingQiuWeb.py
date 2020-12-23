import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By #设置元素定位使用哪种方法的
from selenium.webdriver.support.ui import WebDriverWait #元素等待类
from selenium.webdriver.support import expected_conditions as EC #提供条件判断函数

driver = webdriver.Chrome()
#访问网址
driver.get('https://wx.zsxq.com/dweb2/index/group/5448528884')
time.sleep(8)

driver.maximize_window() #窗口最大化

#获取圈子的名字
def get_group_name():
    group_name = driver.find_element_by_css_selector('.group-text .name').text
    return group_name
groupname = get_group_name()

#获取第i个标签话题的内容
def geti(i):
    #点击第二个置顶文章，只有这个文章里面有标签
    sec_topic = WebDriverWait(driver, 3, 0.5).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.item:nth-child(2) div.content")
        )
    )
    sec_topic.click()
    # driver.find_element_by_css_selector('div.item:nth-child(2) div.content').click()
    time.sleep(1)
    # 向下滚动一部分，找到圈子的标签
    driver.execute_script("window.scrollBy(0,300)")
    time.sleep(1)

    tag1 = driver.find_element_by_css_selector(
        f'div[class="topic-detail-panel"] div[class="tag-container"] div[class="tag"]:nth-child({i})')

    tag1_text = tag1.text
    tag1.click() #点击标签

    #通过滚动的次数，控制可以获取到的内容多少
    for i in range(150):
        driver.execute_script("window.scrollBy(0,500)") #滚动页面
        time.sleep(2)

    f = open(f'd:/Tiffany/pyTry/{groupname}/{tag1_text}.txt', 'w+', encoding='utf-8')
    sys.stdout = f
    sys.stderr = f

    topics = driver.find_elements_by_css_selector('app-topic')
    for topic in topics:
        images = topic.find_elements_by_xpath('.//div[@class="image-container"]/img')
        image_src = []
        for image in images:
            src = image.get_attribute('src')
            image_src.append(src)

        links = topic.find_elements_by_xpath('.//a[@class="link-of-topic"]')
        link = []
        for l in links:
            link_src = l.get_attribute('href')
            link.append(link_src)

        print(f'序号{topics.index(topic)} 的内容是: {topic.text}\n\t \n\t有以下图片{image_src}\n\t有以下链接{link}\n\n')
    f.close()
    #点击圈子标题，回到本圈子
    driver.find_element_by_css_selector('a[class="index item"] >div').click()
    time.sleep(3)

for i in range(1,17):
    geti(i)




