from selenium.webdriver.common.by import By


def workflowSelect(browser):
    return browser.find_element(By.ID, 'clinicalName0').click()


def facilitySelect(browser):
    return browser.find_element(By.ID, 'facilityName0').click()


def endpointSelect(browser):
    return browser.find_element(By.CSS_SELECTOR, '[automation="endpointName"]').click()


def endpointSkip(browser):
    return browser.find_element(By.CSS_SELECTOR, '[ng-click="$ctrl.skipEndpointSelect()"]').click()


def patientSkip(browser):
    return browser.find_element(By.CSS_SELECTOR, '[ng-click="$ctrl.skipPatientSelect()"]').click()


def patientSearch(browser):
    return browser.find_element(By.CSS_SELECTOR, '[automation="SearchComponentBtnSearch"]').click()


def addNewPatient(browser):
    return browser.find_element(By.ID, 'add-patient').click()


def intakeContinueBtn(browser):
    return browser.find_element(By.CSS_SELECTOR, '[automation="intakeStepContinueBtn"]').click()


