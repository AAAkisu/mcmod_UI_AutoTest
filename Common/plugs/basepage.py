import datetime
import os
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Common.plugs.get_config import r_config
from Common.plugs.get_log import Log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')
log_dir = r_config(conf_dir, "log", "log_path")
images_dir = r_config(conf_dir, "image", "img_path")

logger = Log(log_dir)


class BasePage:
    def __int__(self, driver):
        self.driver = driver

    def save_picture(self):
        pass

    # 等待页面元素可见
    def wait_eleVisible(self, locator, doc=''):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logger.info('{0},等待页面元素:{1}:可见，共耗时{2}s '.format(doc, locator, wait_time))
        except:
            logger.info('{0},等待页面元素:{1} 失败！！！'.format(doc, locator))
            self.save_pictuer(doc)

    # 查找页面元素
    def get_element(self, locator, doc=''):
        print(locator)
        logger.info('{0},查找页面元素:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.driver.find_element(*locator)
        except:
            logger.info('{0},查找页面元素:{1} 失败！！！'.format(doc, locator))
            raise

    # 点击页面元素
    def click_element(self, locator, doc=''):
        logger.info('{0},点击页面元素:{1}'.format(doc, locator))
        try:
            self.get_element(locator, doc).click()
        except:
            logger.info('点击页面元素:{0},失败！！！'.format(locator))
            raise

    # 输入操作
    def input_element(self, locator, key, doc=''):
        logger.info('{0},页面元素:{1} 输入值 {2}'.format(doc, locator, key))
        try:
            self.wait_eleVisible(locator, doc)
            self.get_element(locator, doc).send_keys(key)
        except:
            logger.info('{0},页面元素输入失败！！！'.format(doc))
            raise

    # 获取文本
    def get_element_text(self, locator, doc=''):
        logger.info('{0},获取页面元素:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.get_element(locator, doc).text
        except:
            logger.info('{0},页面元素的文本获取失败！！！'.format(doc))
            raise

    # 获取页面元素属性
    def get_element_attribute(self, attr, locator, doc=''):
        logger.info('{0},获取页面元素属性:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.get_element(locator, doc).get_attribute(attr)
        except:
            logger.info('{0},页面元素的属性获取 失败！！！'.format(doc))
            raise

    # 查找页面元素
    def get_element(self, locator, doc=''):
        print(locator)
        logger.info('{0},查找页面元素:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.driver.find_element(*locator)
        except:
            logger.info('{0},查找页面元素:{1} 失败！！！'.format(doc, locator))
            raise

    # 点击页面元素
    def click_element(self, locator, doc=''):
        logger.info('{0},点击页面元素:{1}'.format(doc, locator))
        try:
            self.get_element(locator, doc).click()
        except:
            logger.info('点击页面元素:{0},失败！！！'.format(locator))
            raise

    # 输入操作
    def input_element(self, locator, key, doc=''):
        logger.info('{0},页面元素:{1} 输入值 {2}'.format(doc, locator, key))
        try:
            self.wait_eleVisible(locator, doc)
            self.get_element(locator, doc).send_keys(key)
        except:
            logger.info('{0},页面元素输入失败！！！'.format(doc))
            raise

    # 获取文本
    def get_element_text(self, locator, doc=''):
        logger.info('{0},获取页面元素:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.get_element(locator, doc).text
        except:
            logger.info('{0},页面元素的文本获取失败！！！'.format(doc))
            raise

    # 获取页面元素属性
    def get_element_attribute(self, attr, locator, doc=''):
        logger.info('{0},获取页面元素属性:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.get_element(locator, doc).get_attribute(attr)
        except:
            logger.info('{0},页面元素的属性获取 失败！！！'.format(doc))
            raise

    # alter 处理
    def alter_action(self):
        pass

    # iframe 切换
    def switch_iframe(self):
        pass

    # windows 切换
    def switch_window(self):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理
