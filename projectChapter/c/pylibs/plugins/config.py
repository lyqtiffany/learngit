'''
@author: haiwen
@date: 2021/2/28
@file: config.py
'''
import yaml
def read_yml(path):
    res=yaml.safe_load(open(path,encoding='utf8'))
    return res



if __name__ == '__main__':
    res=read_yml('../../conf/api_conf.yml')
    print(res)