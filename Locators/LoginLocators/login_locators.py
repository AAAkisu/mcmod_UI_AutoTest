from selenium.webdriver.common.by import By


class LoginLocators:
    login_username_loc = (By.XPATH, '//*[@id="login-username"]')
    login_password_loc = (By.XPATH, '//*[@id="login-password"]')
    login_button_loc = (By.XPATH, '//*[@id="login-action-btn"]')
    home_page_loc = (By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[1]/a')
