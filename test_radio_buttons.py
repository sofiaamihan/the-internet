from selenium.webdriver.common.by import By
import pytest

class TestRadioButtons:

    @pytest.mark.buttons
    def test_radio_buttons(self, driver):
        driver.get("https://formy-project.herokuapp.com/radiobutton")

        buttons = driver.find_elements(By.XPATH, "//input[@class='form-check-input']")

        buttons[1].click()

        assert not buttons[0].is_selected()
        assert buttons[1].is_selected()
        assert not buttons[2].is_selected()