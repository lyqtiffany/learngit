import requests
import hashlib
#项目的服务器地址+端口
HOST = 'http://121.41.14.39:8082'

# 2 封装加密函数
def get_md5(pwd): #编写加密密码的函数
    md5 = hashlib.md5() #创建对象for md5
    md5.update(pwd.encode('utf-8')) #加密方法
    return md5.hexdigest() #返回十六进制,加密后的结果

def login():
    #1 -url
    url = f'{HOST}/account/sLogin'
    password = get_md5('xintian')
    # 2- 请求体--字典格式
    payload = {'username':'sq0777','password':password}
    #抓包看到的密码是加密的md5 32位小，所以需要转换成加密后的密码输入

    resp = requests.post(url, data=payload)
    #打印请求头,响应对象的请求的头
    print(resp.request.headers) #相应对象.请求.请求头
    print(resp.request.body) #查看请求的Body
    #3 查看响应
    print(resp.text) #返回是字符串格式,响应体
    #响应头
    print(resp.headers)
    print(resp.json()) #———前提，响应数据一定要是json才可以使用，返回是字典
if __name__ == '__main__': #快捷键 ctrl + j
    login()

#通过接口文档的请求参数格式，可以看出来是data格式还是json格式，或者抓包看请求的webform
'''
请求体的数据格式在请求头里面
data: 请求体是表单格式的使用，这个参数默认的格式就是表单
    变量= 值 'Content-Type': 'application/x-www-form-urlencoded'
json： 如果请求提的数据格式是json,可以直接使用这个变量，模式就是json格式
    json 格式 'Content-Type': 'application/json'，
#发送请求带了json格式，就会看到header显示成json格式
files  文件上传接口使用
params  一般是GET请求使用
'''



'''
json跟字典的区别？
    json 一个数据格式，本身就是字符串类型,pycharm控制台打印出来显示是双引号
    dict: 数据类型，可以储存， pycharm控制台打印出来显示是单引号
'''

'''#字典类型
a = {"name" : "sq"} #字典打印出来都是单引号
print(a)

#json
b = '{"password": "123"}'
print(b)

#字典转化成json
import json
print(json.dumps(a))
'''
