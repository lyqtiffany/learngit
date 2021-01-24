#token一般通过响应消息体传给客户端
#一般需要账号与密码通过特定的接口（登陆、获取token接口）去访问服务器，才能返回一个token

# session 是登陆用户和未登录用户访问网站，会生成不同的session（会话）, 每个session有唯一的session ID
# session经过服务器鉴权，一般通过响应头里面的set-cookie让客户端保存JsessionID,后续访问网站会携带这个cookie（header里面）

#前后端分离的项目一般用token
#前后端不分离的项目有些用session

'''
登陆接口的特性
    1 作为普通的接口测试
    2 需要获取token给后续接口关联
'''

import requests
import hashlib
from interfaceChapter.delivery_systemC.configs.config import HOST
import copy

#121.41.14.39:8082/doc.html#/home  swagger 接口文档

def get_md5(pwd):  # 编写加密密码的函数
    md5 = hashlib.md5()  # 创建对象for md5
    md5.update(pwd.encode('utf-8'))  # 加密方法
    return md5.hexdigest()  # 返回十六进制,加密后的结果

class Login:
    # 2 封装加密函数
    def login(self, inData, getToken = False):
        #1 -url
        url = f'{HOST}/account/sLogin'
        #调用加密函数
        # inData["password"] = get_md5(inData["password"])
        # payload = inData

        #NAME_PSW是全局变量，里面的密码被Md5多次加密，需要拷贝給新对象，避免每次修改全局变量地址
        payload = copy.copy(inData )
        payload["password"] = get_md5(payload["password"])


        # 抓包看到的密码是加密的md5 32位小，所以需要转换成加密后的密码输入
        resp = requests.post(url, data=payload)
        if getToken == True:
            return resp.json()['data']['token'] #获取token
        else:
            return resp.json()  #响应数据

if __name__ == '__main__': #快捷键 ctrl + j
    res = Login().login({'username':'sq0777','password':'xintian'})
    print(res)
    res1 = Login().login({'username':'sq0777','password':'xintian'}, getToken=True)
    print(res1)



