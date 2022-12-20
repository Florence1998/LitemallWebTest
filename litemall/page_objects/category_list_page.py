"""类目列表页面"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from litemall.page_objects.base_page import BasePage
from litemall.utils.log_utils import logger


class CategoryListPage(BasePage):
    """类目列表页面：点击添加"""
    __BTN_ADD = (By.XPATH, "//*[text()='添加']")
    __MSG_ADD_OPERATION = (By.XPATH, "//p[contains(text(),'创建成功')]")
    __MSG_DELETE_OPERATION = (By.XPATH, "//p[contains(text(),'删除成功')]")

    def click_add(self):
        logger.info("类目列表页面：点击添加")
        # 点击“添加”按钮
        self.do_find(self.__BTN_ADD).click()

        # ==》创建类目页面
        from litemall.page_objects.category_create_page import CategoryCreatePage
        return CategoryCreatePage(self.driver)

    """类目列表页面：获取创建结果"""

    def get_operate_result(self):
        logger.info("获取冒泡消息文本（创建结果）")
        # 获取冒泡消息文本
        element = self.wait_element_until_visible(self.__MSG_ADD_OPERATION)
        msg = element.text
        logger.info(f"冒泡信息是：{msg}")
        # ==》返回消息文本
        return msg

    """类目列表页面：点击删除"""

    def delete_category(self, category_name):
        logger.info("类目列表页面：点击删除")
        # 对指定类目进行删除
        self.do_find(By.XPATH, f"//*[text()='{category_name}']/../..//*[text()='删除']").click()

        # ==》跳转到当前页面
        return CategoryListPage(self.driver)

    """类目列表页面：获取删除结果"""

    def get_delete_result(self):
        logger.info("获取冒泡消息文本（删除结果）")
        # 获取冒泡消息文本
        element = self.wait_element_until_visible(self.__MSG_DELETE_OPERATION)
        msg = element.text
        logger.info(f"冒泡信息是：{msg}")

        # ==》返回消息文本
        return msg
