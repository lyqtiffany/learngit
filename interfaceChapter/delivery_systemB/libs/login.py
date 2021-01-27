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
from interfaceChapter.delivery_systemB.configs.config import HOST

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
        inData["password"] = get_md5(inData["password"])
        payload = inData
        # print(id(payload)) 每次的payload  ID地址是同一个值

        # 抓包看到的密码是加密的md5 32位小，所以需要转换成加密后的密码输入
        resp = requests.post(url, data=payload)
        # print(resp.encoding)
        # resp.encoding="gbk" #修改响应的编码,encoding是属性
        if getToken == True:
            return resp.json()['data']['token'] #获取token
        else:
            return resp.json()  #响应数据

if __name__ == '__main__': #快捷键 ctrl + j
    res = Login().login({'username':'sq0777','password':'xintian'})
    print(res)
    res1 = Login().login({'username':'sq0777','password':'xintian'}, getToken=True)
    print(res1)


    #编码，把字符转换成计算机可以识别的
    name = "你好"
    name1 = name.encode("utf-8")  # 编码
    print(name1)

    #把计算机的编码解码成人可以看懂的
    name2 = name1.decode("gbk") #解码
    print(name2)
    name2 = name1.decode("utf-8")  # 解码，解铃还得系铃人
    print(name2)

    '''
    在接口测试里的编码乱码
    服务器，接口返回的响应数据是开发决定的，是什么编码必须遵守
    响应中，content-type的charset会显示服务器的编码
    '''



