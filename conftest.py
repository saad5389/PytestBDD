from selenium import webdriver
import time
import settings
import pytest
from datetime import datetime
from pathlib import Path


# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default=settings.browser)
#     parser.addoption("--env", action="store", default=settings.env)

#
# @pytest.fixture(scope='session')
# def getBrowser(request):
#     _browser = request.config.getoption("--browser")
#     return _browser

#
# @pytest.fixture(scope='session')
# def getenv(request):
#     _env = request.config.getoption("--env")
#     return _env


# @pytest.fixture(scope='session')
# def getDriver(request, browser, getenv):
#     _driver = None
#     print("browser from getBrowser method - " + browser)
#
#     if browser == "chrome":
#         _driver = webdriver.Chrome("./ChromeDriver/chromedriver.exe")
#
#     elif browser == "firefox":
#         _driver = webdriver.Firefox('./FirefoxDriver/geckodriver.exe')
#
#     if getenv == "qa":
#         print("env selected by the user is " + getenv)
#         _driver.get("https://one-sites-qa.avizia.com/#/login")
#
#     elif getenv == "staging":
#         print("env selected by the user is " + getenv)
#         _driver.get("https://one-sites-stg.avizia.com/#/login")
#
#     elif getenv == "preprod":
#         print("env selected by the user is " + getenv)
#         _driver.get("https://one-sites-pre-prod.avizia.com/#/site")
#     _driver.maximize_window()
#     _driver.implicitly_wait(20)
#     request.cls.driver = _driver
#     _driver.delete_all_cookies()
#     yield request.cls.driver
#     time.sleep(2)
#     request.cls.driver.quit()


# Only Chrome browser executable
# @fixture(params=[webdriver.Chrome])
# def browser(request):
#     driver = request.param
#     browsers = driver("ChromeDriver/chromedriver.exe")
#     yield browsers
#     browsers.quit()


@pytest.fixture
def browser():
    browsers = webdriver.Chrome('ChromeDriver/chromedriver.exe')
    browsers.implicitly_wait(10)
    yield browsers


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # set custom options only if none are provided from command line
    now = datetime.now()
    # create report target dir
    reports_dir = Path('reports', now.strftime('%Y%m%d'))
    reports_dir.mkdir(parents=True, exist_ok=True)
    # custom report file
    report = reports_dir / f"report_{now.strftime('%H%M')}.html"
    # adjust plugin options
    config.option.htmlpath = report
    config.option.self_contained_html = True
