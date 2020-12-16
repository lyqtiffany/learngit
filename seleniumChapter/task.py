#作业
'''
#访问：https://m.weibo.cn/
# 点击：大家都在搜
找到：微博热搜榜
点击：微博热搜榜

找到：实时热点，每分钟更新一次新闻列表
将其中带有 热、沸、新字样的热搜信息获取到，并注明属于三种当中的哪一种
'''


import time
from selenium import webdriver
from seleniumChapter.bWaitLib import waitEle
from selenium.webdriver.common.by import By


#创建浏览器驱动对象，这里是打开浏览器
#如果driver路径添加到了环境变量，就不用写driver路径了。
driver = webdriver.Chrome()
#访问网址
driver.get('https://m.weibo.cn/') #get会帮忙等待

#点击：大家都在搜
# driver.find_element_by_class_name('m-search').click() #老方法
driver.find_element_by_xpath("//label[@class='m-search']").click()
# time.sleep(2)

#点击：微博热搜榜, #元素不好定位的时候，可以分步进行定位，先定位大元素
waitEle(driver, 5, 0.5, By.XPATH, "//div[@id='app']/div/div/div[2]//div[@class='card-main']/div[8]").click()

'''#点击：微博热搜榜
# hotSearchBlock = driver.find_element_by_class_name('m-col-2') #找到热搜榜所在的大标签
# hotSearchSli = hotSearchBlock.find_elements_by_class_name('m-item-box') #在大标签中搜热搜
# hotSearchSli[-1].click()  #点击：微博热搜榜，它必然是在最后一个'''
time.sleep(2)

##//div[@id="app"]/div[1]/div[2]//div[@class="card card11"]
#实时热点的每一行热搜
hotDivSli = driver.find_elements_by_xpath('//div[@id="app"]/div[1]/div[2]//div[@class="card card11"][1]/div/div/div')
# print(hotDivSli)

'''#定位到实时热点，每分钟更新一次新闻列表 card list
#hotSli = driver.find_element_by_css_selector("#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div>div")
#card list,每个热搜标题都有card4这个class
#hotDivSli = hotSli.find_elements_by_class_name("card4")'''


for hotDiv in hotDivSli: #每个热搜标题
    # 判断热搜标题是否有图片标签，热，沸，新
    #注意，当使用父元素.find_element_by_xpath()这种方式定位时
    #表达式开头必须用.开头
    #否则xpath会从整个文档的最开始寻找，xpath就是这么实现的
    iconSli = hotDiv.find_elements_by_xpath(".//span[@class=\"m-link-icon\"]/img") #每一行热搜的图片列表

    if iconSli: # 列表不为空，表示热搜有图片标签
        #获取图片img标签的src属性
        srcLink = iconSli[0].get_attribute("src") #有图片时，只有一个图片，直接用下标0来指定图片
        # print(srcLink)
        #判断图片类型
        if "hot" in srcLink:
            hotType = "热"
            hotText = hotDiv.find_element_by_xpath(".//span[@class=\"main-text m-text-cut\"]").text #最前面加上.
            print(f'{hotType}:{hotText}')
        elif "new" in srcLink:
            hotType = "新"
            hotText = hotDiv.find_element_by_class_name("main-text").text
            print(f'{hotType}:{hotText}')
        elif "fei" in srcLink:
            hotType = "沸"
            hotText = hotDiv.find_element_by_class_name("main-text").text
            print(f'{hotType}:{hotText}')

time.sleep(2)
driver.quit()

