from selenium.webdriver.common.by import By
from driver_handler import DriverHandle


class Settings:
    ALL_USERS = (By.ID, 'users')
    PROFILE_TABLE = "//span[@title='<<replace>>']"

    def __init__(self):
        self.driver_handler = DriverHandle()

    def open_page(self, page_url):
        self.driver_handler.get_url(page_url)

    def users(self):
        self.driver_handler.wait_for_element_to_display(*self.ALL_USERS)

    def requested_users(self, email):
        var = str(self.PROFILE_TABLE).replace("<<replace>>", email)
        return self.driver_handler.get_element_containing_text(By.XPATH, var, email).text
