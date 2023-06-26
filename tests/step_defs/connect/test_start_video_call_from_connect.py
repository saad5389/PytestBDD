import pytest
from data import userdetails, route
from pageObject.loginObj import Login
from pageObject.connectObj import Connect
from helpers import Helpers
from pytest_bdd import (given, scenario, then, when, parsers)
from selenium.webdriver.common.alert import Alert

loginObj = Login()
connectObj = Connect()
helpers = Helpers()


@pytest.mark.skip
@pytest.mark.web
@pytest.hookimpl(tryfirst=True)
@scenario('../../../tests/features/connect/start_video_call_from_connect'
          '.feature', 'Start video call from Connect')
def test_start_video_call_from_connect(web_driver):
    """Start video call from Connect"""


@given('Login page')
def get_website():
    loginObj.open_page(userdetails.BaseURL + route.site)


@when(parsers.parse('user enter code "{code}" and login successfully with valid creds "{email}", "{password}"'))
def user_login(code, email, password):
    helpers.login(code, email, password)


@when(parsers.parse('user go to Quick Connect and create a room with "{email}" address'))
def createQuickRoom(email):
    loginObj.open_page(userdetails.BaseURL + route.connect)
    connectObj.email_invitation_method()
    connectObj.enter_email(email)
    connectObj.invite_participants()


@then(parsers.parse('user join the newly created room'))
def test_joinRoom():
    connectObj.join_room()

@pytest.hookimpl(trylast=True)
@then(parsers.parse('user ends the call'))
def endCall():
    connectObj.joined_call_end()
    connectObj.black_toast()
