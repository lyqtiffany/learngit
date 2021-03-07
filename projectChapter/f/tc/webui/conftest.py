'''
@author: haiwen
@date: 2021/1/22
@file: conftest.py
'''
import pytest

from pylib.webui.bussiness import LoginPage
@pytest.fixture(scope='session')
def init_loginPage():
    loginPage = LoginPage()
    yield loginPage
    loginPage.close_browser()
