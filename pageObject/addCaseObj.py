from selenium.webdriver.common.by import By


def createCase(browser):
    return browser.find_element(By.ID, 'addCase').click()
