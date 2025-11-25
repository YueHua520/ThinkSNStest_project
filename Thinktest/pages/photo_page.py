from selenium.webdriver.common.by import By
from pages.base_page import Basepage


class PhotoPage(Basepage):
    FRIENDPHOTO = (By.XPATH, "//span[text() = '好友的照片']")

    def __init__(self, browser):
        super().__init__(browser)

    def open_photo_url(self):
        self.open_url(f"{self.base_url}/apps/photo/index.php?s=/Index/photos/uid/3")
