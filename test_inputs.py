import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestInputs:

    @pytest.mark.inputs
    def test_number_inputs(self, driver):
        driver.get("https://the-internet.herokuapp.com/inputs")
        actions = ActionChains(driver)
        input_locator = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
        input_locator.send_keys("3")
        for i in range(3):
            actions.key_down(Keys.ARROW_UP).perform()
        assert input_locator.get_attribute("value") == "6"
        for i in range(7):
            actions.key_down(Keys.ARROW_DOWN).perform()
        assert input_locator.get_attribute("value") == "-1"

    @pytest.mark.inputs
    def test_letter_inputs(self, driver):
        driver.get("https://the-internet.herokuapp.com/inputs")
        input_locator = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
        input_locator.send_keys("abc")
        assert input_locator.get_attribute("value") == ""
