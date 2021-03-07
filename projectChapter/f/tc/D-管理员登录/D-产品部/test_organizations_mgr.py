'''
@author: haiwen
@date: 2021/1/17
@file: test_organizations_mgr.py
'''
import pytest


@pytest.fixture()
def after_tc000002(init_org,empty_orgs):
    org_api = empty_orgs
    yield org_api
    #清除数据
    org_api.delete(org['_id'])

def test_tc000002(after_tc000002):
    global org
    org_api = after_tc000002
    # step1 创建
    org = org_api.add(name='开发部门')
    # step2 列出并校验
    orgs = org_api.list_all()
    assert org in orgs

@pytest.fixture()
def before_tc000051(init_org,empty_orgs):
    global org_api
    org_api = empty_orgs
    sale_org = org_api.add(name = '销售部门')
    yield sale_org
    org_api.delete(sale_org['_id'])

def test_tc000051(before_tc000051):
    sale_org = before_tc000051
    #修改销售部门为测试部门
    org_api.edit(sale_org['_id'],name='测试部门')
    #校验是否修改成功--根据销售部门的ID判断其对应的name是否改成测试部门
    orgs = org_api.list_all()
    for org in orgs:
        #根据id判断其数据是否为销售部门，然后再判断名称
        if org['_id'] == sale_org['_id']:
            assert org['name'] == '测试部门'
            break
