from selenium.webdriver.common.by import By
from pages.base_page import Basepage


class RegisterPage(Basepage):
    """注册页面"""
    EMAIL = (By.XPATH, "//input[@name='email']")
    PASSWD = (By.XPATH, "//input[@name='passwd']")
    REPASSWD = (By.XPATH, "//input[@name='repasswd']")
    NAME = (By.XPATH, "//input[@name='name']")
    SEX = (By.XPATH, "//label[contains(text(), '{}')]")
    YEAR = (By.XPATH, "//select[@name='birthday_year']")
    MONTH = (By.XPATH, "//select[@name='birthday_month']")
    DAY = (By.XPATH, "//select[@name='birthday_day']")
    LOCATION = (By.XPATH, "//input[@class='btn_b' and @value='选择地区']")
    PROVINCE = (By.XPATH, "//a[contains(@onclick, '{}')]")
    CITY = (By.XPATH, "//a[contains(@onclick, '{}')]")
    SUBMIT = "save();"
    PRIVACY = (By.XPATH, "//select[@name='baseinfoprivacy']")
    AGREE = (By.XPATH, "//input[@value='同意条款 立即注册']")

    def __init__(self, browser):
        super().__init__(browser)

    def open_register_page(self):
        self.open_url(f"{self.base_url}?s=/Index/reg")

    def input_email(self, email):
        self.clear_text(self.EMAIL)
        self.input_element(self.EMAIL, email)

    def input_password(self, password):
        self.clear_text(self.PASSWD)
        self.clear_text(self.REPASSWD)
        self.input_element(self.PASSWD, password)
        self.input_element(self.REPASSWD, password)

    def input_name(self, name):
        self.clear_text(self.NAME)
        self.input_element(self.NAME, name)

    def select_sex(self, sex_value):
        # 动态生成，运用format函数插入数据
        locator = (self.SEX[0], self.SEX[1].format(sex_value))
        self.click_element(locator)

    def select_location(self, province, city):
        # 选择地区
        self.click_element(self.LOCATION)
        # 选择省会
        location_province = (self.PROVINCE[0], self.PROVINCE[1].format(province))
        province_element = self.wait_element_visible(location_province)
        self.js_click(province_element)
        # 选择城市
        location_city = (self.CITY[0], self.CITY[1].format(city))
        city_element = self.wait_element_visible(location_city)
        self.js_click(city_element)

        # 提交(唯一标识符)java提交
        self.browser.execute_script(self.SUBMIT)

    def finish_register(self):
        self.click_element(self.AGREE)

    # def select_birthday(self, year, month, day):
    #     """select的选择年月日"""
    #     self.select_element_text(self.YEAR, year)
    #     self.select_element_text(self.MONTH, month)
    #     self.select_element_text(self.DAY, day)

    def select_birthday(self, year, month, day):
        """安全选择生日，只选择存在的选项"""
        # 检查并选择年份
        if self.is_option_available(self.YEAR, year):
            self.select_element_text(self.YEAR, year)
        else:
            print(f"年份选项不可用: {year}")
        # 检查并选择月份
        if self.is_option_available(self.MONTH, month):
            self.select_element_text(self.MONTH, month)
        else:
            print(f"月份选项不可用: {month}")
        # 检查并选择日期
        if self.is_option_available(self.DAY, day):
            self.select_element_text(self.DAY, day)
        else:
            print(f"日期选项不可用: {day}")

    # def select_privacy(self, privacy_value):
    #     self.select_element_value(self.PRIVACY, privacy_value)
    def select_privacy(self, privacy_value):
        if self.is_option_available(self.PRIVACY, privacy_value):
            self.select_element_value(self.PRIVACY, privacy_value)
        else:
            print(f"权限无法查到{privacy_value}")
