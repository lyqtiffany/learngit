#自动化手机浏览器和PC浏览器使用的驱动都是相同的，只需要选择符合该浏览器版本的驱动就可以

#建议选择谷歌浏览器，因为对自动化适配最好

#此时和手机产生了关联，用到了appium


from appium import webdriver

caps={
#平台
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "test",
    #被测app信息-仅限chrome浏览器,不需要填写包名和入口信息
    'browserName':'Chrome',
    'newCommandTimeout':6000,
     #确保自动化之后不重置app
    'noReset':True,
     #底层驱动
    'automationName':'UiAutomator2',
    #指定chromedriver
    'chromedriverExecutableDir':'D:/driver/chromedriver76.0.3809'
    #appium默认使用appium安装文件中自带的webdriver,需要指定合适版本的webdriver
}

driver=webdriver.Remote('http://localhost:4723/wd/hub',caps)

driver.get('http://www.baidu.com')



driver.find_element_by_id('index-kw').send_keys('selenium\n')
# res = driver.find_element_by_css_selector('span[class="c-title-text"]').text
# print(res)

#手机安装chrome的包，先下载apk到电脑上
# 手机连接上电脑,命令adb install  apk的路口

#其他浏览器（需要有对应的驱动）
# 自行获取package activity
# 自行切换webview中
