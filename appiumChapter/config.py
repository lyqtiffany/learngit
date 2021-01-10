boss_caps={
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

#拷贝公共配置项目，比如一个小米手机，给另外一个设备使用
xiaomi_caps = boss_caps.copy()
meizu_caps = boss_caps.copy()

xiaomi_caps['plathformVersion'] = '9'
xiaomi_caps['deviceName'] = 'xiaomi' #adb devices查找出来的
#systemport作为UI2和电脑之间通信的端口，如果同时测试多台设备，需要更改该端口
#自定义端口范围8245-8299,建议8250之后开始
xiaomi_caps['systemPort'] = '8251'

meizu_caps['plathformVersion'] = '8'
meizu_caps['deviceName'] = 'meizu'
meizu_caps['systemPort'] = '8253'
