from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import pytest

class TestHorizontalSlider:

    @pytest.mark.slider
    def test_slider_clicks(self, driver):
        driver.get("https://the-internet.herokuapp.com/horizontal_slider")

        # Find Slider
        slider = driver.find_element(By.XPATH, "//div[@class='sliderContainer']/input")
        width = slider.size["width"]

        # Move to beginning of Slider then click
        actions = ActionChains(driver)
        actions.move_to_element(slider).perform() # Centralise the mouse within the element first
        actions.move_by_offset((width / 2 * -1), 0).click()

        # Start of Slider value
        value = driver.find_element(By.XPATH, "//span[@id='range']")
        assert value.text == "0"

        # Increase value by one click
        actions.key_down(Keys.ARROW_RIGHT).perform()

        value = driver.find_element(By.XPATH, "//span[@id='range']")
        assert value.text == "0.5"

    @pytest.mark.slider
    def test_slider_mouse(self, driver):
        driver.get("https://the-internet.herokuapp.com/horizontal_slider")

        # Find Slider
        slider = driver.find_element(By.XPATH, "//div[@class='sliderContainer']/input")
        width = slider.size["width"]

        # Move to beginning of Slider
        actions = ActionChains(driver)
        actions.move_to_element(slider).perform()  # Centralise the mouse within the element first
        actions.move_by_offset((width / 2 * -1), 0).perform()

        # Start of Slider value
        value = driver.find_element(By.XPATH, "//span[@id='range']")
        assert value.text == "0"

        # Click and drag to increase value
        # STEP = 1 OFFSET. You can use width/2 if there's no step
        actions.click_and_hold(slider).move_by_offset(5, 0).release().perform()

        value = driver.find_element(By.XPATH, "//span[@id='range']")
        assert value.text == "2.5"