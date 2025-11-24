from selenium.webdriver.common.by import By
from pages.base_page import Basepage
import time

class Blogpage(Basepage):
    """日志页面对象"""

    CLASSIFICATION = (By.XPATH, "//select[@name='category']")
    TITLE = (By.XPATH, "//input[@id='title']")
    IFRAMEONE = (By.XPATH, "//iframe[@class='ke-iframe']")
    IFBODY = (By.XPATH, "//body[@class='ke-content']")
    FILE = (By.XPATH, "//input[@name='myfile']")
    PRIVACY = (By.XPATH, "//select[@name='privacy']")
    COMMENT = (By.XPATH, "//select[@id='cc']")
    PUBLICATION = (By.XPATH, "//input[@value='发 表']")

    def __init__(self, browser):
        """初始化基本信息"""
        super().__init__(browser)

    def open_blog_page(self):
        """打开日志页面"""
        # 打开浏览器地址（前提要登录）
        self.browser.get(f"{self.base_url}/apps/blog/index.php?s=/Index/addBlog")

    def click_my_blog(self):
        """点击我的日志标签"""
        self.click_element()

    def click_everyone_blog(self):
        """点击大家的日志标签"""

    def click_friend_blog(self):
        """点击好友的日志标签"""

    def select_types(self, value):
        """选择分类"""
        if self.is_option_available(self.CLASSIFICATION, value):
            self.select_element_value(self.CLASSIFICATION, value)
        else:
            print(f"分类无法查到{value}")

    def input_title(self, title):
        """输入标题"""
        self.input_element(self.TITLE, title)

    def input_content(self, text, index=0):
        """输入内容"""
        try:
            self.switch_to_frame(index)
            time.sleep(3)
            body_elem = self.wait_element_click(self.IFBODY)
            body_elem.clear()
            body_elem.send_keys(text)
        except Exception as e2:
            print(f"备用方案也失败: {e2}")
            raise
        finally:
            self.switch_exit_frame()

    def upload_file(self):
        """上传附件"""

    def select_permission(self):
        """设置权限"""

    def select_common(self):
        """设置评论权限"""

    def publication(self):
        """发表日志"""


if __name__ == '__main__':
    from pages.login_page import Loginpage
    from selenium import webdriver

    dr = webdriver.Firefox()
    # 先登录
    login_page = Loginpage(dr)
    login_page.open_login_page()
    login_page.input_email("jwy@qq.com")
    login_page.input_passwd("123456")
    login_page.click_login()

    # 登录后直接创建博客页面对象并操作
    blog_page = Blogpage(dr)
    blog_page.open_blog_page()
    blog_page.input_title(title="shabi温帅")
    blog_page.input_content(text="123", index=0)
