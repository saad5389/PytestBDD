import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DriverHandle:

    def get_driver(self):
        try:
            driver: 'WebDriver' = pytest.web_driver
            return driver
        except Exception as e:
            print(f"in Get Driver {str(e)}")

    def get_url(self, pstr_url):
        try:
            self.get_driver().get(pstr_url)
        except Exception as e:
            raise Exception("Error occurred while opening the url " + pstr_url + "-->", e)

    def send_keys(self, locater_type_by, locate_identifier, pstr_text_to_send):
        try:
            self.wait_for_element_to_display(locater_type_by, locate_identifier)
            self.get_element(locater_type_by, locate_identifier).send_keys(pstr_text_to_send)
        except Exception as e:
            raise Exception("Exception occurred while sending text to element :", locate_identifier, "-->", e)

    def get_element(self, locater_type_by, locate_identifier):
        try:
            return self.get_driver().find_element(by=locater_type_by, value=locate_identifier)
        except Exception as e:
            raise Exception(
                f"Error occurred while getting the element By {locater_type_by} :" + locate_identifier + "-->", e)

    def wait_for_element_to_display(self, locater_type_by, locate_identifier, pint_time_to_wait=20):
        try:
            count = 0
            while not self.get_element(locater_type_by, locate_identifier).is_displayed():
                count += 1
                if count > pint_time_to_wait:
                    break
            WebDriverWait(self.get_driver(), pint_time_to_wait).until(
                EC.visibility_of(self.get_element(locater_type_by, locate_identifier)))
        except Exception as e:
            raise Exception("Exception occurred while waiting for element to be located :", locate_identifier, " --> ",
                            e)

    def click_element(self, locater_type_by, locate_identifier):
        try:
            self.wait_for_element_to_display(locater_type_by, locate_identifier)
            self.get_element(locater_type_by, locate_identifier).click()
        except Exception as e:
            raise Exception("Exception occurred while clicking element :", locate_identifier, "-->", e)

    def click_element_by_text(self, locater_type_by, locate_identifier, text):
        try:
            self.get_element_containing_text(locater_type_by, locate_identifier, text).click()
        except Exception as e:
            raise Exception("Exception occurred while clicking element :", locate_identifier, "-->", e)

    def get_element_text(self, locater_type_by, locate_identifier, pint_wait_for_element=20):
        try:
            self.wait_for_element_to_display(locater_type_by, locate_identifier, pint_wait_for_element)
            return self.get_element(locater_type_by, locate_identifier).text
        except Exception as e:
            raise Exception("Exception occurred while fetching element text -->", e)

    def is_element_present(self, locater_type_by, locate_identifier):
        try:
            element = self.get_element(locater_type_by, locate_identifier)
            # element = WebDriverWait(self.get_driver(), 20).until(EC.presence_of_element_located((locater_type_by,
            # locater_identifer)))
            if element is not None:
                return True
            else:
                return False
        except Exception as e:
            raise Exception("Exception occurred while checking if element is present -->", e)

    def get_element_containing_text(self, locater_type_by, locate_identifier, text):
        elements = self.get_driver().find_elements(locater_type_by, value=locate_identifier)
        for element in elements:
            if text in (element.text or
                        element.get_attribute("textContent") or
                        element.get_attribute("innerText")):
                return element
        print("Element not found")
        return None

    # def alert(self):
    #     print("-----------------2--------------------")
    #     alert = self.get_driver().switch_to.alert
    #     print("-----------------3--------------------")
    #     # alert_text = alert.text
    #     print("-----------------4--------------------")
    #     # assert alert_text == "Use camera and microphone?"
    #     print("-----------------5--------------------")
    #     alert.accept()
    #     self.get_driver().switch_to.default_content()
