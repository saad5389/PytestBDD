import time
import pytest_bdd

from data import userdetails
from pageObject import loginObj, signupObj


pytest_bdd.scenarios('C:\\Users\\muhammad.saad\\PycharmProjects\\pythonProject11\\tests\\features\\signup_new.feature')


@pytest_bdd.given('Code page')
def get_website(browser):
    browser.get("https://one-sites-pre-prod.avizia.com/#/site")
    browser.maximize_window()


@pytest_bdd.when(pytest_bdd.parsers.parse('the user enter Code "{code}" and clicks on Next button'))
def sitesCode(browser, code):
    sites_code = loginObj.sites_code(browser)
    sites_code.send_keys(code)
    signupObj.signup_btn(browser)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user clicks on Sign Up button'))
def signUp_click(browser):
    time.sleep(2)
    signupObj.signup_btn(browser)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user enter Firstname "{firstname}", Lastname "{lastname}" and '
                                          'Email "{email}"'))
def request_access(browser, firstname, lastname, email):
    first_name = signupObj.first_name(browser)
    first_name.send_keys(firstname)
    last_name = signupObj.last_name(browser)
    last_name.send_keys(lastname)
    email_address = loginObj.email1(browser)
    email_address.send_keys(email)


@pytest_bdd.then(
    pytest_bdd.parsers.parse('the user clicks on Request Access button should Signup successfully and lands on '
                             'Request Sent screen with Thankyou message'))
def requested(browser):
    time.sleep(2)
    signupObj.request_access(browser)
    request_sent = signupObj.request_Sent(browser)
    assert userdetails.requestSent in request_sent
