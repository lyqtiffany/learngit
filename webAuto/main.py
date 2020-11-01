from testcases import testcase1
from util import util
from selenium import webdriver
from time import sleep
from testcases.basic.test_user_register import TestUserRegister
from testcases.basic.test_user_login import TestUserLogin
from testcases.basic.test_admin_login import TestAdminLogin
from testcases.basic.test_write_article import TestWriteArticle

if __name__ == '__main__':
    # testcase1.test1()
    # testcase1.testXY()
    # testcase1.yanzheng()
    # testcase1.getStringYanZheng()
    # util.get_code()
    # print(util.gen_random_str())

    # driver = webdriver.Chrome()
    # driver.get('http://jpress.io/user/register')
    # sleep(3)
    # driver.maximize_window()
    # print(util.get_code(driver, 'captchaimg'))  #获取图片验证码

    # case01 = TestUserRegister()   #用户注册
    # case01.test_register_code_error()
    # case01.test_register_pass()

    login = TestUserLogin() #测试用户登陆
    # # case02.test_user_login_username_error()
    login.test_user_login_ok() #两个一次测试需要先清空第一个case数据 clear()

    # case03 = TestAdminLogin()
    # case03.test_admin_login_username_error()  #测试管理员登陆
    # case03.test_admin_login_ok()

    sleep(2)
    case04 = TestWriteArticle(login)  #文章投稿， 输入文章内容处，定位有问题，需要继续调试解决
    # case04.test_add_article_error()
    case04.test_add_article_pass()  #添加文章
    case04.test_delete_article_pass() #删除文章


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


'''
为测试项目添加测试报告
HTMLTestRunner_PY3, 在github里面搜索下载zip
    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'ExampleReport.html'

    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTest))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase1))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase2))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase3))

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)


'''



