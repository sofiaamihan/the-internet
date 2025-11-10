from selenium.webdriver.common.by import By
import pytest

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