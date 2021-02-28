#restful 格式的接口，

import requests
from conf.env import host
from pylibs.webapi.common import login
from conf.env import g_email,g_password

#增加部门
def add_org(name,cookies):
    payload = {"name": name,
               "parent": "KygmxccyRb4KSeaN7",
               "sort_no": 100,
               "hidden": False,
               "space": cookies['X-Space-Id']} #从cookies取spaceId

    resp = requests.post(f'{host}/api/v4/organizations',json=payload,cookies=cookies)
    return resp.json()['value'][0] #返回部门信息，value的第一个元素


#列出部门
def list_orgs(cookies):
    resp = requests.get(f'{host}/api/v4/organizations', cookies=cookies)
    return resp.json()['value'] #返回部门列表


#删除部门
def del_org(organization_id,cookies):
    resp = requests.delete(f'{host}/api/v4/organizations/{organization_id}', cookies=cookies)
    return resp.json()



if __name__ == '__main__':
    cookies = login(g_email, g_password)
    org = add_org('测试部门', cookies)
    print(org)
    org_list_res = list_orgs(cookies)
    print(org_list_res)
    assert org in org_list_res
    del_org(org['_id'],cookies)