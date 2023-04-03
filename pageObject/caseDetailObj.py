from selenium.webdriver.common.by import By


def caseId(browser):
    return browser.find_element(By.ID, 'case-detail-summary').text
