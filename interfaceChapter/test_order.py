
# 需要安装pytest_xdist 分布式框架

import pytest
import time

def test001():
    assert 1==1
    time.sleep(2)
    print("-----test001 is running")

def test002():
    assert 1==1
    time.sleep(2)
    print("-----test002 is running")

if __name__ == '__main__':
    pytest.main(['test_order.py','-s','-n','8'])  #-n分布式,8是8核

