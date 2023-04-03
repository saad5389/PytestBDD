from selenium.webdriver.common.by import By


def first_name(browser):
    return browser.find_element(By.ID, 'first_name')


def last_name(browser):
    return browser.find_element(By.ID, 'last_name')


def signup_email(browser):
    return browser.find_element(By.ID, 'email')


def signup_btn(browser):
    return browser.find_element(By.ID, 'signUpBtn').click()


def request_access(browser):
    return browser.find_element(By.ID, 'loginBtn').click()


def request_Sent(browser):
    return browser.find_element(By.CSS_SELECTOR, '[automation="loginCardTopLayout"] p.lead').text
