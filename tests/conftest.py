import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs/todomvc/dist/'
    driver_options = webdriver.ChromeOptions()
    # driver_options = webdriver.FirefoxOptions()
    # driver_options.add_argument("--headless")
    browser.config.driver_options = driver_options
    yield  # test runs here
    browser.quit()


# @pytest.fixture()
# def driver():
#     driver_options = webdriver.ChromeOptions()
#     driver_options.add_argument('--headless')
#     chrome_driver = webdriver.Chrome(options=driver_options)
#     yield chrome_driver
#     chrome_driver.quit()
