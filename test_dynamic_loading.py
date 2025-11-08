import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# TODO - locate something using the source link

class TestDynamicLoading:

    @pytest.mark.dynamic
    def test_dynamic_hidden_loading(self, driver):
        driver.get("https://the-internet.herokuapp.com/dynamic_loading")

        link = driver.find_elements(By.XPATH, "//div[@class='example']/a")[0]
        link.click()
        assert driver.current_url == "https://the-internet.herokuapp.com/dynamic_loading/1"

        assert ec.invisibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
        button = driver.find_element(By.XPATH, "//div[@id='start']/button")
        button.click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4")))

    @pytest.mark.dynamic
    def test_dynamic_rendered_loading(self, driver):
        driver.get("https://the-internet.herokuapp.com/dynamic_loading")

        link = driver.find_elements(By.XPATH, "//div[@class='example']/a")[1]
        link.click()
        assert driver.current_url == "https://the-internet.herokuapp.com/dynamic_loading/2"

        button = driver.find_element(By.XPATH, "//div[@id='start']/button")
        button.click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='finish']/h4")))