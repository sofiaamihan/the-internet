import os.path
import pytest
from selenium import webdriver
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
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

@pytest.fixture()
def download_dir():
    path = "/Users/sofiaamihan/Downloads"
    if not os.path.exists(path):
        os.makedirs(path)
    return path

@allure.title("Setting up Driver")
@pytest.fixture()
def driver(download_dir):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.geolocation": 1
    })

    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()