from selenium.webdriver.common.by import By


def manageAllCases(browser):
    return browser.find_element(By.CSS_SELECTOR, '[ng-click="$ctrl.gotoAllCases()"]').click()
