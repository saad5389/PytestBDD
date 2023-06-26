from selenium.webdriver.common.by import By
from driver_handler import DriverHandle


class Dashboard:
    MANAGE_ALL_CASES = (By.CSS_SELECTOR, '[ng-click="$ctrl.gotoAllCases()"]')

    def __init__(self):
        self.driver_handler = DriverHandle()

    def manageAllCases(self):
        self.driver_handler.click_element(*self.MANAGE_ALL_CASES)
