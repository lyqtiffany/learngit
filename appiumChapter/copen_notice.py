#打开通知栏
import time

from appiumChapter.config import boss_caps
from appium import webdriver
#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',boss_caps)
#隐士等待的触发条件是？--获取元素，且当前页面没有该元素才会触发

driver.implicitly_wait(10)#稳定元素

#模拟打开通知栏
driver.open_notifications()

time.sleep(5)
#关闭通知栏--模拟发送返回键
#发送安卓系统标准键盘事件信号
driver.keyevent(4)
# driver.press_keycode(4)  效果同上

print('打开通知栏')

#模拟调节音量
for i in range(5):
    driver.keyevent(24)  #增加音量
    time.sleep(1)

driver.quit()