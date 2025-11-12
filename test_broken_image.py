import pytest
from selenium.webdriver.common.by import By

class TestBrokenImages:

    @pytest.mark.image
    def test_broken_images(self, driver):
        driver.get("https://the-internet.herokuapp.com/broken_images")
        images = driver.find_elements(By.XPATH, "//div[@id='content']/div[@class='example']/img")

        image_1_has_loaded = driver.execute_script("return arguments[0].complete && arguments[0].naturalWidth > 0;", images[0])
        image_2_has_loaded = driver.execute_script("return arguments[0].complete && arguments[0].naturalWidth > 0;", images[1])
        image_3_has_loaded = driver.execute_script("return arguments[0].complete && arguments[0].naturalWidth > 0;", images[2])

        assert [True if image_1_has_loaded == False else False]
        assert [True if image_2_has_loaded == False else False]
        assert image_3_has_loaded