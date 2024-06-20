from selenium import webdriver
from Pages.home_page import Homepage


class TestHomePage:
    def test_search(self):
        self.driver = webdriver.Edge()
        Homepage(self.driver).search("联机")
