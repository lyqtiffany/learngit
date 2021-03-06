from selenium import webdriver

#创建浏览器驱动对象，这里是打开浏览器
#如果driver路径添加到了环境变量，就不用写driver路径了。
driver = webdriver.Chrome()
#访问网址
driver.get('file:///C:/Users/Administrator/PycharmProjects/pythonLearnFrist/seleniumChapter/atest.html')

'''#匹配元素列表，返回所有能匹配到的元素，存在一个列表里面
eleLi = driver.find_elements_by_class_name('xyz')
#获取元素的文本值，并打印出来
for ele in eleLi:
    print(ele.text)'''

#class属性有复合类,可以任意取里面的一个单词，用作class的匹配查找，但是结果可能不唯一
#如果要找到唯一定位，最好在F12里面ctrl F,输入匹配规则，只出现一个匹配结果
# #class属性中间的空格是间隔符号，表示这个元素有多个class属性


driver.quit()

# http://vip.ytesting.com/q.do?a&id=ff808081703da3a4017041c7a6ea00e3

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

#创建浏览器驱动对象，这里是打开浏览器
#如果driver路径添加到了环境变量，就不用写driver路径了。
driver = webdriver.Chrome()
#访问网址
driver.get('https://m.weibo.cn/')

#点击：大家都在搜
driver.find_element_by_class_name('m-search').click()
time.sleep(2)

#点击：微博热搜榜
hotSearchBlock = driver.find_element_by_class_name('m-col-2') #找到热搜榜所在的大标签
hotSearchSli = hotSearchBlock.find_elements_by_class_name('m-item-box') #在大标签中搜热搜
hotSearchSli[-1].click()  #点击：微博热搜榜，它必然是在最后一个
time.sleep(1)

#定位到实时热点，每分钟更新一次新闻列表 card list
hotSli = driver.find_element_by_css_selector("#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div>div")
#card list,每个热搜标题都有card4这个class
hotDivSli = hotSli.find_elements_by_class_name("card4")


for hotDiv in hotDivSli: #每个热搜标题
    # 判断热搜标题是否有图片标签，热，沸，新
    iconSli = hotDiv.find_elements_by_class_name("m-link-icon")
    # 如果有图片标签
    if iconSli:
        #获取img标签
        img = iconSli[0].find_element_by_tag_name("img")
        #获取src属性
        srcLink = img.get_attribute("src")
        # print(srcLink)
        #判断图片类型
        if "hot" in srcLink:
            hotType = "热"
            hotText = hotDiv.find_element_by_class_name("main-text").text
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



