'''
@author: haiwen
@date: 2021/3/1
@file: conftest.py
'''
import pytest
from pylibs.webapi.bussiness import OrganizAPI,AccountsAPI

@pytest.fixture(scope='session',autouse=True)
def init_org(empty_orgs):
    org_api = empty_orgs
    sale_org = org_api.add(name='销售部门')
    yield sale_org   #
    #当测试结束时应该删除该环境
    org_api.delete(sale_org['_id'])

#清空签约对象
@pytest.fixture(scope='session')
def empty_accounts(admin_login):
    acc_api = AccountsAPI(admin_login)
    acc_api.delete_all()
    yield acc_api