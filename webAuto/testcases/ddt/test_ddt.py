# selenium ddt
'''
安装ddt 模块
使用@ddt, @data, @unpack, @file_data加载数据， @pack是进行解包
'''

import os
from ddt import ddt, data, unpack, file_data
import unittest

def get_data():
    testdata = [{'name': 'tom', 'age': 30}, {'name': 'kite', 'age': 20}]

@ddt
class MyTestCase(unittest.TestCase):
    #读取元组数据，单组元素
    @data(1,2,3)  #有数据的地方就用@data来封装
    def test1(self, value):
        print(value)
    '''
    1
    2
    3'''


    # 读取元组数据，多组元素
    @data((1,2,3),(4,5,6))
    def test2(self,value):
        print(value)
    '''
    (1, 2, 3)
    (4, 5, 6)
    '''

    #读取元组数据，拆分数据
    @data((1,2,3),(4,5,6))
    @unpack #拆分数据
    def test3(self, value1, value2, value3):
        print(value1, value2, value3)
    '''
    1 2 3
    4 5 6
    '''

    #列表
    @data([{'name': 'tom', 'age': 30}, {'name': 'kite', 'age': 20}])
    def test4(self, value):
        print(value) #[{'name': 'tom', 'age': 30}, {'name': 'kite', 'age': 20}]


    #字典
    @data({'name': 'tom', 'age': 30}, {'name': 'kite', 'age': 20})
    def test5(self, value):
        print(value)
    '''{'name': 'tom', 'age': 30}
    {'name': 'kite', 'age': 20}'''

    # 字典 拆分
    @data({'name': 'tom', 'age': 30}, {'name': 'kite', 'age': 20})
    @unpack
    def test6(self, name, age):
        print(name, age)
    '''tom 30
    kite 20
    '''

    #变量或者方法调用
    testdata = [{'name': 'tom', 'age': 30}, {'name': 'kite', 'age': 20}]

    #@data(*testdata)
    @data(get_data())
    def test7(self, value):
        print(value)


    #读文件
    @file_data(os.getcwd() + '/test.json') #cwd current working directory
    def test8(self, value2):
        print(value2) # ['tom', 'kate', 'rose']

if __name__ == '__main__':
    unittest.main()