'''
@author: haiwen
@date: 2021/3/1
@file: test_orgnaizations.py
'''
import pytest
from pylibs.webapi.bussiness import OrganizAPI

@pytest.fixture()
def before_tc000002(empty_orgs):
    org_api = empty_orgs
    yield org_api
    org_api.delete(org['_id'])

def test_tc000002(before_tc000002):
    global org
    org_api = before_tc000002
    #step1 新增
    org = org_api.add(name= '产品部门')
    #step2 查询并校验
    org_list = org_api.list_all()
    assert org in org_list


@pytest.fixture()
def before_tc000051(empty_orgs):
    org_api = empty_orgs
    org = org_api.add(name='研发部门')
    yield org,org_api
    #执行清除动作
    org_api.delete(org['_id'])


def test_tc000051(before_tc000051):
    #修改
    org_api = before_tc000051[1]  # 元组取值
    org = before_tc000051[0]
    org_api.update(org['_id'],name='测试部')
    #检查是否修改成功
    org_list = org_api.list_all()
    for item in org_list:
        # 通过ID判断部门信息，再检查名称是否已经修改
        if item['_id'] == org['_id']:
            assert item['name']=='测试部'
            # assert item["sort_no"]==100
            break #检查完就可以退出


def test_tc000052(empty_orgs):
    org_api = empty_orgs
    org_list1= org_api.list_all()
    res = org_api.update('99999',name='不存在的部门')
    # 1.返回结果提示指定数据不存在
    print(res)
    assert res['error']['code'] == 500 # 客户端错误一般是400，服务端500
    # 2.如果没有修改成功，系统数据不应该改变
    org_list2 = org_api.list_all()
    assert org_list1 == org_list2
