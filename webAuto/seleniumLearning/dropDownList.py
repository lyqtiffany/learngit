from selenium import  webdriver
from time import sleep
import os

from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/forms2.html'
        print(file_path)
        self.driver.get(file_path)

    def test_dropdownlist(self):
        se = self.driver.find_element_by_id('province') #下拉列表默认选择第一个
        select = Select(se)
        # select.select_by_index(2) #select 3rd item
        #
        # sleep(2)
        # select.select_by_value('bj')  #html 里面的value对应的值
        # sleep(2)
        #
        # select.select_by_visible_text('Tianjing') #页面上看到的文本

        # for i in range(3):
        #     select.select_by_index(i)
        #     sleep(1)
        #
        # select.deselect_all() #反选所有
        # sleep(1)

        for option in select.options: #所有选项,还有first_selected_options, all_selected_options
            print(option.text)


    def test_checkbox(self):
        swimming = self.driver.find_element_by_name('swimming')
        if not swimming.is_selected():
            swimming.click()

        reading = self.driver.find_element_by_name('reading')
        if not reading.is_selected():
            reading.click()

        sleep(5)
        swimming.click()
        sleep(3)

        self.driver.quit()
    def test_radio(self):
        lst = self.driver.find_elements_by_name('gender')
        lst[0].click()
        lst[1].click()

if __name__ == '__main__':
    case = TestCase()
    # case.test_checkbox()
    # case.test_radio()
    case.test_dropdownlist()