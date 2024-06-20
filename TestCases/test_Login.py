from selenium import webdriver
from Pages.login_page import Loginpage


class TestLogin:
    def test_login(self):
        self.driver = webdriver.Edge()
        Loginpage(self.driver).login()
