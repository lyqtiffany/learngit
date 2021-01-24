from interfaceChapter.delivery_systemC.configs.config import NAME_PSW
from interfaceChapter.delivery_systemC.libs.login import Login
from interfaceChapter.delivery_systemC.libs.shop import Shop
#conftest放到哪一个包，只对这个包起作用！，比如当前是test_case包

import pytest
import os
'''
**scope**: ##有4个级别参数
"function" (默认)， 在conftest作用域下，所有的def test_xxx测试方法运行前都会执行1次！
"class" ,在conftest作用域下，每一个的class Testxxx测试类，运行前都会执行一次
"module" ,在conftest作用域下，每一个的test_xxx.py测试模块，运行前都会执行一次
"session" ,在conftest作用域下，这个包运行前只会执行一次
'''

@pytest.fixture(scope='session',autouse=True)  #加了autouse会自动调用
def start_running():
    #在自动化执行一开始就执行下面的函数代码！
    print("start")

    #测试报告数据清除
    try:
        for one in os.listdir('../report/tmp'):
            if 'json' in one or 'txt' in one:
                os.remove(f'../report/tmp/{one}')
    except:
        print('first time run')
    yield  # 相当于teardown用法

#fixture里面函数不能直接调用执行，如果需要调试，需要先注释@pytest.fixture(scope='session',autouse=True)


#思考： 商铺的编辑接口的初始化操作，--只有这一个接口需求，其他不需要
#能不能指定一些接口执行特定的fixture--哪里需要，哪里手动调用

@pytest.fixture(scope='function')
def update_shop_init(shop_init):
    # 1 登录
    #token = Login().login(NAME_PSW, getToken=True)
    # token = Login().login({'username': 'sq0777', 'password': 'xintian'}, getToken=True)

    #  # 2 店铺id   列出店铺调用
    #shop = Shop(token)

    shopID = shop_init.shop_list({'page':1,'limit':20})['data']['records'][0]['id']

    ## 3 图片Info 图片上传接口
    image_info =shop_init.file_upload('123.png','../data/123.png')
    return shopID, image_info


'''
问题点：
    1-店铺更新接口，每一次操作都得操作登陆--累赘的
    2-登陆操作--不只有店铺模块需要--其他也需要
    3-如果业务比较复杂，需要前置条件进行模块化
解决方案：
    1. 能不能把登录操作单独剥离出来
    2. 店铺的实例化也可以剥离出来
    3. 操作一个模块的测试，只需要登录一次
'''

#1 能不能把登录操作单独抽离出来
@pytest.fixture(scope='class')
def login_init():
    token = Login().login(NAME_PSW, getToken=True)
    return token

# 2-店铺的实例也可以剥离出来---需要关联一个fixture
@pytest.fixture(scope='class')
def shop_init(login_init):
    # 在下一个fixture需要使用上一个fixture的返回值，
    # 直接在下一个函数的形参里写上上一个fixture的函数名字，使用他即可以
    shop = Shop(login_init)
    return shop








'''
fixture 使用技巧
方法1，使用函数名直接调用，但是没有返回值
    @pytest.mark.usefixtures('update_shop_init')#写入函数名字，调用conftest
方法2，需要使用到fixture返回值，
   直接在对应的接口函数里，加入一个形参，参数名就是fixture
'''

















# @pytest.fixture(scope='class')
# def xt_shop():
#     print("----类 class fixture")
#
# @pytest.fixture(scope='class')
# def xt_shop2():
#     print("----类 class fixture2")


'''
#如果一个类，或者一个方法，需要多个fixture,可以叠加,先执行就近原则，下往上先2后1执行
@pytest.mark.usefixtures('xt_shop') #类级别
@pytest.mark.usefixtures('xt_shop2') #类级别
class TestShop:

'''

