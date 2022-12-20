"""登录页面"""
from selenium.webdriver.common.by import By

from litemall.page_objects.base_page import BasePage
from litemall.utils.log_utils import logger


class LoginPage(BasePage):
    """登录页面：用户登录"""
    _BASE_URL = "https://litemall.hogwarts.ceshiren.com/"

    __INPUT_USERNAME = (By.CSS_SELECTOR, "[name='username']")
    __INPUT_PASSWORD = (By.CSS_SELECTOR, "[name='password']")
    __BTN_LOGIN = (By.CSS_SELECTOR, ".el-button--primary")

    def login(self):
        # 访问登录页
        logger.info("登录页面：用户登录")
        # 输入“用户名”
        self.do_send_keys("hogwarts", self.__INPUT_USERNAME)
        # 输入“密码”
        self.do_send_keys("test12345", self.__INPUT_PASSWORD)
        # 点击“登录”按钮
        self.do_find(self.__BTN_LOGIN).click()

        # ==》首页
        from litemall.page_objects.home_page import HomePage
        return HomePage(self.driver)
