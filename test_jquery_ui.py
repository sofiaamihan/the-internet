import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os

class TestJQueryUI:

    @pytest.mark.jquery
    def test_jquery_ui(self, driver):

        driver.get("https://the-internet.herokuapp.com/jqueryui")

        link = driver.find_elements(By.XPATH, "//a")[2]
        link.click()

        assert driver.current_url == "https://the-internet.herokuapp.com/jqueryui/menu"

        enabled = driver.find_element(By.ID, "ui-id-3")
        downloads = driver.find_element(By.ID, "ui-id-4")
        pdf = driver.find_element(By.ID, "ui-id-5")

        actions = ActionChains(driver)
        actions.move_to_element(enabled).perform()

        wait = WebDriverWait(driver, 10)

        if wait.until(ec.visibility_of_element_located((By.ID, "ui-id-4"))):
            actions.move_to_element(downloads).perform()
            if wait.until(ec.visibility_of_element_located((By.ID, "ui-id-5"))):
                pdf.click()

        file_path = "/Users/sofiaamihan/Downloads/menu.pdf"

        timeout = 15
        while timeout > 0 and not os.path.exists(file_path):
            time.sleep(1)
            timeout -= 1

        assert os.path.isfile(file_path), f"File was not downloaded: {file_path}"