import pytest

from data import userdetails, route
from pytest_bdd import (given, scenario, then, when, parsers)
from pageObject.signupObj import SignUp
from pageObject.loginObj import Login
from pageObject.settingsObj import Settings
from faker import Faker


signupObj = SignUp()
loginObj = Login()
settingsObj = Settings()
fake = Faker()
email = fake.user_name() + userdetails.test_domain


# @pytest.mark.skip
@pytest.mark.web
@pytest.hookimpl(tryfirst=True)
@scenario('../../../tests/features/signup/request_signup_new'
          '.feature', 'Request signup with new user')
def test_request_signup_with_new_user(web_driver):
    """Request signup with new user"""


@given('Code page')
def get_website():
    signupObj.open_page(userdetails.stg + route.site)


@when(parsers.parse('the user enter Code "{code}" and clicks on Next button'))
def sitesCode(code):
    loginObj.enter_site_code(code)
    loginObj.next_signup_btn()


@when(parsers.parse('the user clicks on Sign Up button'))
def signUp_click():
    signupObj.signup_btn_click()


@when(parsers.parse('the user enter Firstname "{firstname}", Lastname "{lastname}" and Email'))
def request_access(firstname, lastname):
    signupObj.enter_first_name(firstname)
    signupObj.enter_last_name(lastname)
    signupObj.enter_email(email)


@then(parsers.parse('the user clicks on Request Access button should Signup successfully and lands on '
                    'Request Sent screen with Thankyou message'))
def requested():
    signupObj.click_request_access_btn()
    request_sent = signupObj.request_Sent()
    assert userdetails.requestSent in request_sent
    signupObj.back_to_login()
    loginObj.click_login()


@then(parsers.parse('user login with admin user email "{email}" and password "{password}"'))
def login_user(email, password):
    loginObj.enter_email(email)
    loginObj.enter_password(password)
    loginObj.click_login()
    welcome = loginObj.sitesWelcome()
    assert userdetails.Welcome in welcome


@pytest.hookimpl(trylast=True)
@then(parsers.parse('admin verify the signup request'))
def signup_request_verify():
    signupObj.open_page(userdetails.stg + route.settings)
    settingsObj.users()
    new_user = settingsObj.requested_users(email)
    assert email == new_user
