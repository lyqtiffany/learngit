from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep


def get_element(driver, *loc): #*表示可以传任意多个参数
    e = driver.find_element(*loc)
    return e

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    sleep(1)

    loc = (By.ID, 'kw')
    loc2 = (By.ID, 'su')
    get_element(driver, *loc).send_keys('selenium') #这里为什么要用*,表示参数要解包？
    #get_element(driver, By.ID, 'kw').send_keys('selenium')
    get_element(driver, *loc2).click()