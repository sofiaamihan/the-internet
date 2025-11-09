from selenium.webdriver.common.by import By
import pytest

class TestDeepDom:

    @pytest.mark.dom
    def test_table(self, driver):
        driver.get("https://the-internet.herokuapp.com/large")
        items = driver.find_elements(By.XPATH, "//td[contains(text(), '5.11')]")
        assert items[0].text == "5.11"

    @pytest.mark.dom
    def test_list(self, driver):
        driver.get("https://the-internet.herokuapp.com/large")
        item = driver.find_element(By.XPATH, "//div[@id='sibling-23.3']")
        assert item.text == "23.3"
