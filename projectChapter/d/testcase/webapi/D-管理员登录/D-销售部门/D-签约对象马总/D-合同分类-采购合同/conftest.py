'''
@author: haiwen
@date: 2021/3/3
@file: conftest.py
'''
import pytest
from pylibs.webapi.bussiness import ContractTypesAPI,ContractsAPI
# session级别的Fixture不能套用低于session级别的fixture 其他依次类推
@pytest.fixture(scope='session')
def init_contract_type(empty_contypes):
    cta= empty_contypes
    #创建合同分类
    buy_contype= cta.add(name='采购合同',code='2021-3-3')
    yield buy_contype
    cta.delete(buy_contype['_id']) # 清除该合同分类

#清空当前系统合同
@pytest.fixture(scope='session')
def empty_contracts(admin_login):
    con_api = ContractsAPI(admin_login)
    con_api.delete_all()
    yield con_api