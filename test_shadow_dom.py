from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestShadowDOM:

    @pytest.mark.dom
    def test_shadow_dom(self, driver):
        driver.get("https://the-internet.herokuapp.com/shadowdom")

        # Alternative
        # line_1 = driver.find_element(By.XPATH, "//span[@slot='my-text']").text

        line_1 = driver.find_element(By.CSS_SELECTOR, "span[slot='my-text']").text
        assert line_1 == "Let's have some different text!"

        line_2 = driver.find_elements(By.CSS_SELECTOR, "ul[slot='my-text']")[0].text.split('\n')[0]
        assert line_2 == "Let's have some different text!"

        line_3 = driver.find_elements(By.CSS_SELECTOR, "ul[slot='my-text']")[0].text.split('\n')[1]
        assert line_3 == "In a list!"

    def test_shadow_dom2(self, driver):
        driver.get("https://practice.expandtesting.com/shadowdom")
        wait = WebDriverWait(driver, 10)

        # 1 - Get Parent Id
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='shadow-host']")))
        parent = driver.find_element(By.XPATH, "//div[@id='shadow-host']")

        # 2 - Get Shadow DOM via JS
        shadow = parent.shadow_root

        # 3 - Access hidden element
        hidden = shadow.find_element(By.ID, "my-btn")

        assert hidden.is_displayed()