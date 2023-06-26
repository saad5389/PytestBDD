from selenium.webdriver.common.by import By
from driver_handler import DriverHandle


class MyCases:
    CASE_NUM = '[automation="myCaseID"]'
    ACTIVE = (By.ID, '#active')

    def __init__(self):
        self.driver_handler = DriverHandle()

    def waitForActiveCases(self, case_id):
        self.driver_handler.wait_for_element_to_display(*self.ACTIVE)

    def myAssignedCase(self, case_id):
        var = str(self.CASE_NUM).replace("<<replace>>", case_id)
        return self.driver_handler.get_element_containing_text(By.CSS_SELECTOR, var, case_id).text

