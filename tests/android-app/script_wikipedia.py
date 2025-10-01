from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
options = UiAutomator2Options().load_capabilities(
    {
        # Specify device and os_version for testing
        "platformName": "android-app",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": "bs://sample.app",
        # Add your caps here
        'bstack:options': {
            "projectName": "First Appium",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": "bsuser_jRfAn5",
            "accessKey": "RXY6Dy1zfcXqQstYyqQh",
        },
    }
)
driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

# Test case for the BrowserStack sample Android app.
# If you have uploaded your app, update the test case here.
search_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
)
search_element.click()
search_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
)
search_input.send_keys("BrowserStack")
time.sleep(5)
search_results = driver.find_elements(
    AppiumBy.CLASS_NAME, "android-app.widget.TextView"
)
assert len(search_results) > 0

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
