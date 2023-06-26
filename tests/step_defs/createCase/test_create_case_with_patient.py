import pytest
from data import userdetails, route
from pageObject.loginObj import Login
from pageObject.dashboardObj import Dashboard
from pageObject.caseDetailObj import CaseDetail
from pageObject.allCasesObj import AllCases
from pageObject.addCaseObj import AddCase
from pageObject.headerObj import HeaderMenu
from pageObject.patientObj import Patient
from helpers import Helpers
from pytest_bdd import (given, scenario, then, when, parsers)

loginObj = Login()
dashboardObj = Dashboard()
caseDetailObj = CaseDetail()
allCasesObj = AllCases()
addCaseObj = AddCase()
headerObj = HeaderMenu()
patientObj = Patient()
helpers = Helpers()


# @pytest.mark.skip
@pytest.mark.web
@pytest.hookimpl(tryfirst=True)
@scenario('../../../tests/features/createCase/create_case_with_patient'
          '.feature', 'Create case with Patient')
def test_Create_case_with_Patient(web_driver):
    """Create case with Patient"""


@given('Login page')
def get_website():
    loginObj.open_page(userdetails.BaseURL + route.site)


@when(parsers.parse('user enter code "{code}" and login successfully with valid creds "{email}", "{password}"'))
def user_login(code, email, password):
    helpers.login(code, email, password)


@when(parsers.parse('user search for a patient firstname "{firstname}" and lastname "{lastname}"'))
def searchPatient(firstname, lastname):
    helpers.patientSearch(firstname, lastname)
    patientObj.patient_detail_header()
    patientObj.click_create_case()


@when(parsers.parse('user go through case creation steps from all cases'))
def createCase():
    helpers.createCase()


@pytest.hookimpl(trylast=True)
@then(parsers.parse('user creates a case successfully with patient'))
def caseCreatedSuccessfully():
    caseDetailObj.caseDetailSummary()
    caseDetailObj.patientId()
    patient_id = caseDetailObj.patientId()
    assert userdetails.patientName in patient_id
