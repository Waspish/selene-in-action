import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities(
        {
            # Specify device and os_version for testing
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            # Set Url of the application under test
            "app": "bs://sample.app",
            # Browserstack capabilities
            'bstack:options': {
                "projectName": "First Appium",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                # Access credentials
                "userName": "bsuser_jRfAn5",
                "accessKey": "RXY6Dy1zfcXqQstYyqQh",
            },
        }
    )
    browser.config.driver = webdriver.Remote(
        "http://hub.browserstack.com/wd/hub", options=options
    )
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
