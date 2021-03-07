'''
@author: haiwen
@date: 2021/1/18
@file: conftest.py
'''

#准备合同类型数据---销售合同
import pytest
from pylib.webapi.business import ContractTypesAPI

@pytest.fixture(scope='session')
def init_contract_type(admin_login):
    ct_api = ContractTypesAPI(admin_login)
    sale_contract = ct_api.add(name='销售合同',code='202101')
    yield sale_contract
    #清除
    ct_api.delete(sale_contract['_id'])
