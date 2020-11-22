from day7XinBao.pages.basePage import BasePage
from day7XinBao.utils.mysettings import URL
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class AttendanceManagementPage(BasePage):
    def __init__(self,path='/checkwork/manage'):
        super(AttendanceManagementPage,self).__init__()
        self.url=URL+path

        # 打卡按钮
        self.Clock_button=(By.CSS_SELECTOR,".blog-post>.text-center > a")

        # 打卡状态下拉框
        self.Punch_status_dropdown_box=(By.CSS_SELECTOR,'form.searchform>select[name="type"]')

        # 打卡状态搜索按钮
        self.Punch_status_search_button=(By.CSS_SELECTOR,'form.searchform > select+button')

        # 考勤表
        self.attendance_sheet=(By.CSS_SELECTOR,'table')

        # 匹配考勤表的每一行考勤
        self.Single_attendance=(By.CSS_SELECTOR,'tbody>tr')

        # 匹配考勤表的每一个日期
        self.Date_line=(By.CSS_SELECTOR,'tbody>tr>td:nth-child(1)')

        # 匹配考勤表的每一个打卡
        self.Punch_line=(By.CSS_SELECTOR,'tbody>tr>td:nth-child(2)')

        # 匹配考勤表的每一个状态
        self.A_single_status=(By.CSS_SELECTOR,'tbody>tr>td:nth-child(3)')

        # 匹配考勤表的每一个ip
        self.Single_IP=(By.CSS_SELECTOR,'tbody>tr>td:nth-child(4)')

    """
    打开网址
    """
    def to_page(self):
        self.driver.get(self.url)

    """
    打卡按钮
    """
    def Clock_button_Box(self):
        return self.driver.get_element(self.Clock_button)

    """
    打卡状态下拉框
    """
    def Punch_status_Box(self):
        return self.driver.get_element(self.Punch_status_search_button)

    """
    打卡状态搜索按钮
    """
    def Punch_status_search_Box(self):
        return self.driver.get_element(self.Punch_status_search_button)

    """
    考勤表
    """
    def attendance_sheet_Box(self):
        return self.driver.get_element(self.attendance_sheet)

    """
    匹配考勤表的每一行考勤
    """
    def Single_attendance_Box(self):
        return self.driver.get_elements(self.Single_attendance)

    """
    匹配考勤表的每一个日期
    """
    def Date_line_Box(self):
        return self.driver.get_elements(self.Date_line)

    """
    匹配考勤表的每一个打卡
    """
    def Punch_line_Box(self):
        return self.driver.get_elements(self.Punch_line)

    """
    匹配考勤表的每一个状态
    """
    def A_single_status_Box(self):
        return self.driver.get_elements(self.A_single_status)

    """
    匹配考勤表的每一个ip
    """
    def Single_IP_Box(self):
        return self.driver.get_elements(self.Single_IP)

class AttendanceManagementPageAction(AttendanceManagementPage):

    def punchClock(self):
        """
        点击打开按钮
        :return:
        """
        self.Clock_button_Box().click()

    def signStatusSearch(self,status):
        """
        按打卡状态搜索考勤
        :return:
        """
        Select(self.Punch_status_Box()).select_by_visible_text(status)
        """
        点击搜索按钮
        """
        self.Punch_status_search_Box().click()
AMPA=AttendanceManagementPageAction()
AMPA.to_page()
AMPA.punchClock()
AMPA.signStatusSearch('早退')