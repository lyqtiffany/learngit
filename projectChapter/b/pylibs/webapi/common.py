'''
@author: haiwen
@date: 2021/2/26
@file: common.py
'''
import requests
from conf.env import host
from pylibs.plugins.config import read_yml

def login(email,psw):
    payload={"user":{"email":email},"password":psw,"code":"","locale":"zhcn"}
    resp = requests.post(f'{host}/accounts/password/authenticate',
                        json=payload)
    #返回鉴权信息---cookies
    return resp.cookies


#API基础类--用于封装增删改查等公共方法

class BaseAPI:
    def __init__(self,cookies):
        #假设API配置名等于API类名
        cls_name='获取当前classname'  # 如何获取当前classname

        self.conf=read_yml('conf/api_conf.yml')[cls_name]
        self.path=self.conf['path']
        self.cookies = cookies
        #url
        self.url = f'{host}{self.path}' #host+path
        #spaceid
        self.spaceid=self.cookies['X-Space-Id']

    def add(self,**kwargs):  # 传参形式 name=xxx,age=xxx,...
        payload=self.conf['add']  #新增请求的模板
        #更新spaceid
        kwargs['space'] = self.spaceid
        #替换模板数据
        payload.update(kwargs)  #直接更新字典的值
        resp = requests.post(self.url,json=payload,cookies=self.cookies)
        return resp.json()['value'][0]  #返回具体的数据--返回value的第一个元素

    def delete(self,_id):
        resp = requests.delete(f'{self.url}/{_id}',cookies=self.cookies)
        return resp.json()

    def update(self,_id):
        payload = self.conf['update']  #修改的请求参数模板
        resp = requests.put(f'{self.url}/{_id}',json= payload, cookies=self.cookies)
        return resp.json()

    def list_all(self):
        pass

    #删除所有
    def delete_all(self):
        pass


#部门API
class OrganizAPI(BaseAPI):
    pass

#合同API
class ContractsAPI(BaseAPI):
    pass

# if __name__ == '__main__':
#     c = login('tester44@test.com','devops')
#     #cookies是一个类字典的对象
#     print(c['X-Space-Id'])