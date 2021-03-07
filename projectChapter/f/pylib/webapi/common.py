'''
@author: haiwen
@date: 2021/1/15
@file: common.py
'''
import requests
from conf.env import host
from pylib.plugins.config import read_yaml
#定义公共的API
def login(email,password):
    path='/accounts/password/authenticate'
    payload={
            "user":{"email":email},
             "password":password,
             "code":"",
             "locale":"zhcn"
             }
    resp = requests.post(f'{host}{path}',json=payload)
    #当前登录请求应该返回什么?
    #cookies对象中保存了接口的鉴权信息
    return resp.cookies

#定义API基类
class BaseAPI:
    def __init__(self,cookies):
        #需要知道当前的class名称
        classname = self.__class__.__name__ #自动获取当前类的名称
        #直接读取配置文件数据--文件路径需要和导库路径相对目录起点统一
        self.conf = read_yaml('conf/api_conf.yml')[classname]
        #path 同一个业务接口是相同的
        self.path=self.conf['path']
        #cookies
        self.cookies = cookies
        #spaceid 公共
        self.space = self.cookies['X-Space-Id']

    def add(self,**kwargs):
        payload=self.conf['add']  #参数模板
        #请求参数更新spaceid
        kwargs['space'] = self.space
        #payload进行参数替换
        payload.update(kwargs)
        resp = requests.post(f'{host}{self.path}',json=payload,cookies=self.cookies)
        #需要返回有效数据--value的第一个元素
        return resp.json()['value'][0]

#调用的时候需要指定参数名 如 name='xxx',age='11'
    def edit(self,_id,**kwargs):
        #取出set，方便修改数据
        _set = self.conf['edit']['$set']
        # 请求参数更新spaceid
        kwargs['space'] = self.space
        #修改set数据
        _set.update(kwargs)  # 该方法只能更新一层字典，多层嵌套的更新不了
        #嵌套回payload
        payload = {}
        payload['$set']=_set
        resp = requests.put(f'{host}{self.path}/{_id}',json=payload,cookies=self.cookies)
        return resp.json()

    def list_all(self,**kwargs):
        params={'spaceid':self.space}
        params.update(kwargs)
        resp = requests.get(f'{host}{self.path}',params= params,cookies=self.cookies)
        #返回数据--有效数据value对应的列表
        return resp.json()['value']

    def delete(self,_id):
        resp = requests.delete(f'{host}{self.path}/{_id}',cookies=self.cookies)
        return resp.json()

    def delete_all(self):  #一般用于清除环境
        #先列出 再挨个删除
        items = self.list_all()
        for item in items:
            self.delete(item['_id'])


if __name__ == '__main__':
    cookies=login('testuser43@test.com','123456')
    print(cookies['X-Space-Id'])