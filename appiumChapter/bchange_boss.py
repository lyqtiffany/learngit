import time

from appiumChapter.config import boss_caps
from appium import webdriver
import yaml

#思考，抽离密码变量，每次密码修改之后，能够获取调用，多次修改，不要写死，考虑配置文件yml,pyyml
#验证码手动操作，用input()阻塞验证码部分执行，手动输入


#初始化driver对象-用于控制手机

driver = webdriver.Remote(f'http://localhost:4723/wd/hub',boss_caps)
driver.implicitly_wait(10)#稳定元素


def change_pwd(old_pwd,new_pwd):
    #1 进入我的标签
    driver.find_element_by_id("com.hpbr.bosszhipin:id/iv_tab_4").click()
    #2 点击右上角的设置图标
    driver.find_element_by_id("com.hpbr.bosszhipin:id/iv_general_settings").click()
    #3 进入账号与绑定
    driver.find_element_by_id("com.hpbr.bosszhipin:id/cl_item").click()
    #4进入设置密码
    time.sleep(1)
    driver.find_element_by_xpath('//*[@text="设置密码"]').click()
    #5 完成密码设置
    #到了修改密码页面之后，禁止dump截屏了，可以先打印driver.page_source,把页面源码拷贝出来，然后在里面搜索关键词定位元素
    #输入旧密码
    driver.find_element_by_id("com.hpbr.bosszhipin:id/et_old").send_keys(old_pwd)
    #输入新密码
    driver.find_element_by_id("com.hpbr.bosszhipin:id/et_set_password").send_keys(new_pwd) #test1234
    #输入确认密码,完成修改密码
    driver.find_element_by_id("com.hpbr.bosszhipin:id/et_confirm_password").send_keys(new_pwd)
    #点击完成按钮
    #driver.find_element_by_id("com.hpbr.bosszhipin:id/btn_confirm").click()

change_pwd("test1234","test12345")

# driver.quit()



