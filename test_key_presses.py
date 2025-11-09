from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import pytest

class TestKeyPresses:

    @pytest.mark.keys
    def test_letter_keys(self, driver):
        driver.get("https://the-internet.herokuapp.com/key_presses")

        input_locator = driver.find_element(By.XPATH, "//input[@id='target']")
        input_locator.send_keys("Q")

        result_locator = driver.find_element(By.XPATH, "//p[@id='result']")
        assert result_locator.text == "You entered: Q"

    @pytest.mark.keys
    def test_number_keys(self, driver):
        driver.get("https://the-internet.herokuapp.com/key_presses")

        # Focus on element
        input_locator = driver.find_element(By.XPATH, "//input[@id='target']")
        input_locator.click()

        actions = ActionChains(driver)
        actions.key_down(Keys.NUMPAD2).perform()

        result_locator = driver.find_element(By.XPATH, "//p[@id='result']")
        # assert result_locator.text == "You entered: 2"
        assert result_locator.text == "You entered: NUMPAD2"

    @pytest.mark.keys
    def test_general_keys(self, driver):
        driver.get("https://the-internet.herokuapp.com/key_presses")

        # Focus on element
        input_locator = driver.find_element(By.XPATH, "//input[@id='target']")
        input_locator.click()

        actions = ActionChains(driver)
        actions.key_down(Keys.TAB).perform()

        result_locator = driver.find_element(By.XPATH, "//p[@id='result']")
        assert result_locator.text == "You entered: TAB"
