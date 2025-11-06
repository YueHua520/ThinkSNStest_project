from selenium.webdriver.common.by import By
from pages.base_page import Basepage


class Loginpage(Basepage):
    EMAIL = (By.XPATH, "//input[@name='email']")
    PASSWORD = (By.XPATH, "//input[@name='passwd']")
    COMMIT = (By.XPATH, "//input[@value='登 录' or @value='确 定']")

    def __init__(self, browser):
        """初始化"""
        super().__init__(browser)

    def open_login_page(self):
        """打开登录页面"""
        self.browser.get(f"{self.base_url}/index.php")

    def input_email(self, email):
        """输入邮箱"""
        self.input_element(self.EMAIL, email)

    def input_passwd(self, passwd):
        """输入密码"""
        self.input_element(self.PASSWORD, passwd)

    def click_login(self):
        """点击登录"""
        self.click_element(self.COMMIT)
