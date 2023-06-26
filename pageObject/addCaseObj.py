from selenium.webdriver.common.by import By
from driver_handler import DriverHandle


class AddCase:
    ADD_CASE = (By.ID, 'addCase')

    def __init__(self):
        self.driver_handler = DriverHandle()

    def createCase(self):
        self.driver_handler.click_element(*self.ADD_CASE)
