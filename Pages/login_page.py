import time

from selenium.webdriver.common.by import By

from Locators.LoginLocators.login_locators import LoginLocators as loc
from Common.plugs.basepage import BasePage


class Loginpage(BasePage):
    def __init__(self, driver):
        self.driver = driver

        self.url = 'https://www.mcmod.cn/login/'
        self.username = '2521865687@qq.com'
        self.password = 's15825914922'

    def login(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # 页面登录操作
        self.driver.find_element(by=By.XPATH, value=loc.login_username_loc).send_keys(self.username)
        self.driver.find_element(by=By.XPATH, value=loc.login_password_loc).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=loc.login_button_loc).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=loc.home_page_loc).click()
        time.sleep(3)
        # self.input_element(loc.login_username_loc, self.username)
        # self.input_element(loc.login_password_loc, self.password)
        # self.click_element(loc.login_button_loc)
        # time.sleep(3)
        # self.click_element(loc.home_page_loc)
        # time.sleep(3)


