import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TestDropdown:

    @pytest.mark.dropdown
    def test_dropdown_option1(self, driver):
        driver.get("https://the-internet.herokuapp.com/dropdown")
        dropdown_locator = driver.find_element(By.XPATH, "//select[@id='dropdown']")
        select = Select(dropdown_locator)
        select.select_by_value("1")
        option1 = driver.find_elements(By.XPATH, "//select[@id='dropdown']/option")[1]
        assert option1.is_selected()

    @pytest.mark.dropdown
    def test_dropdown_option2(self, driver):
        driver.get("https://the-internet.herokuapp.com/dropdown")
        dropdown_locator = driver.find_element(By.XPATH, "//select[@id='dropdown']")
        select = Select(dropdown_locator)
        select.select_by_value("2")
        option2 = driver.find_elements(By.XPATH, "//select[@id='dropdown']/option")[2]
        assert option2.is_selected()
