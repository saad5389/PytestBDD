import pytest
from faker import Faker
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
fake = Faker()
p_firstname = fake.first_name()
p_lastname = fake.last_name()


# @pytest.mark.skip
@pytest.mark.web
@pytest.hookimpl(tryfirst=True)
@scenario('../../../tests/features/patients/add_patient.feature', 'Add new Patient')
def test_Add_Patient(web_driver):
    """Add new Patient"""


@given('Login page')
def get_website():
    loginObj.open_page(userdetails.BaseURL + route.site)


@when(parsers.parse('user enter code "{code}" and login successfully with valid creds "{email}", "{password}"'))
def user_login(code, email, password):
    helpers.login(code, email, password)


@when(parsers.parse('user clicks on Add patient and enter mandatory fields firstname, lastname, "{dob}" and '
                    '"{gender}"'))
def addPatient(gender):
    helpers.addPatient(p_firstname, p_lastname, gender)


@then(parsers.parse('new patient created successfully'))
def newPatient():
    patientObj.active_create_case()
    patientObj.patient_detail_header()


@pytest.hookimpl(trylast=True)
@then(parsers.parse('verify new patient on patient-search page'))
def verifyPatient():
    helpers.patientVerification(p_firstname, p_lastname)
    abc = patientObj.patient_search(p_lastname)
    assert p_lastname in abc
