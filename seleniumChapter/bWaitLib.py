from selenium import webdriver
#显示等待所需
from selenium.webdriver.common.by import By #设置元素定位使用哪种方法的
from selenium.webdriver.support.ui import WebDriverWait #元素等待类
from selenium.webdriver.support import expected_conditions as EC #提供条件判断函数

# driver = webdriver.Chrome()
# driver.get("https://m.weibo.cn/")



#将显式等待封装成了一个函数
def waitEle(driver, timeout, poll_frequency, findType, findExpression ):
    ele = WebDriverWait(driver, timeout, poll_frequency).until(
        EC.visibility_of_element_located(
            (findType, findExpression)
        )
    )

    return ele
