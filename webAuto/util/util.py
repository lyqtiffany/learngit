import pickle
import random
import string
import time
from webAuto.lib.ShowapiRequest import ShowapiRequest
from time import sleep, strftime, localtime, time

from PIL import Image
import os

import logging

import logging.handlers
import datetime

def get_code(driver, id): #识别图片的验证码

    st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))  # 截图时间戳命名

    #获取验证码图片
    #t = time.time()
    x = os.path.dirname(__file__) # C:\Users\Administrator\PycharmProjects\pythonLearnFrist\webAuto\util
    print(x) #当前文件util.py所在的路径

    path = os.path.dirname(os.path.dirname(__file__)) + '\\screenshot'
    picture_name1 = path + '\\' + str(st) + '.png'

    print(path)  #C:\Users\Administrator\PycharmProjects\pythonLearnFrist\webAuto\screenshot
    print(picture_name1) #C:\Users\Administrator\PycharmProjects\pythonLearnFrist\webAuto\screenshot\1603542863.4486194.png

    driver.save_screenshot(picture_name1) #实现截屏

    ce = driver.find_element_by_id(id) #根据id拿到这个验证码的位置

    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    # dpr = driver.execute_script('return window.devicePixelRatio') #ratio缩放比率
    # print(dpr)
    # im = Image.open(picture_name1)
    # img = im.crop((left*dpr, top*dpr, right*dpr, height*dpr)) 不同分辨率抠图
    #

    im = Image.open(picture_name1)
    img = im.crop((left, top, right, height)) #抠图取得验证码的小图

    #t = time.time()
    st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))  # 截图时间戳命名

    picture_name2 = path + '\\' + str(st) + '.png'
    img.save(picture_name2) #保存抠图取到的验证码小图

    #图片验证码解码
    #r = ShowapiRequest("http://route.showapi.com/184-4", "404646", "2237bfbf1ea3472fbe4b8b69fc6b9a00")
    r = ShowapiRequest("http://route.showapi.com/184-4", "272526", "a924d4e982ae404b8a068b4d1c7784f2")

    r.addFilePara("image", picture_name2)  # 抠图后的图
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post() #
    print(res.text)  # 返回信息
    text = res.json()['showapi_res_body']
    print(text)
    code = text['Result']
    return code

def get_logger():


    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    # TimedRotatingFileHandler根据时间滚动
    rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(message)s"))

    f_handler = logging.FileHandler('error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d]-%(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)

    return logger


def gen_random_str(): #生成随机字符串，数字加字母
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str

def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)

def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)