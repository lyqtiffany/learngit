import pytest
import allure
import os


allure.feature('登陆模块的一级标签')
class TestLogin:    #登录模块的测试类
    #很多操作是有前置条件的，比如买东西必须先登录。
    def setup_class(self):
        print('在这个类执行之前我先执行')


    @pytest.mark.parametrize('a,b',[(1,2),(3,4),(5,6)])
    @allure.story('登陆模块第二个用例的二级标签')
    @allure.title('登录模块第二个case的标题')
    def test_case02(self,a,b):
        print('---hahah---')
        assert 1+a==b

    def teardown_class(self):
        print('测试类的环境清除')

if __name__ == '__main__':

    pytest.main(['test_func.py','-s','--alluredir','../report/tmp'])  #加上参数s就可以显示打印信息了
    os.system('allure generate ../report/tmp -o ../report/report --clean')



