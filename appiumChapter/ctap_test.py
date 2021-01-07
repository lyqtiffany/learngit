#导包
import time

from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号
    'plathformVersion':'8',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息
    'appPackage':'com.renaissance.bingzhe',
    'appActivity':'.UnityPlayerActivity',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #指定自动化驱动
    'automationName':'UiAutomator2',

}

#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#隐士等待的触发条件是？--获取元素，且当前页面没有该元素才会触发

driver.implicitly_wait(10)#稳定元素
#通过寻找目标页面指定元素出现来判断，目标页面加载成功
# driver.find_element_by_id('com.alpha.lagouapk:id/position_name')
#通过坐标点击输入框
#463 155
#获取屏幕高度
time.sleep(18)

#如果屏幕的分辨率不同但是比例（同样比例18:9）一致，可以用相对屏幕尺寸的方法来获取坐标
size = driver.get_window_size() #获取屏幕尺寸
height = size['height']
weight = size['weight']
pos_x = weight/16*11 #屏幕宽带的11/16
pos_y = height/16  #屏幕高度的1/16

driver.tap([(880,70)]) #模拟坐标点击用tap,列表里面带元组
#只有当目标控件出现的时候点击才有效果，所有坐标点击前可以sleep

#坐标对不同分辨率的手机有影响，
# 坐标轴原点是手机左上角









input('输入任意键退出代码')
driver.quit()


