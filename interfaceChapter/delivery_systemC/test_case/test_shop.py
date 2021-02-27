import pytest
import os
from interfaceChapter.delivery_systemC.tools.excelControl import get_excel_data
import allure

# @pytest.mark.usefixtures('xt_shop') #类级别, 自动调用autouse=True的fixture
#如果fixture有返回值的话，userfixture是不能获取到返回值的
# @pytest.mark.usefixtures('shop_init') #自动调用有autouse=True的fixture


@allure.epic("外卖项目") #参数化(yaml/excel)
@allure.feature("店铺模块")
@pytest.mark.shop #店铺有关的标签
class TestShop:
    #这个测试类里面，每一个接口都需要登陆的token,这个实例只需要操作一次
    # def setup_class(self):
    #     #所有的实例只需要登陆一次,可以使用参数化--配置文件实现
    #     self.token = Login().login(NAME_PSW, getToken=True)
    #     self.shopObject = Shop(self.token) #创建店铺实例
    #1 列出店铺


    # 强行跳过，省得去注释这些代码
    #@pytest.mark.skip(reason="这个接口没有开发好，暂时不执行自动化测试")

    #有条件跳过
    #@pytest.mark.skipif(1==1, reason="（前提没有达到，）条件为真，不执行下面的用例")


    @pytest.mark.shop_list #列出店铺的标签
    @pytest.mark.parametrize('inBody, expData',get_excel_data('我的商铺','listshopping'))
    @allure.story("店铺列出")
    @allure.title("{inBody}")#店铺列出操作，从excel接口用例读标题、描述写过来也可以,直接修改get_excel_data
    def test_shop_list(self,inBody, expData,shop_init):
        #调用业务模块代码
        res = shop_init.shop_list(inBody)

        #做断言：遇到不规范的断言
        #如果一个断言不能判断出，需要多个断言:assert后面就是一个布尔表达式
        if 'code' in res:
            assert res['code'] == expData['code']
        else:
            assert res['error'] == expData['error']


    # def test_001(self,update_shop_init):
    #     print('店铺id: ',update_shop_init[0])
    #     print('图片信息: ', update_shop_init[1])


    # 2 更新店铺
    #在执行店铺更新的接口，不仅需要登录操作，还有一些前置操作，获取id,获取图片
    #只有这个接口需要，其他接口不需要，不能放到setup_class
    #pytest--fixture--环境初始化与清除操作,添加conftest文件
   # @pytest.mark.usefixtures('update_shop_init')#写入函数名字，调用conftest里面的初始化函数

    @allure.story("店铺更新")
    @allure.title("店铺更新操作，从excel接口用例读标题、描述写过来也可以")
    @pytest.mark.shop_update #店铺列出的标签
    @pytest.mark.parametrize('inBody, expData',get_excel_data('我的商铺','updateshopping'))

    def test_shop_update(self,inBody, expData, update_shop_init, shop_init):
        #调用业务模块代码
        res = shop_init.shop_update(inBody,update_shop_init[0],update_shop_init[1])

        #做断言：遇到不规范的断言
        #如果一个断言不能判断出，需要多个断言:assert后面就是一个布尔表达式
        if 'code' in res:
            assert res['code'] == expData['code']
        else:
            assert res['error'] == expData['error']

if __name__ == '__main__':

    # pytest.main(['test_shop.py','-m', 'shop_update','--alluredir','../report/tmp'])
    # pytest.main(['test_shop.py', '--alluredir', '../report/tmp'])
    # os.system('allure serve ../report/tmp')

    pytest.main(['test_shop.py', '-s', '--alluredir', '../report/tmp'])
    os.system('allure generate ../report/tmp -o ../report/report --clean')




    #2 更新店铺