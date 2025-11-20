from selenium.webdriver.common.by import By
import pytest

class TestDatePicker:

    @pytest.mark.datepicker
    def test_date_picker(self, driver):
        driver.get("https://formy-project.herokuapp.com/datepicker")

        input_locator = driver.find_element(By.XPATH, "//input[@id='datepicker']")
        input_locator.click()

        date_locator = driver.find_element(By.CSS_SELECTOR, "td[data-date='1762819200000']")
        date_locator.click()

        populated_value = input_locator.get_attribute("value")
        assert populated_value == "11/11/2025"