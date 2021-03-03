'''
@author: haiwen
@date: 2021/2/28
@file: test_organiz.py
'''
import pytest

from pylibs.webapi.organiz_api import add_org,list_orgs,del_org
from pylibs.webapi.common import login
from conf.env import g_email,g_password

@pytest.fixture()
def before_tc000001():
    cookies = login(g_email, g_password)
    yield cookies
    #清除
    res = del_org(org['_id'],cookies)
    print(res)

def test_tc000001(before_tc000001):
    global org  #声明全局变量
    cookies=before_tc000001  #用fixtrue返回值的时候不能加括号
    org = add_org('测试部门',cookies) # step1,增加部门
    #step2 列出部门，查看是否存在新增的部门
    org_list = list_orgs(cookies)

    #校验 部门列表是否包含新增部门
    assert org in org_list



