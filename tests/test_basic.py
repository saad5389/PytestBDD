# import time
# from _ast import Assert
#
# import pytest
# from pageObject import loginObj
# from data import userdetails
# from tests.test_base import TestBase
#
#
# @pytest.mark.skip
# class TestBasic(TestBase):
#     @pytest.mark.skip
#     def test_for_specific_browser(self, browser):
#         browser.get("https://www.google.com")
#
#     def test_user_login_successful(self):
#         driver = self.driver
#
#         code = driver.find_element(*loginObj.TestLoginLocators.code)
#         code.send_keys(userdetails.code)
#
#         driver.find_element(*loginObj.TestLoginLocators.signUp).click()
#
#         driver.find_element(*loginObj.TestLoginLocators.loginBtn).click()
#
#         username = driver.find_element(*loginObj.TestLoginLocators.email)
#         username.send_keys(userdetails.preprod_email)
#
#         password = driver.find_element(*loginObj.TestLoginLocators.password)
#         password.send_keys(userdetails.preprod_password)
#
#         driver.find_element(*loginObj.TestLoginLocators.loginBtn).click()
#         time.sleep(3)
#
#         welcome = driver.find_element(*loginObj.TestLoginLocators.welcomeHeading).text
#         assert userdetails.welcome in welcome
#     #
#     # def test_user_logout_successful(self):
#     #     driver = self.driver
#     #     driver.find_element(*loginObj.TestLoginLocators.userMenu).click()
#     #     driver.find_element(*loginObj.TestLoginLocators.logout).click()
