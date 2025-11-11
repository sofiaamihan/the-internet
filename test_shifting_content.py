import pytest
from selenium.webdriver.common.by import By
import allure

class TestShiftingContent:

    @pytest.mark.content
    def test_menu(self, driver):

        # Load 1
        driver.get("https://the-internet.herokuapp.com/shifting_content/menu")
        gallery_menu = driver.find_element(By.XPATH, "//a[@class='shift']")
        x_coordinates = gallery_menu.rect['x']

        # Load 2
        driver.get("https://the-internet.herokuapp.com/shifting_content/menu?pixel_shift=100")
        gallery_menu_2 = driver.find_element(By.XPATH, "//a[@class='shift']")
        x_coordinates_2 = gallery_menu_2.rect['x']

        allure.attach(
            f"{x_coordinates} VS {x_coordinates_2}",
            name="Difference in coordinates",
            attachment_type=allure.attachment_type.TEXT
        )

        assert x_coordinates != x_coordinates_2