import time
import pytest_bdd
from data import userdetails
from pageObject import loginObj, addCaseObj, allCasesObj, dashboardObj, caseDetailObj

pytest_bdd.scenarios('C:\\Users\\muhammad.saad\\PycharmProjects\\pythonProject11\\tests\\features'
                     '\\create_case_all_cases.feature')


@pytest_bdd.given('Login and create a case')
def get_website(browser):
    browser.get("https://one-sites-pre-prod.avizia.com/#/site")
    browser.maximize_window()


@pytest_bdd.when(pytest_bdd.parsers.parse('user enter code "{code}" and login successfully with valid creds "{'
                                          'email}", "{password}"'))
def user_login(browser, code, email, password):
    sites_code = loginObj.sites_code(browser)
    sites_code.send_keys(code)
    loginObj.next_signup_btn(browser)
    time.sleep(2)
    loginObj.login_btn(browser)
    email_address = loginObj.email1(browser)
    email_address.send_keys(email)
    pass1 = loginObj.password1(browser)
    pass1.send_keys(password)
    loginObj.login_btn(browser)
    welcome1 = loginObj.sitesWelcome(browser)
    assert userdetails.welcome in welcome1
    time.sleep(1)


@pytest_bdd.when(pytest_bdd.parsers.parse('user go through case creation steps from all cases'))
def createCase(browser):
    dashboardObj.manageAllCases(browser)
    addCaseObj.createCase(browser)
    allCasesObj.workflowSelect(browser)
    allCasesObj.facilitySelect(browser)
    allCasesObj.endpointSkip(browser)
    allCasesObj.patientSkip(browser)
    allCasesObj.intakeContinueBtn(browser)
    time.sleep(2)


@pytest_bdd.then(pytest_bdd.parsers.parse('case created successfully without Patient'))
def caseCreatedSuccessfully(browser):
    case_id = caseDetailObj.caseId(browser)
    print(case_id)
    assert userdetails.caseID in case_id
    time.sleep(1)


