'''
@author: haiwen
@date: 2021/1/22
@file: test_schedules.py
'''
import allure
import pytest

from pylib.webui.bussiness import LoginPage
from pylib.plugins.config import read_yaml
@pytest.fixture()
def before_tc005001(init_loginPage):
    schedule_page = init_loginPage.login('testuser43@test.com', '123456').to_schedule_page()
    yield schedule_page
    schedule_page.logout()  #退出

@pytest.mark.parametrize('task',read_yaml('case_data/api_case_data.yml')['Schedules']['task'])
def test_tc005001(before_tc005001,task):
    schedule_page = before_tc005001
    schedules =schedule_page.new_schedule(task,'小张').logout().login('xiaozhang@test.com','123456').list_schedules()
    #校验
    assert task in schedules
