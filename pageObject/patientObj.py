import random
from datetime import timedelta
from selenium.webdriver.common.by import By
from driver_handler import DriverHandle
from data import userdetails


class Patient:
    ADD_PATIENT = (By.CSS_SELECTOR, '[automation="PatientSearchAddPatient"]')
    PATIENT_HEADER = (By.CSS_SELECTOR, '[automation = "AddPatientHeader"]')
    ENTER_FIRSTNAME = (By.ID, 'first-name')
    ENTER_LASTNAME = (By.ID, 'last-name')
    PATIENT_FIRSTNAME = (By.ID, 'firstName')
    PATIENT_LASTNAME = (By.ID, 'lastName')
    PATIENT_DOB = (By.CSS_SELECTOR, '[automation="AddPatientDateOfBirth"] input')
    PATIENT_GENDER = (By.CSS_SELECTOR, '[automation="AddPatientGender"]')
    PATIENT_GENDER_SELECTION = (By.CSS_SELECTOR, '[automation="AddPatientGender"] ul li')
    SUBMIT_BTN = (By.CSS_SELECTOR, '[automation="AddPatientBtnSave"] button')
    SEARCH = (By.CSS_SELECTOR, '[automation="SearchComponentBtnSearch"]')
    SELECT = (By.CSS_SELECTOR, '[automation="SearchComponentBtnSelect"]')
    PATIENT_HEADER_TITLE = (By.CSS_SELECTOR, '[automation="PatientDetailHeaderTitle"] span')
    ACTIVE_CASES_BTN = (By.CSS_SELECTOR, '[automation="PatientSummaryActiveCasesBtnCreateCasePanelHeader"]')
    PATIENT_SEARCH_NAME = '[automation="SearchComponentColumnPatientName"]'

    def __init__(self):
        self.driver_handler = DriverHandle()

    def display_add_patient(self):
        self.driver_handler.wait_for_element_to_display(*self.ADD_PATIENT)

    def click_add_patient(self):
        self.driver_handler.click_element(*self.ADD_PATIENT)

    def patientHeader(self):
        self.driver_handler.wait_for_element_to_display(*self.PATIENT_HEADER)

    def enter_first_name(self, firstname):
        self.driver_handler.send_keys(*self.ENTER_FIRSTNAME, firstname)

    def enter_last_name(self, lastname):
        self.driver_handler.send_keys(*self.ENTER_LASTNAME, lastname)

    def patient_firstname(self, firstname):
        self.driver_handler.send_keys(*self.PATIENT_FIRSTNAME, firstname)

    def patient_lastname(self, lastname):
        self.driver_handler.send_keys(*self.PATIENT_LASTNAME, lastname)

    def patient_dob(self):
        random_date = userdetails.start_date + timedelta(days=random.randint(0, (userdetails.end_date - userdetails.start_date).days))
        dob = random_date.strftime("%Y-%m-%d")
        self.driver_handler.send_keys(*self.PATIENT_DOB, dob)

    def patient_gender(self, gender):
        self.driver_handler.click_element(*self.PATIENT_GENDER)
        return self.driver_handler.click_element_by_text(*self.PATIENT_GENDER_SELECTION, gender)

    def submitBtn(self):
        self.driver_handler.click_element(*self.SUBMIT_BTN)

    def click_search(self):
        self.driver_handler.click_element(*self.SEARCH)

    def click_select(self):
        self.driver_handler.click_element(*self.SELECT)

    def patient_detail_header(self):
        return self.driver_handler.get_element_text(*self.PATIENT_HEADER_TITLE)

    def active_create_case(self):
        self.driver_handler.wait_for_element_to_display(*self.ACTIVE_CASES_BTN)

    def patientName(self):
        return self.driver_handler.get_element_text(*self.PATIENT_HEADER_TITLE)

    def click_create_case(self):
        self.driver_handler.click_element(*self.ACTIVE_CASES_BTN)

    def patient_search(self, p_lastname):
        var = str(self.PATIENT_SEARCH_NAME).replace("<<replace>>", p_lastname)
        return self.driver_handler.get_element_containing_text(By.CSS_SELECTOR, var, p_lastname).text
