#窗口截图
import time
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

#截取整个页面
driver.get_screenshot_as_file("./dall.png") #保存到当前路径，格式官方建议png
#截取单个元素
ele = driver.find_element_by_id("kw")
ele.screenshot("./dele.png")

#driver.get('file:///C:/Users/Administrator/PycharmProjects/pythonLearnFrist/seleniumChapter/dalert.html')

'''#触发对话框，只有确定按钮
driver.find_element_by_id("bu1").click()
time.sleep(1)
#操作对话框,先获取对象，赋值给变量
al = driver.switch_to.alert #注意switch_to后面是一个.
#确定对话框
al.accept()'''

'''#触发确认框
driver.find_element_by_id("bu2").click()
#获取确认框对象
al = driver.switch_to.alert
#确认框有确定accept()和取消dismiss()
# al.accept()
#取消确认框
al.dismiss()'''

'''#提示框，有确定，取消和文本输入
driver.find_element_by_id("bu3").click()
al = driver.switch_to.alert
#可以获取警告框的文本信息
print(al.text)
#可以向提示框输入文本
al.send_keys("这是我输入的内容") #输入的内容会生效，但是不会在界面上展示
al.accept()
# al.dismiss()'''

driver.quit()