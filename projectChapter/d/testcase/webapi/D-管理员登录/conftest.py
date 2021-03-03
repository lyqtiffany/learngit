'''
@author: haiwen
@date: 2021/3/1
@file: conftest.py
'''
#管理员登录
import pytest

from conf.env import g_password,g_email
from pylibs.webapi.common import login
from pylibs.webapi.bussiness import OrganizAPI

@pytest.fixture(scope='session')
def admin_login():
    cookies = login(g_email,g_password)
    return cookies

@pytest.fixture(scope='session')
def empty_orgs(admin_login):
    org_api = OrganizAPI(admin_login)
    org_api.delete_all() #清空所有部门
    return org_api

