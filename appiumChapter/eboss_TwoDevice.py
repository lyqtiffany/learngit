#pyyaml是python的一个专门针对yaml文件操作的模块
#pip install pyyaml

import time
import os
from multiprocessing import Process
import subprocess
from appiumChapter.config import boss_caps
from appium import webdriver
import yaml

#思考，抽离密码变量，每次密码修改之后，能够获取调用，多次修改，不要写死，考虑配置文件yml,pyyml
#验证码手动操作，用input()阻塞验证码部分执行，手动输入


#初始化driver对象-用于控制手机
def start_app(port, caps):
    global driver
    driver = webdriver.Remote(f'http://localhost:{port}/wd/hub',caps)
    driver.implicitly_wait(10)#稳定元素



def get_login_text():
     #获取登陆页面的信息，用来断言
    login_ele = driver.find_elements_by_id('com.hpbr.bosszhipin:id/wechatLoginText')
    #login_page_ele = driver.find_element_by_id("com.hpbr.bosszhipin:id/tv_password_login")
    #assert login_page_ele.text == "账号密码登录"
    if login_ele: #表示存在登陆页面
        print('进入到登陆页面')
        return login_ele[0].text
    else:
        return None


def change_pwd(old_pwd,new_pwd):
    #1 进入我的标签
    driver.find_element_by_id("com.hpbr.bosszhipin:id/iv_tab_4").click()
    #2 点击右上角的设置图标
    driver.find_element_by_id("com.hpbr.bosszhipin:id/iv_general_settings").click()
    #3 进入账号与绑定
    driver.find_element_by_id("com.hpbr.bosszhipin:id/cl_item").click()
    #4进入设置密码
    time.sleep(1)
    driver.find_element_by_xpath('//*[@text="修改密码"]').click()
    #5 完成密码设置
    #到了修改密码页面之后，禁止dump截屏了，可以先打印driver.page_source,把页面源码拷贝出来，然后在里面搜索关键词定位元素
    #输入旧密码
    driver.find_element_by_id("com.hpbr.bosszhipin:id/et_old").send_keys(old_pwd)
    #输入新密码
    driver.find_element_by_id("com.hpbr.bosszhipin:id/et_new").send_keys(new_pwd) #test1234
    #输入确认密码,完成修改密码
    driver.find_element_by_id("com.hpbr.bosszhipin:id/et_new_confirm").send_keys(new_pwd)
    #点击完成按钮
    driver.find_element_by_id("com.hpbr.bosszhipin:id/btn_save").click()


    #跳入了手机号登陆注册页面


def before_change():
    psw=load_yml()
    login(psw['old'])

def after_change(old_psw,new_psw):
    # 交换密码
    psw = {}
    psw['new'] = old_psw
    psw['old'] = new_psw
    dump_yml({'psw': psw})

#写yaml文件
def dump_yml(data):
    with open('password.yml', 'w', encoding='utf8') as f:
        content=yaml.safe_dump(data)
        f.write(content)

#读yml文件
def load_yml():
    with open('password.yml', encoding='utf8') as f:
        #content = f.read() #读取文件的内容
        #data = yaml.safe_load(content) #转化文件的内容
        psw=yaml.safe_load(f.read())['psw']
    return psw

def login(new_pwd):
    driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_password_login').click()
    driver.find_element_by_id('com.hpbr.bosszhipin:id/et_password').send_keys(new_pwd)
    time.sleep(10) #暂停，手动滑动验证码图片
    driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_login').click()

def end_app():
    driver.quit()


def start_appium(*port):
    for p in port:
        cmd = 'appium -p ' + str(p)
        print(cmd)
        subprocess.Popen(cmd, shell=True)

def close_appium(port):
    # 查看端口被哪个进程占用
    p = subprocess.Popen(f'netstat -ano |findstr {port}', shell=True, stdout=subprocess.PIPE) #linux netstat -ntpl|grep port
    res1 = p.stdout.read().decode('gbk') #解码命令的输出,windows默认用gbk,linux用utf-8
    if res1: #如果获取到了输出，表示该端口对应的PID存在
        pid = res1.split()[-1]
        os.system(f'taskkill /f /pid {pid}') #linxu关闭进程 kill -9

def sync_appium_server():
    process_list=[]
    for port in ['4723','4725']:
        p=Process(target=start_appium,args=(port,))
        p.start()
        process_list.append(p)
    return process_list


def terminal_sync_server(process_list):
    for p in process_list:
        p.terminate()

#main方法用来测试自定义的方法
if __name__ == '__main__':
    print(load_yml())