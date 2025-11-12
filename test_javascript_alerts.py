from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest

class TestJavascriptAlerts:

    @pytest.mark.alerts
    def test_js_alert(self, driver):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        buttons = driver.find_elements(By.XPATH, "//ul/li/button")
        alert_button = buttons[0]
        alert_button.click()

        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.alert_is_present())

        # Click Alert
        alert = driver.switch_to.alert
        alert.accept()

        result = driver.find_element(By.XPATH, "//p[@id='result']").text
        assert result == "You successfully clicked an alert"

    @pytest.mark.alerts
    def test_js_confirm(self, driver):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        buttons = driver.find_elements(By.XPATH, "//ul/li/button")
        confirm_button = buttons[1]

        # Accept
        confirm_button.click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        result = driver.find_element(By.XPATH, "//p[@id='result']").text
        assert result == "You clicked: Ok"

        # Dismiss
        confirm_button.click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.alert_is_present())
        alert = driver.switch_to.alert
        alert.dismiss()
        result = driver.find_element(By.XPATH, "//p[@id='result']").text
        assert result == "You clicked: Cancel"

    @pytest.mark.alerts
    def test_js_prompt(self, driver):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        buttons = driver.find_elements(By.XPATH, "//ul/li/button")
        prompt_button = buttons[2]
        prompt_button.click()

        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.alert_is_present())

        alert = driver.switch_to.alert
        alert.send_keys("Testing")
        alert.accept()

        result = driver.find_element(By.XPATH, "//p[@id='result']").text
        assert result == "You entered: Testing"