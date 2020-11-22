import os


# def test1():
#     print('test1')
import time
from selenium import webdriver
from time import sleep
import pyautogui
from PIL import Image  #PIL 需要pip install PIL
import requests
import pytesseract  #pytesseract 需要 pip install pytesseract

#命令终端安装PyAutoFUI   pip install, 在元素不能选中时，通过x,y坐标来点击

def testXY():
    driver = webdriver.Chrome() #打开谷歌浏览器
    driver.get('http://jpress.io/user/register') #打开首页
    driver.maximize_window()
    sleep(1)
    elem = driver.find_element_by_id('agree') # 注册页面，同意的button只能通过xy 坐标点击，需要安装导入pytest
    print(elem.rect)
    rect = elem.rect
    sleep(1)

    pyautogui.moveTo(rect['x']+10, rect['y']+130) #pyautogui.click(rect['x']+10, rect['y']+130) 也可以
    pyautogui.click()
    sleep(3)

def yanzheng(): #'http://jpress.io/user/register'注册页面的验证码小图，截取
    # 验证码，使用pytesseract模块和PIL模块解决
    #安装 pip install  pytesseract    pip install pil
    #网页验证码解决思路：截屏整个页面，获得验证码坐标数据，根据坐标数据抠图，使用pytesseract模块进行验证
    browser = webdriver.Chrome() #打开谷歌浏览器
    browser.get('http://jpress.io/user/register') #打开首页
    browser.maximize_window()

    #获取验证码图片
    t = time.time()
    picture_name1 = str(t) + '.png'
    browser.save_screenshot(picture_name1) #截屏

    ce = browser.find_element_by_id("captchaimg") #获得目前验证码所在地址
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    im = Image.open(picture_name1)
    img = im.crop((left, top, right, height)) #crop抠图

    t = time.time()
    picture_name2 = str(t) + '.png'

    img.save(picture_name2)#这里就是截取到的验证码图片
    browser.close()

def getStringYanZheng(): #验证简单的验证码或者通过第三方api识别验证码

    ##验证老师举例的简单验证码图片
    # path = os.path.dirname(os.path.abspath(__file__)) #tf try
    # file_path = 'file:///' + path + 'test.png'  #验证老师举例的简单验证码图片
    # image1 = Image.open(file_path)
    #
    # image1 = Image.open('test.png') #打开第一步扣出的验证码部分的图片
    # str = pytesseract.image_to_string(image1)
    # print(str)#就可以验证简单的验证码，只是加了些点，没有横竖线干扰的那种


    #复杂验证码,通过后台的AI算法
    #https://www.showapi.com/apiGateway/view/184/4 从这个万维易源网站下载Showapirequest的包 #第三方API
    #Showapirequest的包 放到当前项目的lib文件夹下面, 里面需要用到requests模块，pip3 install requests
    #https://www.showapi.com/apiGateway/view/184/4 API调用参考
    from webAuto.lib.ShowapiRequest import ShowapiRequest

    r = ShowapiRequest("http://route.showapi.com/184-4", "404646", "2237bfbf1ea3472fbe4b8b69fc6b9a00")
    # r = ShowapiRequest("http://route.showapi.com/184-4","272526","a924d4e982ae404b8a068b4d1c7784f2")

    r.addFilePara("image", "test.png")  # 抠图后的图
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    print(res.text)  # 返回信息

    body = res.json()['showapi_res_body']
    print(body['Result'])

