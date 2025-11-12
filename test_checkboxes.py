from selenium.webdriver.common.by import By
import pytest

class TestCheckboxes:

    @pytest.mark.checkboxes
    def test_first_checkbox(self, driver):
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = driver.find_elements(By.XPATH, "//form[@id='checkboxes']/input")
        checkboxes[0].click()
        assert checkboxes[0].is_selected()
        assert checkboxes[1].is_selected()

    @pytest.mark.checkboxes
    def test_second_checkbox(self, driver):
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = driver.find_elements(By.XPATH, "//form[@id='checkboxes']/input")
        checkboxes[1].click()
        assert [True if checkboxes[0].is_selected() == False else False]
        assert [True if checkboxes[1].is_selected() == False else False]

    @pytest.mark.checkboxes
    def test_checkboxes(self, driver):
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = driver.find_elements(By.XPATH, "//form[@id='checkboxes']/input")
        checkboxes[0].click()
        checkboxes[1].click()
        assert checkboxes[0].is_selected()
        assert [True if checkboxes[1].is_selected() == False else False]
