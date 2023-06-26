from selenium.webdriver.common.by import By
from driver_handler import DriverHandle


class Login:
    LOGIN_BTN = (By.ID, 'loginBtn')
    SIGNUP_BTN = (By.ID, 'signUpBtn')
    CODE = (By.ID, 'code')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    WELCOME = (By.CSS_SELECTOR, '[automation="sitesWelcome"]')
    INCORRECT_EMAIL_PASSWORD = (By.CSS_SELECTOR, '[automation="incorrectEmailPassword"]')

    def __init__(self):
        self.driver_handler = DriverHandle()

    def open_page(self, page_url):
        self.driver_handler.get_url(page_url)

    def enter_site_code(self, code):
        self.driver_handler.send_keys(*self.CODE, code)

    def click_login(self):
        self.driver_handler.click_element(*self.LOGIN_BTN)

    def next_signup_btn(self):
        self.driver_handler.click_element(*self.SIGNUP_BTN)

    def enter_email(self, email):
        self.driver_handler.send_keys(*self.EMAIL, email)

    def enter_password(self, password):
        self.driver_handler.send_keys(*self.PASSWORD, password)

    def sitesWelcome(self):
        return self.driver_handler.get_element_text(*self.WELCOME)

    def invalid_creds(self):
        return self.driver_handler.get_element_text(*self.INCORRECT_EMAIL_PASSWORD)
