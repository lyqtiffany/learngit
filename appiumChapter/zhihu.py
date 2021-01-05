'''
@author: haiwen
@date: 2020/9/14
@file: zhihu.py
'''
import time

from appium import webdriver

#告诉appium测试配置信息
caps={
#移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'plathformVersion':'8',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息:
    #1.打开被测app，2.命令行输入以下信息
    #adb shell dumpsys activity recents | findstr intent={
    'appPackage':'com.zhihu.android',
    'appActivity':'.app.ui.activity.LauncherActivity',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒，默认60s
    'newCommandTimeout':36000,
    #设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName':'UiAutomator2',#或者UiAutomator1
    'skipServerInstallation':True#跳过UI2的安装，如果第一次运行程序，不要添加该配置
}


#需要知道appium-server地址
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
#设置隐式等待时间
driver.implicitly_wait(10)
time.sleep(10)
#以content-desc属性定位元素
driver.find_element_by_accessibility_id('热榜').click()
time.sleep(3)
driver.quit()

