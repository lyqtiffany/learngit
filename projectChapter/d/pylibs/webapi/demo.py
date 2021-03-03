'''
@author: haiwen
@date: 2021/3/1
@file: demo.py
'''
class Base():
    def current_name(self):
        print(self.__class__.__name__)


class A(Base):
    pass

class B(Base):
    pass

if __name__ == '__main__':
    A().current_name()
    B().current_name()