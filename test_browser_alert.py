from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestBrowserAlert:

    @pytest.mark.alert
    def test_right_click(self, driver):
        driver.get("https://the-internet.herokuapp.com/context_menu")
        box_locator = driver.find_element(By.XPATH, "//div[@id='hot-spot']")
        actions = ActionChains(driver)
        actions.context_click(box_locator).perform()
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.alert_is_present())

    @pytest.mark.alert
    def test_left_click(self, driver):
        driver.get("https://the-internet.herokuapp.com/context_menu")
        box_locator = driver.find_element(By.XPATH, "//div[@id='hot-spot']")
        box_locator.click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.none_of(ec.alert_is_present()))

    @pytest.mark.alert
    def test_read_text(self, driver):
        driver.get("https://the-internet.herokuapp.com/context_menu")
        box_locator = driver.find_element(By.XPATH, "//div[@id='hot-spot']")
        actions = ActionChains(driver)
        actions.context_click(box_locator).perform()
        wait = WebDriverWait(driver, 10)
        if wait.until(ec.alert_is_present()):
            alert = driver.switch_to.alert
            assert alert.text == "You selected a context menu"

