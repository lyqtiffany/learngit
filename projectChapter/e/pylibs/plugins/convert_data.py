'''
@author: haiwen
@date: 2021/3/3
@file: convert_data.py
'''

#获取当前时间--可以根据指定的格式输出字符串形式的时间
import datetime
import functools

import allure

from pylibs.plugins.config import read_yml


def current_time():
    dt = datetime.datetime.now()  # 带时区
    # datetime.datetime.utcnow()  #不带时区
    #2020-07-07T07:31:06.754Z
    cur_time = dt.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return cur_time[:-3]+'Z'

#转化数据格式
def get_param(path='../../casedata/api_testdata.yml'):
    #读取yaml文件
    res = read_yml(path)['contracts']['add']
    data_list = list(res.values())
    #转化数据格式成 [(),()]这种类型
    params = list(zip(*data_list))
    return params

def dynamic_report(target_title):
    def outter(fun):
        @functools.wraps(fun)  #保留原有的函数信息
        def inner(*args,**kwargs):
            #目标的标题
            title=kwargs.get(target_title,'用例名未定义') # 从键值对参数中获取
            allure.dynamic.title(title)
            res = fun(*args,**kwargs)
            return res
        return inner
    return outter

if __name__ == '__main__':
    print(get_param())