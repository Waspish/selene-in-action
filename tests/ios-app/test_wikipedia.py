from appium.webdriver.common.appiumby import AppiumBy
from selene import have, browser

def test_search():
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
    browser.element((AppiumBy.ID, "Text Input")).type(
        "Appium IOS"
    )
    browser.element((AppiumBy.ID, "Text Output")).should(have.text('Appium IOS'))

