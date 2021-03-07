'''
@author: haiwen
@date: 2021/1/17
@file: conftest.py
'''
import pytest
from pylib.webapi.common import login
from pylib.webapi.business import OrganizAPI
from conf.env import g_email,g_psw

#全局session 或 package
@pytest.fixture(scope='session')
def admin_login():
    cookies = login(g_email,g_psw)
    return cookies

#清除当前子部门
@pytest.fixture(scope='session')
def empty_orgs(admin_login):
    org_api = OrganizAPI(admin_login)
    org_api.delete_all()
    return org_api