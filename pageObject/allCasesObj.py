from selenium.webdriver.common.by import By
from driver_handler import DriverHandle


class AllCases:
    SELECT_WORKFLOW = (By.ID, 'clinicalName1')
    SELECT_FACILITY = (By.ID, 'facilityName0')
    SELECT_ENDPOINT = (By.CSS_SELECTOR, '[automation="endpointName"]')
    SKIP_ENDPOINT = (By.CSS_SELECTOR, '[ng-click="$ctrl.skipEndpointSelect()"]')
    SKIP_PATIENT = (By.CSS_SELECTOR, '[ng-click="$ctrl.skipPatientSelect()"]')
    PATIENT_SEARCH = (By.CSS_SELECTOR, '[automation="SearchComponentBtnSearch"]')
    ADD_NEW_PATIENT = (By.ID, 'add-patients')
    INTAKE_CONTINUE_BTN = (By.CSS_SELECTOR, '[automation="intakeStepContinueBtn"]')
    SEARCH_CASE = (By.CSS_SELECTOR, '[ng-model="$ctrl.searchTerm"]')
    CASE_NUM = (By.CSS_SELECTOR, '.case-number strong')

    def __init__(self):
        self.driver_handler = DriverHandle()
        
    def workflowSelect(self):
        self.driver_handler.click_element(*self.SELECT_WORKFLOW)
    
    def facilitySelect(self):
        self.driver_handler.click_element(*self.SELECT_FACILITY)
    
    def endpointSelect(self):
        self.driver_handler.click_element(*self.SELECT_ENDPOINT)
    
    def endpointSkip(self):
        self.driver_handler.click_element(*self.SKIP_ENDPOINT)
    
    def patientSkip(self):
        self.driver_handler.click_element(*self.SKIP_PATIENT)
    
    def patientSearch(self):
        self.driver_handler.click_element(*self.PATIENT_SEARCH)
    
    def addNewPatient(self):
        self.driver_handler.click_element(*self.ADD_NEW_PATIENT)
    
    def intakeContinueBtn(self):
        self.driver_handler.click_element(*self.INTAKE_CONTINUE_BTN)

    def searchCase(self, case_id):
        self.driver_handler.click_element(*self.SEARCH_CASE)
        self.driver_handler.send_keys(*self.SEARCH_CASE, case_id)

    def expectedCase(self):
        self.driver_handler.wait_for_element_to_display(*self.CASE_NUM)
        return self.driver_handler.get_element_text(*self.CASE_NUM)

