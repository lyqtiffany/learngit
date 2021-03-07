'''
@author: haiwen
@date: 2021/3/3
@file: test_contract.py
'''
import allure
import pytest

from pylibs.plugins.convert_data import current_time, get_param, dynamic_report


# @allure.title('{name}')
@dynamic_report('name')
@pytest.mark.parametrize(['name','amount'],get_param('casedata/api_testdata.yml'))
def test_tc003001(empty_contracts,init_account,init_contract_type,init_org,name,amount):
    ctapi=empty_contracts
    othercompany=init_account['_id']  #签约对象
    contract_type=init_contract_type['_id']  #合同分类
    company_id=init_org['_id']  #部门
    #参数字典
    kwargs={
        'name' : name,
        'amount':amount,
        'othercompany' : othercompany,
        'contract_type' : contract_type,
        'company_id' : company_id,
        'create_date' : current_time()
    }
    #创建合同
    contract= ctapi.add(**kwargs)

    #检查合同是否创建
    contract_list = ctapi.list_all()
    assert contract in contract_list


