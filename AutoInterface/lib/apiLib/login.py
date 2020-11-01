
#1 完成登陆代码的编写--依据接口文档
#http://121.41.14.39:9097/api/loginS
#mds在线加密for password https://md5jiami.51240.com/

import pprint#完美打印
import hashlib #哈希库
from AutoInterface.configs.config import HOST
import requests

#发请求
'''
data---一般是表单
json---  json格式
files---文件
'''

# pprint.pprint(resp.json())
# print(resp.request.headers)#请求头

'''
封装思路：
    1- 登录接口比较特殊
        用途：
            1- 获取登录的token----给后续接口做关联
            2- 接口本身也需要自动化测试
'''

# url = f'{HOST}/api/loginS'
# payload = {'username':'20154084', 'password': 'e10adc3949ba59abbe56e058f20f883e'}
#
# resp = requests.post(url, json=payload)
# print(resp.text) #字符串
# print(resp.json()) #返回字典格式
# pprint.pprint(resp.json())
# print(resp.request.headers) #请求头，json格式
# inData = {'username': '20154084', 'password': 'e10adc3949ba59abbe56e058f20f883e'}

'''
封装思路：
1-登录接口比较特殊
    用途：
    1-获取登录的token--给后续接口做关联
    2-登陆接口本身也需要自动化测试
'''


def get_md5(pwd): #编写加密密码的函数
    md5 = hashlib.md5() #创建对象for md5
    md5.update(pwd.encode('utf-8')) #加密方法
    return md5.hexdigest() #返回十六进制,加密后的结果


class Login: #登录类
    def login(self, inData, getToken=False): #实例方法
        #1--接口的url-考虑参数化
        url = f'{HOST}/api/loginS' #字符串
        #2-构建请求
        payload = inData # 请求体 body
        payload['password'] = get_md5(payload['password']) #字典-修改键值对
        # 字典修改值操作：  字典名[键名]=新的值
        resp = requests.post(url, json=payload)
        if getToken:#获取token
            return resp.json()['token'] #获取token
        else: #登录，  不获取token
            return resp.json()  # 返回字典格式
if __name__ == '__main__':
    testdata = {'username': '20154084', 'password': '123456'}
    #实例化对象
    #res = Login().login(testdata,getToken=True) #获取token
    res = Login().login(testdata)  # 实现登录
    print(res)


