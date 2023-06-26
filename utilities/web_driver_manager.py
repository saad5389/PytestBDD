import pytest
from pytest import fixture
from config import Config
import configparser
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
import settings
from data import userdetails, route


# user_name = "saad5389"
# access_key = "rYFrmzea7jSoixjpTemFmPowyyjDZMZdgy2VtOdu6YRXEdFAOW"
# remote_url = "https://" + user_name + ":" + access_key + "@hub.lambdatest.com/wd/hub"

# chrome_caps = {
#     "single_test":
#         {
#             "browserName": "Chrome",
#             "browserVersion": "114.0",
#             "LT:Options": {
#                 "username": "saad5389",
#                 "accessKey": "rYFrmzea7jSoixjpTemFmPowyyjDZMZdgy2VtOdu6YRXEdFAOW",
#                 "platformName": "Windows 10",
#                 "headless": True,
#                 "build": "one",
#                 "project": "pythonProject11",
#                 "selenium_version": "4.0.0",
#                 "w3c": True
#             }
#         }
# }

# firefox_caps = {
#     "build": "2.0",
#     "name,": "lambdatest firefox",
#     "platformName": "Windows 10",
#     "browserName": "Firefox",
#     "browserVersion": "latest"
# }

# def before_scenario(self, request):
#     desired_caps = {}
#
#     if request.param == "chrome":
#         desired_caps.update(self.chrome_caps)
#         pytest.web_driver = webdriver.Remote(
#             command_executor=RemoteConnection(self.remote_url),
#             desired_capabilities={"LT: Options": desired_caps}
#         )
# elif request.param == "firefox":
#     desired_caps.update(self.firefox_caps)
#     pytest.web_driver = webdriver.Remote(
#         command_executor=RemoteConnection(self.remote_url),
#         desired_capabilities={"LT: Options": desired_caps}
#     )

# config = configparser.ConfigParser()
# config.read('config.ini')
# browser = config.get('browser', 'default')
# if browser == "chrome":
#     options = ChromeOptions()
#     # Add any Chrome-specific options if needed
#     pytest.web_driver = webdriver.Chrome(options=options)
#     # options.arguments('--headless')
#     # options.add_argument("--use-fake-ui-for-media-stream")
# elif browser == "firefox":
#     options = FirefoxOptions()
#     # Add any Firefox-specific options if needed
#     pytest.web_driver = webdriver.Firefox(options=options)
# else:
#     raise ValueError("Invalid browser specified")
#
# pytest.web_driver.maximize_window()
# pytest.web_driver.implicitly_wait(20)

def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


# def getEnv(request):
#     _env = request.config.getoption("--env")
#     return _env


def getDriver(request):
    browser = getBrowser(request)
    pytest.web_driver = None
    print("browser from getBrowser method - " + browser)

    if browser == "chrome":
        options = ChromeOptions()
        pytest.web_driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        pytest.web_driver = webdriver.Firefox(options=options)

    # env = getEnv(request)
    
    # if env == "devtp15":
    #     print("env selected by the user is " + env)
    #     pytest.web_driver.get(userdetails.devtp15 + route.site)
    # elif env == "qa":
    #     print("env selected by the user is " + env)
    #     pytest.web_driver.get(userdetails.qa + route.site)
    #
    # elif env == "staging":
    #     print("env selected by the user is " + env)
    #     pytest.web_driver.get(userdetails.stg + route.site)
    #
    # elif env == "preprod":
    #     print("env selected by the user is " + env)
    #     pytest.web_driver.get(userdetails.preprod + route.site)
    pytest.web_driver.implicitly_wait(20)
    pytest.web_driver.delete_all_cookies()
    pytest.web_driver.maximize_window()


def after_scenario():
    pytest.web_driver.quit()
