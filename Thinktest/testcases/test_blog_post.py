from pages import Loginpage
from selenium import webdriver
import unittest
import json


class Testblog(unittest.TestCase):
    """测试日志发送功能"""

    @classmethod
    def setUpClass(cls):
        with open("../datas/login/login.json", 'r', encoding='utf-8') as file:
            cls.all_test_logindata = json.load(file)

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.login_page = Loginpage(self.browser)

    def tearDown(self):
        self.browser.quit()

