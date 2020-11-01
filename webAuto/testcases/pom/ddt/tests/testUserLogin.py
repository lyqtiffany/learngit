from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webAuto.testcases.pom.ddt.pages.userLoginPage import UserLoginPage
from webAuto.testcases.pom.ddt.pages.userRegisterPage import UserRegisterPage
from time import sleep
from webAuto.util import util
import pytest

class TestUserLogin(object):

    login_data = [
        ('', '123456', '账号不能为空'),
        ('lyqtiffany', 'lyq1994811', '用户中心')
    ]

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.loginPage = UserLoginPage(self.driver)
        self.loginPage.goto_login_page()

    @pytest.mark.parametrize('username, pwd, expected', login_data)
    def test_login(self, username, pwd, expected):

        self.loginPage.input_username(username)

        self.loginPage.input_pwd(pwd)
        self.loginPage.click_login_btn()
        sleep(2)

        if username == '':

            # 等待提示框
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())  # 验证弹框出现
            alert = self.driver.switch_to.alert

            sleep(3)
            assert alert.text == expected
            print(alert.text)
            alert.accept()
        else:
            WebDriverWait(self.driver, 5).until(EC.title_is(expected))  #
            sleep(3)
            assert self.driver.title == expected

            self.driver.quit()


if __name__ == '__main__':
    pytest.main(['testUserLogin.py'])




'''
jenkens

java -jar jenkins.war --httpPort=8081  #启动jenkins 默认8080,跟tomcat冲突  
获取到密码 9006be61e0ab4065bd2a8e9a7253803c   #C:\Users\Administrator\.jenkins\secrets\initialAdminPassword
打开浏览器访问localhost:8081

在jenkins中运行
先在命令行运行测试
pytest webAuto/testcases/pom/tests/testUserLogin.py

在jenins中运行
创建item
构建总选择执行batch
cd 
pytest webAuto/testcase/pom/tests/testUserLogin.py

'''