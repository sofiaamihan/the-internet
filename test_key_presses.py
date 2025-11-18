import sys

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
    def test_capital_letters_keys(self, driver):
        driver.get("https://the-internet.herokuapp.com/key_presses")

        input_locator = driver.find_element(By.XPATH, "//input[@id='target']")

        actions = ActionChains(driver)
        actions.key_down(Keys.SHIFT).perform()
        input_locator.send_keys("abc")

        results = driver.find_element(By.XPATH, "//input[@id='target']").get_attribute("value")
        assert results == "ABC"

    @pytest.mark.keys
    def test_copy_and_paste(self, driver):
        driver.get("https://the-internet.herokuapp.com/key_presses")
        cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        actions = ActionChains(driver)

        input_locator = driver.find_element(By.XPATH, "//input[@id='target']")
        input_locator.send_keys('hi')

        actions.key_down(Keys.SHIFT).key_down(Keys.ARROW_UP).perform()
        actions.key_down(cmd_ctrl).send_keys("c").perform()
        actions.key_down(Keys.DELETE).perform()
        actions.key_down(cmd_ctrl).send_keys("v").perform()
        actions.key_down(cmd_ctrl).send_keys("v").perform()

        results = driver.find_element(By.XPATH, "//input[@id='target']").get_attribute("value")
        assert results == "hihi"

    def test_forward_backward(self, driver):
        driver.get("https://the-internet.herokuapp.com/inputs")
        driver.get("https://the-internet.herokuapp.com/key_presses")

        actions = ActionChains(driver)
        assert len(driver.window_handles) == 2


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
