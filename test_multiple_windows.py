from selenium.webdriver.common.by import By
import pytest

class TestMultipleWindows:

    @pytest.mark.windows
    def test_multiple_windows(self, driver):
        driver.get("https://the-internet.herokuapp.com/windows")

        link = driver.find_element(By.XPATH, "//a[contains(text(), 'Click Here')]")
        link.click()

        windows = driver.window_handles
        assert len(windows) == 2 # 2 windows are present but selenium will not automatically switch

        driver.switch_to.window(windows[1])

        assert driver.current_url == "https://the-internet.herokuapp.com/windows/new"