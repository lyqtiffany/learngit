'''
@author: haiwen
@date: 2021/1/22
@file: demo.py
'''
from selenium.common.exceptions import WebDriverException


class Base:
    def __init__(self):
        pass

    def get_class_name(self):
        return self.__class__.__name__

    def get_parent_class_name(self):
        # 首先获取继承的父类
        bases=self.__class__.__bases__
        return [base.__name__ for base in bases]

    def get_ancestor_names(self):
        return [ancestor.__name__ for ancestor in self.__class__.mro()][:-2]


class Father(Base):
    def init_driver(self):
        self.driver = 'abc'

    def del_driver(self):
        self.driver = None

    @classmethod
    def auto_instance(cls):
        return cls



class Child(Father):
    pass

class Sub(Child):
    pass



if __name__ == '__main__':
    print(Child().get_class_name())
    print(Base().get_parent_class_name())
    print(Sub().get_ancestor_names())

