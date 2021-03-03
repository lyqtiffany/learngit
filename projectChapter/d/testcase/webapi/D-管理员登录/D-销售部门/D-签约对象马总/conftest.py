'''
@author: haiwen
@date: 2021/3/3
@file: conftest.py
'''
import pytest
from pylibs.webapi.bussiness import AccountsAPI,ContractTypesAPI

@pytest.fixture(scope='session')
def init_account(empty_accounts,init_org):
    acc_api = empty_accounts # 直接使用fixture返回的api对象
    #创建签约对象
    account_ma = acc_api.add(name='马总',company_ids=[init_org['_id']])
    yield account_ma
    #清除
    acc_api.delete(account_ma['_id'])

#清空分类
@pytest.fixture(scope='session')
def empty_contypes(admin_login):
    contype_api = ContractTypesAPI(admin_login)
    contype_api.delete_all()
    yield contype_api