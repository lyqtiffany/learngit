#selenium等待条件
# title_is 判断title是否出现
# title_contains 判断title页面标题是否包含某些字符
# presence_of_element_located 判断某个元素是否被加载到了dom树里，但是并不代表这个元素可见
# url_contains 判断当前url是否包含某个url
# url_matches 判断当前url是否符合某种格式
# url_to_be 判断当前url是否出现
# url_changes 判断当前url是否已经发生了变化
# visibility_of_element_located 判断某个元素是否被添加到了dom树里，且宽高都大于0
# visibility_of 判断看某个元素是否可见
# presence_of_all_elements_located 判断至少有一个元素存在于dom树中，返回所有定位到的元素
# visibility_of_any_elements_located 判断至少有一个元素在页面中可见
# visibility_of_all_elements_located 判断是否所有元素都在页面中可见
# text_to_be_present_in_element 判断指定的元素中是否包含了预期的字符串
# text_to_be_present_in_element_value 判断指定的元素属性值中是否包含了预期的字符串
# frame_to_be_available_and_switch_to_it 判断iframe是否可以switch进去
# invisibility_of_element_located 判断某个元素是否在dom中不可见
# element_to_be_clickable 判断某个元素是否可见并且是enable的，也就是说是是否可以点击
# staleness_of 等待某个元素从dom中删除
# element_to_be_selected 判断某个元素是否被选中了，一般用于下拉列表中
# element_located_to_be_selected 与上面的意思一样，只不过上面实例化的时候传入的是元素对象，这个传入的是定位
# element_selection_state_to_be 判断某个元素的选中状态是否符合预期
# element_located_selection_state_to_be 与上面一样，只不过传值不同而已
# number_of_windows_to_be 判断当前窗口数是否等于预期
# new_window_is_opened 判断是否有窗口增加
# alert_is_present 判断页面是否有弹窗

from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = 'file:///' + os.path.abspath('test_wait.html')
        self.driver.get(path)

    def test(self):
        self.driver.find_element_by_id('btn').click()
        #显式等待
        wait = WebDriverWait(self.driver,3)
        wait.until(EC.text_to_be_present_in_element((By.ID,'id2'), 'id 2'))
        print(self.driver.find_element_by_id('id2').text)
        print('ok')

if __name__ == '__main__':
    case = TestCase()
    case.test()