from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 无头模式，可选
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver