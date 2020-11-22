import pytest

#夹具,被后面的方法引用
@pytest.fixture() #里面scope参数默认的值是function，区分使用范围,可以改成模块

def init():
    print('init...')
    return 1

def test1(init):
    print('test1')

def test2(init):
    print('test2')

if __name__ == '__main__': #点击左边运行，可以看到两个test1 test2都执行了
    pytest.main(['-sv', 'test06fixture.py'])
    # 输出test06fixture.py::test1 init...
    #也输出test06fixture.py::test2 init...





