#                   _oo0oo_
#                  o8888888o
#                  88' . '88
#                  (| -_- |)
#                  0\  =  /0
#                ___/`---'\___
#              .' \\|     |// '.
#             / \\|||  :  |||// \
#            / _||||| -:- |||||_ \
#           |   | \\\  -  /// |   |
#           | \_|  ''\---/''  |_/ |
#           \ .-\___  '-'  ___/-. /
#         ___'. .'  /--.--\  `. .'___
#       .'' '< `.___\_<|>_/___.' >'  ''.
#     | | : `- \`.;`\ _ /`;.`/ - ` : | |
#     \  \ `_.   \_ __\ /__ _/   .-` /  /
# =====`-.____`.___ \_____/___.-`___.-'=====
#                   `=---='
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#           菩提本无树，明镜亦非台
#           本来无BUG，何必常修改
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


class Basepage:
    """基础方法类"""

    def __init__(self, browser):
        """初始化同页面浏览器，设置主地址"""
        self.browser = browser
        self.base_url = "http://172.31.21.98/ThinkSNS"
        # self.browser.implicitly_wait(30)

    def open_url(self, url):
        """通用打开网页方法"""
        self.browser.get(url)
        self.browser.maximize_window()

    def wait_element_visible(self, locator, timeout=10, time_interval=0.3):
        """等待元素可见方法"""
        try:
            elem = WebDriverWait(self.browser, timeout, time_interval).until(
                EC.presence_of_element_located(locator)
            )
            return elem
        except TimeoutException:
            raise Exception(f"等待元素存在超时！定位器：{locator}")

    def wait_element_click(self, locator, timeout=10, time_interval=0.3):
        """等待元素可点击方法"""
        try:
            elem = WebDriverWait(self.browser, timeout, time_interval).until(
                EC.element_to_be_clickable(locator)
            )
            return elem
        except TimeoutException:
            raise Exception(f"等待元素可点击超时！定位器：{locator}")

    def clear_text(self, locator):
        """文本清空方法"""
        elem = self.wait_element_visible(locator)
        elem.clear()

    def click_element(self, locator):
        """通用点击方法"""
        elem = self.wait_element_click(locator)
        elem.click()

    def js_click(self, element):
        """java点击方法"""
        self.browser.execute_script("arguments[0].click();", element)

    def input_element(self, locator, text):
        """通用输入方法"""
        elem = self.wait_element_visible(locator)
        elem.send_keys(text)

    def select_element_text(self, locator, text):
        """下拉框文本选择方法"""
        elem = Select(self.wait_element_visible(locator))
        elem.select_by_visible_text(text)

    def select_element_value(self, locator, value):
        """下拉框值选择方法"""
        elem = Select(self.wait_element_visible(locator))
        elem.select_by_value(value)

    def select_element_index(self, locator, index):
        """下拉框索引选择方法"""
        elem = Select(self.wait_element_visible(locator))
        elem.select_by_index(index)

    def is_option_available(self, locator, option_text):
        """优先判断元素是否存在"""
        try:
            select = Select(self.wait_element_visible(locator))
            options = [option.text for option in select.options]
            return option_text in options
        except Exception:
            return False

    def switch_to_frame(self, locator):
        """跳转至frame"""
        elem = self.wait_element_visible(locator)
        self.browser.switch_to.frame(elem)

    def switch_exit_frame(self):
        """退出frame,到主结构"""
        self.browser.switch_to.default_content()

    def switch_before_frame(self):
        """切换至上一层frame"""
        self.browser.switch_to.parent_frame()
