from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import allure
import pytest

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

    @pytest.mark.elements
    def test_styles_elements(self, driver):
        driver.get("https://the-internet.herokuapp.com/disappearing_elements")

        elements = driver.find_elements(By.XPATH, "//div[@class='example']/ul/li/a")
        home_element = elements[0]

        allure.attach(
            f"Colour of element: {home_element.value_of_css_property('color')}",
             name=f"Colour",
             attachment_type=allure.attachment_type.TEXT
        )

        assert home_element.value_of_css_property('color') == "rgba(218, 75, 75, 1)"

        actions = ActionChains(driver)
        actions.move_to_element(home_element).perform()

        allure.attach(
            f"Colour of element: {home_element.value_of_css_property('color')}",
            name=f"Colour",
            attachment_type=allure.attachment_type.TEXT
        )

        assert home_element.value_of_css_property('color') == "rgba(0, 0, 0, 1)"