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

class MyTestCase03(unittest.TestCase):

    def test01(self):  #必须用test起头
        print('test01')

    def test02(self):
        print('test02')

class MyTestCase04(unittest.TestCase):
    def test03(self):
        print('test03')

    def test04(self):
        print('test04')


if __name__ == '__main__': #执行时需要加载器，测试套件，运行器
    loader = unittest.TestLoader() #加载器加载测试用例
    suite = unittest.TestSuite() #测试套件

    # 方法一 通过测试用例名字加载到套件
    suite.addTest(loader.loadTestsFromTestCase(MyTestCase03))
    suite.addTest(loader.loadTestsFromTestCase(MyTestCase04))

    # 方法二 通过测试用例模板去加载到套件
    # suite.addTest(loader.loadTestsFromModule(MyTestCase03))
    # suite.addTest(loader.loadTestsFromModule(MyTestCase04))

    #方法三 #推荐  通过路径加载当前文件所在路径下的
    # import os
    # path = os.path.dirname(os.path.abspath(__file__))
    # suite.addTest(loader.discover(path))

    #运行器
    runner = unittest.TextTestRunner() #运行器
    runner.run(suite)

    #方法四：逐条加载测试用例 low
    # case1 = MyTestCase03("test01")
    # case2 = MyTestCase03("test02")
    # suite.addTest(case1)
    # suite.addTest(case2)



#setup    tear down分为类方法和实例方法
# 整个类，它运行一次，
# 实例方法，每次运行实例方法的时候，它都会运行
# 执行顺序：setupClass-setUp-testA-tearDown-setUp-testB-tearDown-tearDownclass 0-9 A-z a-z
#断言方法，assertEqual, assertIn....


#加载测试用例的4种方法
# #方法一 实例化
# suite = unittest.TestSuite()
# loader = unittest.TestLoader()

# suite.addTest(loader.loadTestsFromTestCase(MyTest1))
# suite.addTest(loader.loadTestsFromTestCase(MyTest2))

#方法二 通过测试用例模板去加载
#suite.addTest(loader.loadTestsFromModule(MyTest1))
#suite.addTest(loader.loadTestsFromModule(MyTest2))

#方法三  #推荐   # 通过路径加载当前文件所在路径下的 #推荐
# import os
# path = os.path.dirname(os.path.abspath(__file__))
# suite.addTest(loader.discover(path))

#方法四，逐条加载测试用例，麻烦
#case1 = MyTest1("test1")
#case2 = MyTest1("test2")
#suite.addTest(case1)
#suite.addTest(case2)

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