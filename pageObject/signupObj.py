from selenium.webdriver.common.by import By
from driver_handler import DriverHandle


class SignUp:
    SIGNUP_BTN = (By.CSS_SELECTOR, '[type="button"][id="signUpBtn"]')
    ENTER_FIRSTNAME = (By.ID, 'first_name')
    ENTER_LASTNAME = (By.ID, 'last_name')
    ENTER_EMAIL = (By.ID, 'email')
    REQUEST_BTN = (By.ID, 'loginBtn')
    REQUEST_SENT = (By.CSS_SELECTOR, '[automation="loginCardTopLayout"] p.lead')
    BACK_TO_LOGIN = (By.ID, 'backBtn')

    def __init__(self):
        self.driver_handler = DriverHandle()

    def open_page(self, page_url):
        self.driver_handler.get_url(page_url)

    def signup_btn_click(self):
        self.driver_handler.click_element(*self.SIGNUP_BTN)

    def enter_first_name(self, first_name):
        self.driver_handler.send_keys(*self.ENTER_FIRSTNAME, first_name)

    def enter_last_name(self, last_name):
        self.driver_handler.send_keys(*self.ENTER_LASTNAME, last_name)

    def enter_email(self, email):
        self.driver_handler.send_keys(*self.ENTER_EMAIL, email)

    def click_request_access_btn(self):
        self.driver_handler.click_element(*self.REQUEST_BTN)

    def back_to_login(self):
        self.driver_handler.click_element(*self.BACK_TO_LOGIN)

    def request_Sent(self):
        return self.driver_handler.get_element_text(*self.REQUEST_SENT)
