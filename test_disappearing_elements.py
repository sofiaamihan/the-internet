from selenium.webdriver.common.by import By
import allure
import pytest

# TODO - experimenting with styles, how to check the css
# TODO - elements that appear on a screen for a fixed amount of time, check that too

class TestDisappearingElements:

    @pytest.mark.elements
    def test_disappearing_elements(self, driver):
        driver.get("https://the-internet.herokuapp.com/disappearing_elements")

        for i in range(5):
            driver.refresh()
            elements = driver.find_elements(By.XPATH, "//div[@class='example']/ul/li")
            length = len(elements)
            element_texts = [e.text for e in elements]

            allure.attach(
                f"Iteration {i + 1}: Number of elements = {length}\nElements: {element_texts}",
                name=f"Iteration_{i + 1}",
                attachment_type=allure.attachment_type.TEXT
            )

            assert length >= 4, f"Expected at least 4 elements, found {length}"