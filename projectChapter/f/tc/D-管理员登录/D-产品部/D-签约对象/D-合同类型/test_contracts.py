'''
@author: haiwen
@date: 2021/1/18
@file: test_contracts.py
'''
import allure
import pytest

from pylib.plugins.tools import dynamic_report
from pylib.webapi.business import ContractsAPI
from pylib.plugins.config import current_time, get_param


#aftert只是命名规范 表示只做清除
@pytest.fixture()
def after_tc003001(admin_login,):
    cont_api = ContractsAPI(admin_login)
    yield cont_api
    #cont_api.delete(contract['_id'])

#合同
# @allure.title('{name}')
@dynamic_report('name')   #自定义测试用例装饰器
@pytest.mark.parametrize(['name','amount'],get_param())
def test_tc003001(after_tc003001,init_accounts,init_contract_type,init_org,name,amount):
    #测试报告用例
    allure.dynamic.title('测试用例：'+name)
    cont_api = after_tc003001
    global contract
    #签约对象
    accounts_id = init_accounts['_id']
    #合同类型
    contract_type_id = init_contract_type['_id']
    #部门数据
    org_id = init_org['_id']

    #准备参数
    in_params={
        'name' : name,
        'amount': amount,
        'othercompany' : accounts_id,
        'contract_type' : contract_type_id,
        'company_id' : org_id,
        'create_date' : current_time(),
    }

    #创建合同
    contract = cont_api.add(**in_params)

    #校验生成的合同数据
    contracts = cont_api.list_all()
    assert contract in contracts
