'''
@author: haiwen
@date: 2021/2/28
@file: test_organiz.py
'''
import pytest

from pylibs.webapi.bussiness import OrganizAPI
from pylibs.webapi.common import login
from conf.env import g_email,g_password

@pytest.fixture()
def before_tc000001(empty_orgs):
    # cookies = login(g_email, g_password)
    org_api = empty_orgs
    yield org_api
    #清除
    org_api.delete(org['_id'])

def test_tc000001(before_tc000001):
    global org
    org_api = before_tc000001
    # step1,增加部门
    org = org_api.add(name='测开部门')
    #step2 列出部门，查看是否存在新增的部门
    org_list = org_api.list_all()
    #校验 部门列表是否包含新增部门
    assert org in org_list


def test_tc000091(empty_orgs):
    org_api = empty_orgs
    org = org_api.add(name = '测试部门')
    res = org_api.delete(org['_id'])
    assert res == {}  # check 1
    assert org_api.list_all()[1:] == []    #check 2
