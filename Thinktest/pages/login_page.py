from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Loginpage:
    def __init__(self, browser):
        """初始化地址"""
        self.browser = browser
        self.login_url = "http://172.31.21.124/ThinkSNS/index.php"
        self.browser.implicitly_wait(20)

    def input_email(self, email):
        """输入邮箱"""
        email_one = WebDriverWait(self.browser, 10, 0.3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
        )
        email_one.send_keys(email)

    def input_passwd(self, passwd):
        """输入密码"""
        passwd_one = WebDriverWait(self.browser, 10, 0.3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='passwd']"))
        )
        passwd_one.send_keys(passwd)

    def click_login(self):
        """点击登录"""
        click_one = WebDriverWait(self.browser, 10, 0.3).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='登 录']"))
        )
        click_one.click()
