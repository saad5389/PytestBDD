import pytest

from data import userdetails, route
from pageObject.loginObj import Login
from pageObject.dashboardObj import Dashboard
from pageObject.caseDetailObj import CaseDetail
from pageObject.allCasesObj import AllCases
from pageObject.addCaseObj import AddCase
from helpers import Helpers
from pytest_bdd import (given, scenario, then, when, parsers)

loginObj = Login()
dashboardObj = Dashboard()
caseDetailObj = CaseDetail()
allCasesObj = AllCases()
addCaseObj = AddCase()
helpers = Helpers()


# @pytest.mark.skip
@pytest.mark.web
@pytest.hookimpl(tryfirst=True)
@scenario('../../../tests/features/createCase/create_case_all_cases'
          '.feature', 'Create case from all cases without Patient')
def test_Create_case_from_all_cases_without_Patient(web_driver):
    """Create case from all cases without Patient"""


@given('Login page')
def get_website():
    loginObj.open_page(userdetails.BaseURL + route.site)


@when(parsers.parse('user enter code "{code}" and login successfully with valid creds "{email}", "{password}"'))
def user_login(code, email, password):
    helpers.login(code, email, password)


@when(parsers.parse('user go through case creation steps from all cases'))
def createCase():
    helpers.createCaseWithoutPatient()


@then(parsers.parse('case created successfully without Patient'))
def caseCreatedSuccessfully():
    caseDetailObj.caseDetailSummary()
    caseDetailObj.patientId()
    global case_id
    case_id = caseDetailObj.caseId()


@pytest.hookimpl(trylast=True)
@then(parsers.parse('search the created case on All cases page'))
def searchCase():
    loginObj.open_page(userdetails.BaseURL + route.cases)
    allCasesObj.searchCase(case_id)
    expected_case = allCasesObj.expectedCase()
    assert case_id == expected_case
