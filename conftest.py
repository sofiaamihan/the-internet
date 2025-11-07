import pytest
from selenium import webdriver
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook is called after each test phase (setup, call, teardown)
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )

@allure.title("Setting up Driver")
@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()