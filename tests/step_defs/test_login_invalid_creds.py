import time
import pytest_bdd

from data import userdetails
from pageObject import loginObj

pytest_bdd.scenarios('C:\\Users\\muhammad.saad\\PycharmProjects\\pythonProject11\\tests\\features'
                     '\\login_invalid.feature')


@pytest_bdd.given('Login page')
def get_website(browser):
    browser.get("https://one-sites-pre-prod.avizia.com/#/site")
    browser.maximize_window()


@pytest_bdd.when(pytest_bdd.parsers.parse('the user enter Code "{code}" and clicks on Next button'))
def sitesCode(browser, code):
    sites_code = loginObj.sites_code(browser)
    sites_code.send_keys(code)
    loginObj.next_signup_btn(browser)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user clicks on login button'))
def login_click(browser):
    time.sleep(2)
    loginObj.login_btn(browser)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user enter email address "{email}"'))
def login_user(browser, email):
    email_address = loginObj.email1(browser)
    email_address.send_keys(email)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user enter password "{password}"'))
def login_pass(browser, password):
    pass1 = loginObj.password1(browser)
    pass1.send_keys(password)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user clicks on login button'))
def login_btn(browser):
    loginObj.login_btn(browser)


@pytest_bdd.then(pytest_bdd.parsers.parse('user should not login and validation message should appear'))
def sitesWelcome(browser):
    time.sleep(1)
    incorrect_email_pass = loginObj.invalid_creds(browser)
    assert userdetails.invalidCredsError in incorrect_email_pass
    print(incorrect_email_pass)
