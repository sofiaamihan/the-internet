import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import pytest

# TODO - visibility keeps showing true even if it isnt there. is visibiliy the view port or the entire page height or what deems it not visible
# TODO - incremental scroll height checks, so for every scroll check that the height has increased as well
# TODO - maybe i could also check that there is new and different content generating each time

def is_in_viewport(driver, element):
    return driver.execute_script("""
        const rect = arguments[0].getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    """, element)

class TestInfiniteScroll:

    @pytest.mark.scroll
    def test_infinite_scroll(self, driver):
        driver.get("https://the-internet.herokuapp.com/infinite_scroll")

        # Check original scroll height
        initial_height = driver.execute_script("return document.body.scrollHeight")

        # Title should be visible
        assert ec.visibility_of_element_located((By.TAG_NAME, "h3"))

        # Content to load
        time.sleep(1)

        # Scroll past title
        actions = ActionChains(driver)
        actions.scroll_by_amount(0, 800).perform()
        time.sleep(1)
        actions.scroll_by_amount(0, 800).perform()
        time.sleep(1)
        actions.scroll_by_amount(0, 800).perform()
        time.sleep(1)

        # Title should not be visible
        title = driver.find_element(By.TAG_NAME, "h3")
        assert not is_in_viewport(driver, title)

        # Scroll height should have increased
        new_height = driver.execute_script("return document.body.scrollHeight")
        assert initial_height < new_height


