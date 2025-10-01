from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, browser

def test_search():

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            "Appium"
        )

    with step('Verify content found'):
        search_results = browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        )
        search_results.should(have.size_greater_than(0))
        search_results.first.should(have.text('Appium'))

