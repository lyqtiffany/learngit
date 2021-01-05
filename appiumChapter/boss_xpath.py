'''
@author: haiwen
@date: 2020/7/24
@file: boss0726.py
'''
from appium import webdriver

#告诉appium测试配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'plathformVersion':'8',
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
    'newCommandTimeout':6000,
    #设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName':'UiAutomator2',#或者UiAutomator1
    #'skipServerInstallation':True#跳过UI2的安装，如果第一次运行程序，不要添加该配置
}
#需要知道appium-server地址
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#设置隐式等待时间
driver.implicitly_wait(10)

#搜索职位信息
#1.点击搜索
driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/ly_menu"]/*[2]').click()


#操作输入框
# input_ele=driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search')
#//元素标签[@属性="属性值"]
input_ele=driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/et_search"]')
input_ele.click()#先点击一下再输入
input_ele.send_keys('自动化测试')
#选择第一个候选结果
driver.find_element_by_id('com.hpbr.bosszhipin:id/rl_words').click()

#查看职位信息-名称，薪资，公司
jobs=driver.find_elements_by_id('com.hpbr.bosszhipin:id/boss_job_card_view')

for job in jobs:
    name=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_position_name').text
    salary=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_salary_statue').text

    company=job.find_elements_by_id('com.hpbr.bosszhipin:id/tv_company_name')
    #如果可以获取到公司元素
    if company:
        print(f'岗位：{name},薪资：{salary},公司：{company[0].text}')
    #未获取到公司元素
    else:
        print(f'岗位：{name},薪资：{salary},公司：公司名未获取到')

#选择第一个搜索结果，点进去，查看地区、工作年限、学历
job_card=driver.find_element_by_id('com.hpbr.bosszhipin:id/boss_job_card_view')
#进入第一个搜索结果
job_card.click()
#查看地区、工作年限、学历
location=driver.find_element_by_id('tv_required_location').text
experence=driver.find_element_by_id('tv_required_work_exp').text
degree=driver.find_element_by_id('tv_required_degree').text

print(f'地区：{location}，经验:{experence}，学历:{degree}')

#退出关闭session
driver.quit()