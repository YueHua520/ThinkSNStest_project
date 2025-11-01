from selenium.webdriver.common.by import By
from pages.base_page import Basepage

class Blogpage(Basepage):
    """日志页面对象"""



    def __init__(self, browser):
        """初始化基本信息"""
        super().__init__(browser)

    def open_blog_page(self):
        """打开日志页面"""
        # 打开浏览器地址（前提要登录）
        self.browser.get(f"{self.base_url}/apps/blog/index.php?s=/Index/addBlog")

    def select_types(self):
        """选择分类"""

    def input_title(self):
        """输入标题"""

    def input_content(self):
        """输入内容"""

    def upload_file(self):
        """上传附件"""

    def select_permission(self):
        """设置权限"""

    def select_common(self):
        """设置评论权限"""

    def publication(self):
        """发表日志"""



