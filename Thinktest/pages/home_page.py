from selenium.webdriver.common.by import By
from pages.base_page import Basepage


class Homepage(Basepage):
    BLOG = (By.XPATH, "//a[@class='a14' and text()='日志']")
    GIFT = (By.XPATH, "//a[@class='a14' and text()='礼物']")
    SHARE = (By.XPATH, "//a[@class='a14' and text()='分享']")
    PHOTO = (By.XPATH, "//a[@class='a14' and text()='相册']")
    MOOD = (By.XPATH, "//a[@class='a14' and text()='心情']")
    VOTING = (By.XPATH, "//a[@class='a14' and text()='投票']")
    GROUP = (By.XPATH, "//a[@class='a14' and text()='群组']")
    ACTIVITY = (By.XPATH, "//a[@class='a14' and text()='活动']")
    EXIT = (By.XPATH, "//a[contains(text(),'退出')]")

    def __init__(self, browser):
        super().__init__(browser)

    def click_blog(self):
        """点击日志功能标签"""
        self.click_element(self.BLOG)

    def click_gift(self):
        """点击礼物功能标签"""
        self.click_element(self.GIFT)

    def click_share(self):
        """点击分享功能标签"""
        self.click_element(self.SHARE)

    def click_photo(self):
        """点击相册功能标签"""
        self.click_element(self.PHOTO)

    def click_mood(self):
        """点击心情功能标签"""
        self.click_element(self.MOOD)

    def click_voting(self):
        """点击投票功能标签"""
        self.click_element(self.VOTING)

    def click_group(self):
        """点击群组功能标签"""
        self.click_element(self.GROUP)

    def click_activity(self):
        """点击活动功能标签"""
        self.click_element(self.ACTIVITY)

    def click_exit_account(self):
        """点击退出登录"""
        self.click_element(self.EXIT)

    def exit_visible(self):
        self.wait_element_visible(self.EXIT)
