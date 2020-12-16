
#获取断言信息

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#获取当前页面的标题
print(driver.title)

#获取当前页面的url
print(driver.current_url)

#获取标签对之间的文本信息
  #1,标签元素如果不展示在页面上，获取的结果为空
  #2，如果标签对中间没有值，获取到的结果也是空的
  #3，如input 之类的单标签，获取结果也是空的
print(driver.find_element_by_class_name("title-text").text)

#获取元素的某个属性
ele = driver.find_element_by_id("kw")
print(ele.get_attribute("class"))


driver.quit()








