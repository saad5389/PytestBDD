from selenium.webdriver.common.by import By
from driver_handler import DriverHandle


class CaseDetail:
    PATIENT_FULLNAME = (By.ID, 'patient-full-name')
    CASE_DETAIL_SUMMARY = (By.ID, 'case-detail-summary')
    PATIENT_INFO = (By.CSS_SELECTOR, '[automation="headerPatientInfo"]')
    CASE_ID = (By.CSS_SELECTOR, '[id="caseId"] strong')
    ASSIGNED_CASE = (By.CSS_SELECTOR, '[ng-click="$ctrl.openDropdown()"]')
    ASSIGNED_TO_ME = (By.CSS_SELECTOR, '[id="assignee_container"] li span')
    CASE_COMPLETE_BTN = (By.CSS_SELECTOR, '[ng-click="vm.completeCaseFromSection()"]')

    def __init__(self):
        self.driver_handler = DriverHandle()

    def patientId(self):
        self.driver_handler.wait_for_element_to_display(*self.PATIENT_FULLNAME)

    def caseDetailSummary(self):
        self.driver_handler.wait_for_element_to_display(*self.CASE_DETAIL_SUMMARY)

    def patientInfo(self):
        return self.driver_handler.get_element_text(*self.PATIENT_INFO)

    def caseId(self):
        self.driver_handler.wait_for_element_to_display(*self.CASE_ID)
        return self.driver_handler.get_element_text(*self.CASE_ID)

    def waitCaseComplete(self):
        self.driver_handler.wait_for_element_to_display(*self.CASE_COMPLETE_BTN)

    def assign_to_me(self):
        self.driver_handler.wait_for_element_to_display(*self.PATIENT_FULLNAME)
        self.driver_handler.click_element(*self.ASSIGNED_CASE)
        return self.driver_handler.click_element_by_text(*self.ASSIGNED_TO_ME, 'Assign to me')
