import pytest
from data import userdetails, route
from pageObject.loginObj import Login
from pageObject.caseDetailObj import CaseDetail
from pageObject.allCasesObj import AllCases
from pageObject.myCasesObj import MyCases
from pageObject.addCaseObj import AddCase
from helpers import Helpers
from pytest_bdd import (given, scenario, then, when, parsers)

loginObj = Login()
caseDetailObj = CaseDetail()
allCasesObj = AllCases()
myCasesObj = MyCases()
addCaseObj = AddCase()
helpers = Helpers()


# @pytest.mark.skip
@pytest.mark.web
@pytest.hookimpl(tryfirst=True)
@scenario('../../../tests/features/createCase/assign_case_appears_in_my_cases_tab'
          '.feature', 'Assign case appears in My Cases tab')
def test_assign_case_appears_in_My_Cases_tab(web_driver):
    """Assign case appears in My Cases tab"""


@given('Login page')
def get_website():
    loginObj.open_page(userdetails.BaseURL + route.site)


@when(parsers.parse('user enter code "{code}" and login successfully with valid creds "{email}", "{password}"'))
def user_login(code, email, password):
    helpers.login(code, email, password)


@when(parsers.parse('user go through case creation steps from all cases'))
def createCase():
    helpers.createCaseWithoutPatient()


@then(parsers.parse('case created successfully and assigned to me'))
def assignCase():
    caseDetailObj.caseDetailSummary()
    caseDetailObj.patientId()
    global case_id
    case_id = caseDetailObj.caseId()
    caseDetailObj.assign_to_me()
    caseDetailObj.waitCaseComplete()


@pytest.hookimpl(trylast=True)
@then(parsers.parse('search the created case on my cases page'))
def searchCase():
    loginObj.open_page(userdetails.BaseURL + route.myCases)
    assigned_case = myCasesObj.myAssignedCase(case_id)
    assert case_id == assigned_case
