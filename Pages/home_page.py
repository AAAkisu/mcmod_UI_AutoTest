from selenium.webdriver.common.by import By
import time


class Homepage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.mcmod.cn/'

    # def into_login(self):
    #     self.driver.get(self.url)
    #     self.driver.implicitly_wait(10)
    #     self.driver.maximize_window()
    #     time.sleep(3)
    #
    #     # 页面元素定位
    #     login_button_Path = '/html/body/div[1]/div/div[3]/ul/li/a'
    #
    #     # 页面登录操作
    #     self.driver.find_element(by=By.XPATH, value=login_button_Path).click()
    #     time.sleep(5)
    #
    #     # 跳转到新的想要跳转的页面
    #     for handle in self.driver.window_handles:
    #         # 切换到新的页面
    #         self.driver.switch_to.window(handle)
    #         if self.driver.current_url == "https://www.mcmod.cn/":
    #             break
    #
    #     # 断言
    #     assert self.driver.current_url == "https://www.mcmod.cn/"
    #
    #     time.sleep(3)
    #     self.driver.close()

    def search(self, search_text):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # 页面元素定位
        search_open = '/html/body/div[1]/div/div[3]/ul/div'
        search_input = '/html/body/div[1]/div/div[2]/form/input[1]'
        search_btn = '/html/body/div[1]/div/div[2]/form/input[2]'

        # 页面搜索操作
        self.driver.find_element(by=By.XPATH, value=search_open).click()
        self.driver.find_element(by=By.XPATH, value=search_input).send_keys(search_text)
        self.driver.find_element(by=By.XPATH, value=search_btn).click()
        time.sleep(1)

        # 跳转到新的想要跳转的页面
        for handle in self.driver.window_handles:
            # 切换到新的页面
            self.driver.switch_to.window(handle)

        # 断言
        assert "MC百科搜索" in self.driver.page_source

        time.sleep(1)
        self.driver.close()
