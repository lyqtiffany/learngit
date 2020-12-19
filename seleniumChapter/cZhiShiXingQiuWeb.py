#作业
'''

访问: https://www.vmall.com/
获取一级菜单下包含哪些二级菜单
不包含  查看全部

然后获取底部，热销单品中所有 顶部 带有 爆款字样的产品名称及价格

'''

import time
from selenium import webdriver




driver = webdriver.Chrome()
driver.get('https://wx.zsxq.com/dweb2/index/group/5448528884') #访问网址
time.sleep(8)

# driver.refresh()
driver.maximize_window()




tag = driver.find_element_by_css_selector('div.item:nth-child(2) div.content')#找到第二条置顶
tag.click()

tagBody = driver.find_element_by_css_selector('div.topic-detail-panel') #第二条置顶展开的内容
time.sleep(1)
driver.execute_script("window.scrollBy(0,300)")

tag1 = driver.find_element_by_css_selector('div.tag:nth-child(5)') #找到每天进步一点点
tag1.click() #点击每天进步一点点

driver.execute_script("window.scrollBy(0,500)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面
time.sleep(3)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面


main_content = driver.find_elements_by_css_selector('div.talk-content-container div.content') #讨论区的内容



for m in main_content:
    showall = driver.find_element_by_css_selector('div.talk-content-container div.content + p.showAll') #展开全部按钮
    # comment = driver.find_element_by_css_selector('div.comment-box') #评论
    print(f'序号{main_content.index(m)} 的内容是: {m.text}\n\n ')
print('\n\n\n\n讨论区完成\n\n')

taskD = driver.find_elements_by_css_selector('div.solution-content-container') #作业回答
for td in taskD:
    print(f'作业回答是{td.text}')

print('\n\n\n\n作业回复完成\n\n')

task = driver.find_elements_by_css_selector('div.task-content-container') #作业发布
for t in task:
    print(f'作业发布是{t.text}')











