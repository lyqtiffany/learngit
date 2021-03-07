'''
@author: haiwen
@date: 2021/1/15
@file: config.py
'''
import yaml
import datetime

def read_yaml(path):
    with open(path,encoding='utf-8') as f :
        res = yaml.safe_load(f.read())
        return res

def current_time(timeformat='%Y-%m-%dT%H:%M:%S.%f'):
    #返回当前时间
    dt = datetime.datetime.now()#先获取当前时间
    #按照接口接收的时间格式，返回时间字符串2020-07-07T07:31:06.754Z
    #%Y-%m-%dT%H:%M:%S.%f
    cur_time = dt.strftime(timeformat)
    #如果时间戳包含微秒
    if timeformat.endswith('%f'):
        #去掉最后三个字符 再加Z
        cur_time = cur_time[:-3]+'Z'
    return cur_time

def get_param(path='case_data/api_case_data.yml'):
    #先读取原始数据
    test_data= read_yaml(path)
    #再转化数据[(name1,amount1),(name2,amount2).....]
    params = test_data['Contracts']
    testdata = [params[key] for key in params]
    res = list(zip(*testdata))
    return res

if __name__ == '__main__':
    #main方法中相对目录要根据文件自身为起点
    # res = read_yaml('../../conf/api_conf.yml')
    # print(res['ContractsAPI']['add'])
    # print(type(current_time()))
    # print(current_time())
    get_param('../../case_data/api_case_data.yml')