# =================显示等待优化方案2：自定义显式等待
from litemall.utils.log_utils import logger


def click_exception(by, element, max_attempts=5):
    def _inner(driver):  # 定义了一个内函数
        # 多次点击按钮
        actual_attempts = 0  # 实际点击次数
        while actual_attempts <= max_attempts:
            # 进行点击操作
            actual_attempts += 1  # 每次循环，实际点击次数加1
            try:
                # 如果点击过程报错，则直接执行except逻辑，并且继续循环
                # 如果没有报错，则直接return，循环结束
                driver.find_element(by, element).click()
                return True
            except Exception:
                logger.debug("点击的时候出现了一次异常")
        # 当实际点击次数大于最大点击次数时，结束循环并抛出异常
        raise Exception("超出了最大点击次数")

    # return _inner() 错误写法
    return _inner
