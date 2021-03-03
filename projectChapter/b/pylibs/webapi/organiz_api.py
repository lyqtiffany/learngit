'''
@author: haiwen
@date: 2021/2/28
@file: organiz_api.py
'''
import requests
from conf.env import host
# 合同API
#增加
def add_org(name,cookies):
    payload={ "name": name,
                "parent": "KygmxccyRb4KSeaN7",
                "sort_no": 100,
                "hidden": False,
                "space": cookies['X-Space-Id'] } #从cookies取spaceid
    resp=requests.post(f'{host}/api/v4/organizations',json=payload,cookies=cookies)
    return resp.json()['value'][0] #返回部门信息--value的第一个元素

#列出
def list_orgs(cookies):
    resp = requests.get(f'{host}/api/v4/organizations', cookies=cookies)
    return resp.json()['value'] #返回部门列表

#删除
def del_org(organization_id,cookies):
    resp = requests.delete(f'{host}/api/v4/organizations/{organization_id}',cookies=cookies)

    return resp.json()

