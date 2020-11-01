#unittest是python单元测试框架，类似于Junit框架
#unittest中有5个重要的概念，test fixture(初始化和收尾), test case, test suite, test runner（测试的运行）, test loader
#test case,是一个完整的测试流程，包括测试前准备环境的搭建（setup），执行测试代码（run），以及测试后环境的还原（teardown）。
#unittest单元测试的本质也在这里，一个测试用例就是一个完整的测试单元

#多个test case组成一个test suite测试套件
#test runner会执行test case/test suite中的run(result)方法

# test loader是用来加载test cae to test suite,其中有几个loadTestsFrom_()方法，就是从各个地方寻找testcase,创建他们的实例，
#然后添加add到test suite,在返回一个testsuite的实例

#test fixture, 对一个测试用例环境的搭建和销毁，是一个fixture,通过幅轧testcase的setup()和teardown（）方法来实现
#必须用test起头


import unittest
from selenium import webdriver


class MyTestCase01(unittest.TestCase):

    @classmethod  #类方法setup # 整个类，它运行一次，
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
        cls.driver.maximize_window()
        print('setUpClass...')

    def setUp(self) -> None:  #测试前打开数据库 #每运行一个test01/test02都会执行setup/teardown
        print('setup...')

    def tearDown(self) -> None:  # 测试后关闭数据库的连接 #每运行一个test01/test02都会执行setup/teardown
        print('tear down...')

    def test01(self):  #必须用test起头
        self.driver.find_element_by_id('kw').send_keys('unittest')
        print('test01...')
        # self.assertEqual(1+2, 3)

    def test02(self):
        print('test02...')
        # self.assertGreaterEqual(5, 4)

    def aaa(self): #不是test开头， 不会执行
        print('aaa...')
        # self.assertEqual(1+3, 4)
        # self.assertEqual(1, 1)
        # self.assertIn(10, [1, 2, 3])


    @classmethod  #类方法tearDown # 整个类，它运行一次，
    def tearDownClass(cls) -> None:
        print('tearDownClass...')
        cls.driver.quit()




if __name__ == '__main__':
    unittest.main() #单独运行一个类

#setup    tear down分为类方法和实例方法
# 整个类，它运行一次，
# 实例方法，每次运行实例方法的时候，它都会运行
# 执行顺序：setupClass-setUp-testA-tearDown-setUp-testB-tearDown-tearDownclass 0-9 A-z a-z
#断言方法，assertEqual, assertIn....


#加载测试用例的4种方法
# 实例化
# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
#方法一
# suite.addTest(loader.loadTestsFromTestCase(MyTest1))
# suite.addTest(loader.loadTestsFromTestCase(MyTest2))
#

#使用unittest重构测试用例
'''
拷贝上一节测试用例
继承测试用例基础unittest.TestCase
将__init__修改为setup
将assert断言，修改为unittest断言
关闭浏览器放到teardown
注意第二次要清空测试数据
注意顺序测试要加序号，比如test1, test2

'''