import ddt
import unittest
import time
import os
import sys

current_file = os.path.abspath(__file__)
print(f"当前文件路径: {current_file}")
# 获取当前文件所在目录（testcases目录）
current_dir = os.path.dirname(current_file)
print(f"当前目录: {current_dir}")
# 获取项目根目录（Thinktest目录）
project_root = os.path.dirname(current_dir)
print(f"项目根目录: {project_root}")
# 将项目根目录添加到Python路径中，这样Python就能找到pages模块了
sys.path.insert(0, project_root)
print("已添加项目根目录到Python路径")
# 现在可以导入项目模块了

from XTestRunner import HTMLTestRunner
from selenium import webdriver
from pages import Homepage
from pages import RegisterPage


@ddt.ddt
class Testregitercase(unittest.TestCase):
    """测试注册功能"""

    @classmethod
    def setUpClass(cls):
        """整个测试类执行一次"""
        # 初始化浏览器
        cls.browser = webdriver.Firefox()
        # 初始化页面对象
        cls.register_page = RegisterPage(cls.browser)
        cls.home_page = Homepage(cls.browser)

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器,用hasattr函数检查类中是否存在元素，安全报错机制
        if hasattr(cls, "browser") and cls.browser:
            cls.browser.quit()

    def setUp(self):
        """每个测试前执行"""
        # 回到注册界面
        self.register_page.open_register_page()

    def tearDown(self):
        """每个用例后执行"""
        # 如果注册成功，需要退出登录以便进行下一个测试
        try:
            current_url = self.browser.current_url
            if "/Index/reg" in current_url:
                return
            elif "/Info/face" in current_url:
                self.home_page.click_exit_account()
            elif "/Home" in current_url:
                self.home_page.click_exit_account()
            else:
                self.register_page.open_register_page()
        except Exception:
            print("teardown异常")

    @ddt.file_data(os.path.join(project_root, "datas", "register", "registerdata.yaml"))
    def test_registration(self, name, data, validations):
        """测试注册数据"""
        self._testMethodDoc = f"注册测试- {name} "
        # 执行注册流程
        self.register_page.input_email(data["email"])
        self.register_page.input_password(data["passwd"])
        self.register_page.input_name(data["name"])
        self.register_page.select_sex(data["sex_value"])
        self.register_page.select_birthday(
            data["year_select"],
            data["month_select"],
            data["day_select"]
        )
        if data["location_one"] is not None:
            self.register_page.select_location(
                data["location_one"],
                data["location_two"]
            )
        self.register_page.select_privacy(data["pri_select"])
        self.register_page.finish_register()
        # 等待页面跳转
        time.sleep(2)
        # 获取当前页面的url
        current_suf = self.browser.current_url
        # 进行返回值断言
        for validation in validations:
            # 循环遍历找到多层断言的键，读取需要断言的内容，此处type是url类型
            if validation["type"] == "url_contains":
                expected_suf = validation["expected"]
                self.assertIn(
                    expected_suf,
                    current_suf,
                    f"URL不包含预期部分: 期望 '{expected_suf}' 包含在 '{current_suf}' 中"
                )


if __name__ == "__main__":
    suit = unittest.TestLoader().loadTestsFromTestCase(Testregitercase)
    # 拼接路径
    report_path = os.path.join(
        project_root, "reports", "html_reports", f"report_{time.strftime('%Y%m%d%H%M%S')}.html")
    with open(report_path, "wb") as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title="验证注册账号的报告",
            tester="月华",
            description="等价类边界值划分的覆盖各种注册类型的大量账号",
            language="zh-CN",
            rerun=0
        )
        runner.run(suit)
