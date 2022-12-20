import pytest

from litemall.page_objects.login_page import LoginPage


class TestLitemall(object):
    # 前置动作
    def setup_class(self):
        """登录页面：用户登录"""
        self.home = LoginPage().login()

    # 后置动作
    def teardown_class(self):
        # 退出浏览器
        self.home.do_quit()

    # 添加商品类目
    @pytest.mark.parametrize("category_name", ["a", "b", "c"])
    def test_add_type(self, category_name):
        """系统首页：进入商品类目"""
        """类目列表页面：点击添加"""
        """创建类目页面：创建类目"""
        """类目列表页面：获取操作结果"""
        list_page = self.home \
            .go_to_category() \
            .click_add() \
            .create_category(category_name)
        # 断言
        res = list_page.get_operate_result()
        assert res == "创建成功"

        # 数据清理
        list_page.delete_category(category_name)

    # 删除商品类目
    @pytest.mark.parametrize("category_name", ["del_a", "del_b", "del_c"])
    def test_delete_type(self, category_name):
        """系统首页：进入商品类目"""
        """类目列表页面：点击添加"""
        """创建类目页面：创建类目"""
        """类目列表页面：点击删除"""
        """类目列表页面：获取删除结果"""
        res = self.home \
            .go_to_category() \
            .click_add() \
            .create_category(category_name) \
            .delete_category(category_name) \
            .get_delete_result()
        assert res == "删除成功"
