from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest

class TestDragAndDrop:

    @pytest.mark.dragdrop
    def test_drag_and_drop(self, driver):
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")

        element_a = driver.find_element(By.XPATH, "//div[@id='column-a']")
        element_b = driver.find_element(By.XPATH, "//div[@id='column-b']")

        actions = ActionChains(driver)
        actions.drag_and_drop(element_a, element_b).perform()

        headers = driver.find_elements(By.XPATH, "//div[@id='columns']/div/header")
        assert headers[0].text == "B"