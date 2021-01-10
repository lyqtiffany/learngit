#调试app内部webview
# 混合(Hybrid)应用
# 一部分是原生界面和代码，另外一部分是内嵌网页
# 比如微信，支付宝
# 内嵌一个浏览器内核，由浏览器内核实现，这个时候关键是浏览器内核版本，需要找对应驱动

#查看手机webview的版本，手机设置里面搜索webview实现

# 混合模式，元素位置都是在 android.wekit.webview 下面

#准备工作1：修改源码-开启webview,debug
# app 修改编译
# 对webview对象加入setWebContentsDebuggingEnabled的调用
'''
protected void onCreate(Bundle savedInstanceState){
    super.onCreate(savedInstanceState);
    WebView myWebView = (WebView) findViewByID(R.id.jcywebview);
    myWebView.setWebConetntsDebuggingEnabled(true);
    } '''
#注意，从应用市场下载的app不具备此条件


#WebView的自动化
'''
WebView的内容，不依赖所在app
    只是打开一个url
    直接用chrome浏览器打开对应的网页
    使用手机模式
Appium自动化webview
    appium中把所有的界面环境称之为context
    native部分的context名字一般为NATIVE_APP
    webview部分的context则为WEBVIEW_XXXX(应用app package名)
    我们怎么查看当前有哪些context呢？
    driver.contexts
    而显示当前context的则是
    driver.current_context
    切换drvier.switch_to_context(contextname)
'''

'''
#少用，不常用：
通过chrome查看webview元素
chrome://inspect/#devices 浏览器输入这个网站
会检查当前连接的手机有没有打开webview
再点击Inspect
    需要通过chrome的远程调试功能，vpn
    需要android 4.4(KitKat)或者更高版本
'''

'''
总结：
1. 在电脑上自动化手机页面不需要appium
2. 用手机浏览器自动化需要匹配手机浏览器版本的驱动
3. 只有开启debug模式的app才能被自动化webview的内容
4. 自动化webview界面内容需要匹配webview版本的驱动
 自动化对象        测试工具     驱动参考
 电脑端网页        selenium   PC端浏览器
 手机端网页        appium     手机浏览器
 混合app-webview  appium     手机系统webview
'''


from appium import webdriver

caps={
# 平台
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "test",
    # 被测app的信息
    'appActivity':'.MainActivity',
    'appPackage':'com.example.haiwen.myhybirdapp',
    # 设置命令超时时间
    'newCommandTimeout': 6000,
    # 确保自动化之后不重置app
    'noReset': True,
    # 底层驱动
    'automationName': 'UiAutomator2',
    # 如果不想每次都安装UI2驱动，可以这么设置
    'skipServerInstallation': True,
    #使用指定的webview的驱动---指定浏览器所在的目录
    'chromedriverExecutableDir':"D:/driver/chromedriver81.0.4044.138"
    #不配置的时候切换webview有报错，会提示device的webview版本，比如Chrome version on the device: Chrome/81.0.4044.138
}
#启动webdriver
driver=webdriver.Remote('http://localhost:4723/wd/hub',caps)

driver.implicitly_wait(10)

#输入网址--豆瓣
driver.find_element_by_id('com.example.haiwen.myhybirdapp:id/editText').send_keys('https://m.douban.com/home_guide')
#点击enter开始访问
driver.find_element_by_id('com.example.haiwen.myhybirdapp:id/button').click()

#查看app所有contexts
print(driver.contexts)

#查看当前处于哪个context
print(driver.current_context)

#如果以html控件形式自动化webview,需要切到对应的webiew context中
#切换webview成功的前提，
# 1，被测应用开启webview debug模式--从市场安装的不具备此条件
# 2，需要选择符合该操作系统当前webview版本的chromedriver
driver.switch_to.context('WEBVIEW_com.example.haiwen.myhybirdapp')

#像浏览器一样开始操作网页内容
print('当前的context是：%s'%driver.current_context)

#以网页形式自动化，appnium里面有selenium的包的
#搜索电影名称
driver.find_element_by_css_selector('input[class="search-input"]').send_keys('肖申克的救赎\n')

#查看电影分数

rate=driver.find_element_by_css_selector('li.search-module:nth-child(1) .search_results_subjects li:nth-child(1) .rating>span:nth-child(2)').text

print(f'电影评分是{rate}')

#切回原生界面，只能用原生（app支持的）的定位方法，
driver.switch_to.context('NATIVE_APP')
print(f'当前contect: {driver.current_context}')


#切回原生app重新访问百度页面--自动化搜索松勤---自行实现

driver.quit()






