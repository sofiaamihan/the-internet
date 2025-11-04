import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestAddRemoveElements:

    @pytest.mark.add
    def test_add_element(self, driver):
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        add_locator = driver.find_element(By.XPATH, "//div[@class='example']/button")
        add_locator.click()
        element_locator = driver.find_element(By.XPATH, "//div[@id='elements']/button")
        assert element_locator.is_displayed()

    @pytest.mark.remove
    def test_remove_element(self, driver):
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        add_locator = driver.find_element(By.XPATH, "//div[@class='example']/button")
        add_locator.click()
        element_locator = driver.find_element(By.XPATH, "//div[@id='elements']/button")
        element_locator.click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located((By.XPATH, "//div[@id='elements']/button")))