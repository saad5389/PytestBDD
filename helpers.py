from faker import Faker
from data import userdetails, route
from pageObject.allCasesObj import AllCases
from pageObject.loginObj import Login
from pageObject.patientObj import Patient
from pageObject.addCaseObj import AddCase

allCasesObj = AllCases()
addCaseObj = AddCase()
loginObj = Login()
patientObj = Patient()
fake = Faker()
p_firstname = fake.first_name()
p_lastname = fake.last_name()


class Helpers:

    def login(self, code, email, password):
        loginObj.enter_site_code(code)
        loginObj.next_signup_btn()
        loginObj.click_login()
        loginObj.enter_email(email)
        loginObj.enter_password(password)
        loginObj.click_login()
        welcome = loginObj.sitesWelcome()
        assert userdetails.Welcome in welcome

    def createCaseWithoutPatient(self):
        loginObj.open_page(userdetails.BaseURL + route.cases)
        addCaseObj.createCase()
        allCasesObj.workflowSelect()
        allCasesObj.facilitySelect()
        allCasesObj.endpointSkip()
        allCasesObj.patientSkip()
        allCasesObj.intakeContinueBtn()

    def createCase(self):
        allCasesObj.workflowSelect()
        allCasesObj.facilitySelect()
        allCasesObj.endpointSkip()
        allCasesObj.intakeContinueBtn()

    def patientSearch(self, firstname, lastname):
        loginObj.open_page(userdetails.BaseURL + route.patientSearch)
        patientObj.display_add_patient()
        patientObj.enter_first_name(firstname)
        patientObj.enter_last_name(lastname)
        patientObj.click_search()
        patientObj.click_select()

    def patientVerification(self, firstname, lastname):
        loginObj.open_page(userdetails.BaseURL + route.patientSearch)
        patientObj.display_add_patient()
        patientObj.enter_first_name(firstname)
        patientObj.enter_last_name(lastname)
        patientObj.click_search()

    def addPatient(self, firstname, lastname, gender):
        loginObj.open_page(userdetails.BaseURL + route.patientSearch)
        patientObj.display_add_patient()
        patientObj.click_add_patient()
        patientObj.patientHeader()
        patientObj.patient_firstname(firstname)
        patientObj.patient_lastname(lastname)
        patientObj.patient_dob()
        patientObj.patient_gender(gender)
        patientObj.submitBtn()
