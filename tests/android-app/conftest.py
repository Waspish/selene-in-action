import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "deviceName": "Google Pixel 6",
        "platformVersion": "12.0",
        "app": "bs://sample.app",
        "bstack:options": {
            "projectName": "First Appium",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": "bsuser_jRfAn5",
            "accessKey": "RXY6Dy1zfcXqQstYyqQh",
        }
    })
    browser.config.driver = webdriver.Remote(
        "http://hub.browserstack.com/wd/hub", options=options
    )
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
