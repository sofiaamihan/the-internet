from selenium.webdriver.common.by import By
import pytest

class TestNestedFrames:

    @pytest.mark.frames
    def test_nested_frames(self, driver):
        driver.get("https://the-internet.herokuapp.com/nested_frames")

        driver.get("https://the-internet.herokuapp.com/frame_right")
        text = driver.find_element(By.TAG_NAME, "body").text
        assert text == "RIGHT"

        driver.get("https://the-internet.herokuapp.com/frame_left")
        text = driver.find_element(By.TAG_NAME, "body").text
        assert text == "LEFT"

        driver.get("https://the-internet.herokuapp.com/frame_middle")
        text = driver.find_element(By.TAG_NAME, "body").text
        assert text == "MIDDLE"

        driver.get("https://the-internet.herokuapp.com/frame_bottom")
        text = driver.find_element(By.TAG_NAME, "body").text
        assert text == "BOTTOM"

    def test_nested_frames2(self, driver):
        driver.get("https://the-internet.herokuapp.com/nested_frames")

        driver.switch_to.frame("frame-top")
        driver.switch_to.frame("frame-middle")
        text = driver.find_element(By.ID, "content").text
        assert text == "MIDDLE"

        driver.switch_to.default_content()

        driver.switch_to.frame("frame-top")
        driver.switch_to.frame("frame-left")
        text = driver.find_element(By.TAG_NAME, "body").text
        assert text == "LEFT"

        driver.switch_to.default_content()

        driver.switch_to.frame("frame-top")
        driver.switch_to.frame("frame-right")
        text = driver.find_element(By.TAG_NAME, "body").text
        assert text == "RIGHT"

        driver.switch_to.default_content()

        driver.switch_to.frame("frame-bottom")
        text = driver.find_element(By.TAG_NAME, "body").text
        assert text == "BOTTOM"


