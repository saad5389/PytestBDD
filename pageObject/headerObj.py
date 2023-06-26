from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from driver_handler import DriverHandle


class HeaderMenu:
    CLINIC_DROPDOWN = (By.ID, 'dropdown-clinic')
    PATIENT_MENU = (By.XPATH,  '//div[text()=" Patients "]')

    def __init__(self):
        self.driver_handler = DriverHandle()

    def click_clinic_dropdown(self):
        self.driver_handler.click_element(*self.CLINIC_DROPDOWN)

    def wait_patient_menu(self):
        self.driver_handler.wait_for_element_to_display(*self.PATIENT_MENU)

    def click_patient_menu(self):
        self.driver_handler.click_element(*self.PATIENT_MENU)
