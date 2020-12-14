#作业
'''
#访问：https://m.weibo.cn/
# 点击：大家都在搜
找到：微博热搜榜
点击：微博热搜榜

找到：实时热点，每分钟更新一次新闻列表
将其中带有 热、沸、新字样的热搜信息获取到，并注明属于三种当中的哪一种
'''

from selenium import webdriver

#创建浏览器驱动对象，这里是打开浏览器
#如果driver路径添加到了环境变量，就不用写driver路径了。
driver = webdriver.Chrome()
#访问网址
driver.get('https://m.weibo.cn/')

ele = driver.find_element_by_class_name('m-search')
ele.click()

ele = driver.find_element_by_css_selector('#app > div:nth-child(1) > div:nth-child(1) > div.card.m-panel.card16.m-col-2 > div > div > div:nth-child(8) > div > div > h4')
ele.click()
