import pytest
from datetime import datetime
from pathlib import Path
from utilities.mobile_driver_manager import DriverManager
from utilities.web_driver_manager import after_scenario, getDriver
import settings


@pytest.fixture(scope='package')
def setup_teardown():
    mobile_driver_manager = DriverManager()
    mobile_driver_manager.setup_driver()
    yield
    mobile_driver_manager.teardown_driver()


@pytest.fixture(scope='package')
def web_driver(request):
    getDriver(request)
    yield
    after_scenario()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=settings.browser)
    parser.addoption("--env", action="store", default=settings.env)


# @pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now()
    reports_dir = Path('reports', now.strftime('%Y%m%d'))  # create report target dir
    reports_dir.mkdir(parents=True, exist_ok=True)  # custom report file
    report = reports_dir / f"report_{now.strftime('%H%M')}.html"  # adjust plugin options
    config.option.htmlpath = report
    config.option.self_contained_html = True
