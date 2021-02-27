import pytest
from pylibs.webapi.common import fun1
# # 为了把a 做为根目录，所以把a目录设置了source root，a目录就会变成蓝色，（同一时间最好只有一个蓝色文件夹）
#这样导入的路径就不用从projectChapter.a开始写了


def test_fun():
    print('执行项目测试用例')

if __name__ == '__main__':
    fun1()
    pytest.main(['-s','--alluredir=tmp/report'])
