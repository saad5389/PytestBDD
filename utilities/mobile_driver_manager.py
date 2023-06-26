from appium import webdriver as appium_webdriver
import pytest


class DriverManager:
    def __init__(self):
        pytest.mobile_driver = None

    def setup_driver(self):
        caps = {
            'platformName': 'Android',
            'platformVersion': '11.0',
            'deviceName': 'Pixel 5 API 30',
            'appPath': "D:/abc.apk",
            'app': "D:/abc.apk",
            'no-reset': False,
            'full-reset': True,
            'autoGrantPermissions': True,
            # Add other desired capabilities
        }
        # Initialize the driver
        pytest.mobile_driver = appium_webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        # Add necessary configurations and desired capabilities

    def teardown_driver(self):
        if pytest.mobile_driver is not None:
            pytest.mobile_driver.quit()
