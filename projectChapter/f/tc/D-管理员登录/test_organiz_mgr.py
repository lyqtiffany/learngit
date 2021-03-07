'''
@author: haiwen
@date: 2021/1/17
@file: test_organiz_mgr.py
'''
import pytest


@pytest.fixture()
def before_tc000001(empty_orgs):
    #直接从初始化哪里拿到api对象 不需要重新生成了
    org_api = empty_orgs
    yield org_api
    org_api.delete(org['_id'])

def test_tc000001(before_tc000001):
    global org
    org_api = before_tc000001
    #step1 创建
    org = org_api.add(name='销售部门')
    #step2 列出并校验
    orgs = org_api.list_all()
    assert org in orgs

@pytest.fixture()
def before_tc000091(empty_orgs):
    global org_api
    org_api = empty_orgs
    org = org_api.add(name='哈哈哈部门')
    yield org


def test_tc000091(before_tc000091):
    org = before_tc000091
    #删除之前存在列表中
    orgs1 = org_api.list_all()
    assert org in orgs1
    #删除如何校验是否删除成功？
    org_api.delete(org['_id'])
    #删除之后部门不存在列表中
    orgs2 = org_api.list_all()
    assert org not in orgs2
