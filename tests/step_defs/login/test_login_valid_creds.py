import pytest

from data import userdetails, route
from pageObject.loginObj import Login
from pytest_bdd import (given, scenario, then, when, parsers)

loginObj = Login()


# @pytest.mark.skip
@pytest.mark.web
@pytest.hookimpl(tryfirst=True)
@scenario('../../../tests/features/login/login_valid.feature',
          'login with valid creds')
def test_login_with_valid_creds(web_driver):
    """Login with valid credentials"""


@given('Login page')
def get_website():
    loginObj.open_page(userdetails.BaseURL + route.site)


@when(parsers.parse('the user enter Code "{code}" and clicks on Next button'))
def sitesCode(code):
    loginObj.enter_site_code(code)
    loginObj.next_signup_btn()


@when(parsers.parse('the user clicks on Login button'))
def login_click():
    loginObj.click_login()


@when(parsers.parse('the user enter email address "{email}" and password "{password}"'))
def login_user(email, password):
    loginObj.enter_email(email)
    loginObj.enter_password(password)


@when(parsers.parse('the user clicks on login button'))
def login_btn():
    loginObj.click_login()


@pytest.hookimpl(trylast=True)
@then(parsers.parse('user should login successfully and lands on dashboard with Welcome heading'))
def sitesWelcome():
    welcome = loginObj.sitesWelcome()
    assert userdetails.Welcome in welcome
