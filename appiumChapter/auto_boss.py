#UI automator viewer定位元素工具D:\forAppium\androidsdk\tools\bin\UIautomatorviewer.bat 双击，然后点左上角的第二个图标
#WEditor也是一个定位元素的工具pip install weditor     启动 python -m weditor #adb连接手机，手机默认浏览器用谷歌或者火狐 #手机上看到ATX工具安装好


#官网查看基本配置项 http://appium.io/docs/en/writing-running-appium/caps/#general-capabilities
#appium 元素定位方法
#1 目标元素有resource-id且id唯一，或者排第一个，就用find_elements_by_id，（默认找到第一个）
#2 目标元素有content-desc属性,但是这个属性少见
#find_element_by_accessibility_id
#3 通过xpath来查找元素,通过xpath语法描述元素的特征（自身属性，元素的层级关系）
    #app里面class的值和标签一样
    # //标签[@属性=""]
    #选择子元素 //标签[@属性值=""]/*
    #选择父元素 //标签[@属性值=""]/..


#adb无线连接
    #手机和电脑处于同一个局域网
    #首先用USB有限连接方式连接到计算机
    #激活手机的无线服务 adb tcpip 5555
    #adb connect 手机IP
    #adb devices查看无线和有线都连接上了，需要拔掉USB线后不支持文件传输，就不能无线连接


#导包
import time

from appium import webdriver

#准备自动化配置信息
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

#初始化driver对象-用于控制手机-启动被测应用
#IP-appium-server所在机器的网络ip，port-监听的端口号，path固定/wd/hub
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.implicitly_wait(10)#稳定元素

#点击放大镜,
eles=driver.find_elements_by_id('com.hpbr.bosszhipin:id/img_icon')#先取所有符合条件的元素
#找到第二个元素--放大镜
btn=eles[1]
btn.click()

#搜索框输入职位信息
search_input=driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search')
search_input.send_keys('软件测试')#输入参数
time.sleep(2)#等待关键字输入完毕
#模拟直接输入enter
driver.keyevent(66)
#选择符合条件的第一个搜索结果
driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_filtered_name').click()


#获取当前页面所有职位信息元素
job_msg=driver.find_elements_by_id('com.hpbr.bosszhipin:id/view_job_card')

for job in job_msg:
    #输出岗位名称
    name=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_position_name')
    print(name.text)
    #输出薪资
    salary=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_salary_statue')
    print(salary.text)
    #输出公司名称
    company=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_company_name')
    #第四个卡片有可能会被遮挡，判断公司名字是否找到
    #companys=job.find_elements_by_id('com.hpbr.bosszhipin:id/tv_company_name')
    #if companys:
    #   print('%s|%s|%s'%(name.text,salary.text,companys[0].text))
    #else:
    #   print('%s|%s|%s'%(name.text,salary.text,'屏幕长度影响，没有找到公司名字'))

    print('%s|%s|%s'%(name.text,salary.text,company.text))



# input('......')

# 练习，获取地区，年限，学历
# driver.quit()