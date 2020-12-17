#作业
'''

访问: https://www.vmall.com/
获取一级菜单下包含哪些二级菜单
不包含  查看全部

然后获取底部，热销单品中所有 顶部 带有 爆款字样的产品名称及价格

'''

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#访问网址
driver.get('https://www.vmall.com/')
driver.maximize_window()

'''
#为什么一级菜单，不定位到li,也能打印出一级菜单？
#二级菜单，没有看到text属性，为什么也能通过text拿到标签内容？老师直接这样用的，再回顾一遍课程内容
'''

category = driver.find_elements_by_xpath("//ol[@class=\"category-list\"]/li")
for first_Cate in category:
    first_Category = first_Cate.text #获取每个大类的标题，比如手机，笔记本，平板等
    print(f"一级菜单： {first_Category}")  #打印一级菜单的内容

    ActionChains(driver).move_to_element(first_Cate).perform() #鼠标悬停到一级菜单

    sec_category = first_Cate.find_elements_by_xpath(".//ul[@class=\"subcate-list clearfix\"]/li[@class=\"subcate-item\"]")

    for sed_Cate in sec_category:
        second_category = sed_Cate.text
        print(f"\t{second_category}")  #打印二级菜单的选项


# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# .send_keys(Keys.END)

driver.execute_script("window.scrollBy(0,500)") #滚动页面
time.sleep(1)
driver.execute_script("window.scrollBy(0,9000)") #滚动页面

#热销单品，精品推荐，手机等大分类
ele = driver.find_elements_by_xpath("//div[@class=\"h\"]/h2")


#热销单品里面没有爆款，所以扩大范围了。
eles = driver.find_elements(By.XPATH, '//li[@class="grid-items"]')
hot_eles = driver.find_elements(By.XPATH, '//li[@class="grid-items"]//p[@class="grid-tips"]')

for k in eles and hot_eles:
    if k.text == '爆款':
        name = k.find_element(By.XPATH, '//li[@class="grid-items"]//div[@class="grid-title"]').text
        price = k.find_element(By.XPATH, '//li[@class="grid-items"]//p[@class="grid-price"]').text
        print(f'爆款： {name}， 价格: {price}')



# driver.quit()

