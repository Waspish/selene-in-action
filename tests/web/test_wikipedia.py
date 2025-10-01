import time

from allure_commons._allure import step
from selene import have, browser, be



def test_search():
    browser.open('/')

    with step('Change language to English'):
        browser.element('#searchLanguage [value="en"]').click()

    with step('Type search'):
        browser.element('#searchInput').type('Appium')

    with step('Verify content found'):
        search_results = browser.all('.suggestion-link')
        search_results.should(have.size_greater_than(0))
        search_results.first.should(have.text('Appium'))

