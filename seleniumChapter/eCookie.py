#cookie是服务端存在我们本地客户端的一些信息
# 并且是不涉及隐私的信息（这个通常要程序员自我约束）
#cookie里边要存哪些内容也不是固定的，完全按照开发者的心意去实现



import pprint
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8088/')

#登陆一下，增加session
#输入用户名
driver.find_element_by_name('username').send_keys('libai')
#输入密码
driver.find_element_by_name('password').send_keys('opmsopms123')
#登陆按钮
driver.find_element_by_css_selector('button').click()


#获取所有的cookie
cookieSli = driver.get_cookies() #列表里面存了多个字典
pprint.pprint(cookieSli)
#根据name获取某个cookie,需要用cookie的name
# cookie = driver.get_cookie('beegosessionID')
# print(cookie)


#使用cookie模拟登陆
cookieSli = [{'domain': '127.0.0.1',
  'httpOnly': False,
  'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436',
  'path': '/',
  'secure': False,
  'value': '1608555856'},
 {'domain': '127.0.0.1',
  #'expiry': 1640091856,
  'httpOnly': False,
  'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436',
  'path': '/',
  'secure': False,
  'value': '1608555856'},
 {'domain': '127.0.0.1',
  #'expiry': 1640091852,
  'httpOnly': True,
  'name': 'beegosessionID',
  'path': '/',
  'secure': False,
  'value': '139e3b8514aa1808a6dd414b3df811e2'}]

#先清除所有的cookie(原来是未登录的cookie)
driver.delete_all_cookies()

for cookie in cookieSli:
    #添加cookie
    driver.add_cookie(cookie) #一次添加一个cookie
driver.refresh()


'''
关于ui自动化登陆的问题
  1 如果权限足够，则申请服务端权限，读取验证码
  2 也可以在权限足够的情况下，去修改服务器验证码的值
  3 若权限不足，则请开发将测试环境的验证码验证取消，此时输入任何内容都能通过
  4 测试环境设置一个万能验证码
  需要注意的是，第3,4种方法，必须在上线后修正

'''

