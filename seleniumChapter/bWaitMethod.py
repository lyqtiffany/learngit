#设置元素等待

#大多数web应用都是ajax和javascript开发的
#当我们加载页面的时候，一些元素是需要时间的。
#就有可能发生，代码执行到了，而元素没有加载出来
#此时就会出现找不到元素的情况。


#此问题的解决方案是，在元素定位之前，进行等待。等到元素出现，
# import time
# time.sleep(5)
#time.sleep的缺点是，可能第1秒已经出现了元素，但是还要强制等待剩余的4秒


#显示等待，使webdriver等待某个条件的成立，当条件成立时，继续往下执行代码。
#若条件不成立，则每隔一段时间（默认0.5）检查一次，
# 直到达到最大超时时间，还不成立，就抛出超时异常

from selenium import webdriver
#显示等待所需
from selenium.webdriver.common.by import By #设置元素定位使用哪种方法的
from selenium.webdriver.support.ui import WebDriverWait #元素等待类
from selenium.webdriver.support import expected_conditions as EC #提供条件判断函数




driver = webdriver.Chrome()
driver.get("https://m.weibo.cn/")

#隐式等待，只对声明之后行数的代码有效
#隐式等待默认参数是秒，如下代码，最大超时时间是5秒
#当脚本执行到某个元素定位的时候，能定位就继续执行。
#如果不能定位，以轮询的方式（0.5秒检查一次），不断的判断元素是否能被定位
#假设在第x（x<=最大超时时间）秒定位到元素了，就不等了，继续往下执行
#若直到最大时长还没定位成功，就抛出异常。
driver.implicitly_wait(5)

#找到大家都在搜
driver.find_element_by_xpath("html/body/div/div/div/div/a//div").click()

#点击微博热搜榜
# driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div/div[8]/div/div/h4").click()

#显示等待，若等到元素，就不会再等了。比如0.3秒找到了元素，就继续运行，不再等待剩余的时间
#若想使用显式等待，则必须对元素定位进行修改。显示等待必须是对某个具体的元素作主动声明
#第一个参数是driver, 第二个参数是最大超时时间，第三个参数是轮询时间。
#每隔0.5秒检查一次元素是否存在，最多等待5s，
#若在最大时间内，找到了元素，就不等了，继续往下执行
#若到达最大超时时间，还找不到元素，就抛出超时异常
ele = WebDriverWait(driver, 5, 0.5).until(
    EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div[1]/div[1]/div[2]/div/div/div[8]/div/div/h4")
    )
)
ele.click()
#visibility_of_element_located()里面接收元组形式的参数




