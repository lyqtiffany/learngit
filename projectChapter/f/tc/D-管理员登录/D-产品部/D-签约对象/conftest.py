'''
@author: haiwen
@date: 2021/1/18
@file: conftest.py
'''

#初始化签约对象--客户--vip客户
import pytest
from pylib.webapi.business import AccountsAPI

@pytest.fixture(scope='session')
def init_accounts(admin_login,init_org):
    accounts_api = AccountsAPI(admin_login)
    #增加VIP客户
    vip_account = accounts_api.add(name='VIP客户',company_ids=[init_org['_id']])
    yield vip_account
    #清除环境
    accounts_api.delete(vip_account['_id'])
