import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest

def is_in_viewport(driver, element):
    return driver.execute_script("""
        const rect = arguments[0].getBoundingClientRect();
        return(
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.bottom <= (window.innerWidth || document.documentElement.clientWidth) 
        );
    """, element)

class TestFloatingMenu:

    @pytest.mark.menu
    def test_floating_menu(self, driver):
        driver.get("https://the-internet.herokuapp.com/floating_menu")

        # Title
        title = driver.find_element(By.TAG_NAME, "h3")

        # Floating Menu
        floating_menu = driver.find_element(By.XPATH, "//div[@id='menu']")

        # Scroll
        actions = ActionChains(driver)
        # actions.scroll_by_amount(0,1200).perform()
        actions.scroll_by_amount(0, 800).perform()
        time.sleep(1)
        actions.scroll_by_amount(0, 800).perform()
        time.sleep(1)

        # Title should not be visible
        assert not is_in_viewport(driver, title)
        # assert not title.is_displayed() --> This does not work

        # Floating Menu should be visible
        assert floating_menu.is_displayed()
        # assert is_in_viewport(driver, floating_menu) --> This does not work