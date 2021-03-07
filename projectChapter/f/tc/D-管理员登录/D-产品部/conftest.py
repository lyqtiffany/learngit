'''
@author: haiwen
@date: 2021/1/17
@file: conftest.py
'''
import pytest


@pytest.fixture(scope='session')
def init_org(empty_orgs):
    #生成产品部门数据
    org_api = empty_orgs
    org = org_api.add(name='产品部')
    #返回产品部门数据对象
    yield org
    #测试用例结束后，需要清除对应的数据
    org_api.delete(org['_id'])
