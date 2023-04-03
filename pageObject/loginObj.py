from selenium.webdriver.common.by import By


def sites_code(browser):
    return browser.find_element(By.ID, 'code')


def email1(browser):
    return browser.find_element(By.ID, 'email')


def password1(browser):
    return browser.find_element(By.ID, 'password')


def next_signup_btn(browser):
    return browser.find_element(By.ID, 'signUpBtn').click()


def login_btn(browser):
    return browser.find_element(By.ID, 'loginBtn').click()


def sitesWelcome(browser):
    return browser.find_element(By.CSS_SELECTOR, '[automation="sitesWelcome"]').text


def invalid_creds(browser):
    return browser.find_element(By.CSS_SELECTOR, '[automation="incorrectEmailPassword"]').text


# class TestLoginLocators(object):
    # invalid_creds = (By.CSS_SELECTOR, '[automation="incorrectEmailPassword"]').text
#     signUp = (By.ID, 'signUpBtn')
#     loginBtn = (By.ID, 'loginBtn')
#     code = (By.ID, 'code')
#     email = (By.ID, 'email')
#     password = (By.ID, 'password')
#     welcomeHeading = (By.CSS_SELECTOR, '[automation="sitesWelcome"]')
#     userMenu = (By.ID, 'userMenuComponent')
#     logout = (By.ID, 'headerLogout')

