import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestLogin:

    @pytest.mark.login
    def test_positive_login(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://the-internet.herokuapp.com/login")

        username = "tomsmith"
        password = "SuperSecretPassword!"

        username_input = driver.find_element(By.XPATH, "//input[@id='username']")
        username_input.send_keys(username)

        password_input = driver.find_element(By.XPATH, "//input[@id='password']")
        password_input.send_keys(password)

        login_button = driver.find_element(By.XPATH, "//form[@id='login']/button")
        login_button.click()

        success_alert = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='flash']")))
        assert success_alert.text.split('\n')[0] == "You logged into a secure area!"
        assert success_alert.is_displayed()
        assert driver.current_url == "https://the-internet.herokuapp.com/secure"

        logout_button = driver.find_element(By.XPATH, "//a[@class='button secondary radius']")
        logout_button.click()
        success_alert = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='flash']")))
        assert success_alert.text.split('\n')[0] == "You logged out of the secure area!"
        assert success_alert.is_displayed()
        assert driver.current_url == "https://the-internet.herokuapp.com/login"

    @pytest.mark.login
    @pytest.mark.parametrize("username, password, id", [
        ("", "", 1),
        ("tomsmith", "", 2),
        ("", "SuperSecretPassword!", 3)
    ], ids=["no-input", "wrong-password", "wrong-username"])
    def test_negative_login(self, driver, username, password, id):
        wait = WebDriverWait(driver, 10)
        driver.get("https://the-internet.herokuapp.com/login")

        username_input = driver.find_element(By.XPATH, "//input[@id='username']")
        username_input.send_keys(username)

        password_input = driver.find_element(By.XPATH, "//input[@id='password']")
        password_input.send_keys(password)

        login_button = driver.find_element(By.XPATH, "//form[@id='login']/button")
        login_button.click()

        error_alert = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='flash']")))
        assert error_alert.text.split('\n')[0] == "Your username is invalid!" or error_alert.text.split('\n')[0] == "Your password is invalid!"
        assert error_alert.is_displayed()

        allure.attach(
            f"ID {id}: Error Alert -  {error_alert.text}",
            name=f"ID_{id}",
            attachment_type=allure.attachment_type.TEXT
        )