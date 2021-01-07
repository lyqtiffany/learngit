'''
@author: haiwen
@date: 2020/9/16
@file: swipe.py
'''
import time


from appium import webdriver
#初始化driver对象-用于控制手机
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'plathformVersion':'10',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息:
    #1.打开被测app，2.命令行输入以下信息
    #adb shell dumpsys activity recents | findstr intent={
    'appPackage':'com.hpbr.bosszhipin',
    'appActivity':'.module.launcher.WelcomeActivity',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒，默认60s
    'newCommandTimeout':36000,
    #设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName':'UiAutomator2',#或者UiAutomator1
    #'skipServerInstallation':True#跳过UI2的安装，如果第一次运行程序，不要添加该配置
}


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#隐士等待的触发条件是？--获取元素，且当前页面没有该元素才会触发

driver.implicitly_wait(10)#稳定元素

# time.sleep(10)
# #模拟滑动
# x1=500
# y1=1300
# x2=x1
# y2=y1-1000 #这个1000是像素
# driver.swipe(x1,y1,x2,y2)
#
# input('滑动结束')


block=driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/lv_list"]/android.view.ViewGroup')
ele_size=block.size
#模拟滑动
x1=500
y1=1300
#滑动的距离等于区块元素的高度
distance=ele_size['height']
x2=x1
y2=y1-distance

#滑动最常见的使用场景
#例如查找工作信息---爬虫工程师，找到后停止滑动并打印相关信息
def search_job(target):
    while 1:
        job_name=driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_position_name').text
        if target in job_name:
            print('找到工作')
            salary=driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_salary_statue').text
            print(f'工作：{job_name}，薪资:{salary}')
            break
        driver.swipe(x1,y1,x2,y2,1500)#时间单位都是ms
search_job('测试开发')
driver.quit()