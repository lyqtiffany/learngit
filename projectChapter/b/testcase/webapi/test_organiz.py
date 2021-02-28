import pytest
from pylibs.webapi.organiz_api import add_org, list_orgs, del_org
from pylibs.webapi.common import login
from conf.env import g_email,g_password


#fixture默认的覆盖范围是函数
@pytest.fixture()
def before_tc000001():
    cookies = login(g_email, g_password)

    yield cookies
    #清除
    res = del_org(org['_id'], cookies)
    print(res)


def test_tc000001(before_tc000001):
    #声明全局变量
    global org
    #用fixture返回值的时候不能加括号
    cookies = before_tc000001
    #step1,增加部门
    org = add_org('测试部门', cookies)
    #step2 列出部门
    org_list = list_orgs(cookies)

    #校验 部门列表是否包含新增部门
    assert org in org_list


if __name__ == '__main__':
    pytest.main(['-s'])


#put 是幂等性的，不管提交多少次，结果都一样的
