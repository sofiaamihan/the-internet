from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import pytest

class TestEntryModal:

    @pytest.mark.modal
    def test_entry_modal(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://the-internet.herokuapp.com/entry_ad")

        # Visible on first load
        modal = wait.until(ec.visibility_of_element_located((By.ID, "modal")))
        assert modal.is_displayed()

        # Close modal
        close_button = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@class='modal-footer']/p")))
        close_button.click()

        # Modal should no longer be visible
        assert wait.until(ec.invisibility_of_element_located((By.XPATH, "//div[@id='modal']")))
        # Alternative 1 ---
        # assert ec.invisibility_of_element_located((By.XPATH, "//div[@id='modal']"))
        # Alternative 2 ---
        # wait.until(lambda d: not modal.is_displayed())
        # assert not modal.is_displayed()

        # Refresh, get new element reference
        driver.refresh()
        new_modal = driver.find_element(By.XPATH, "//div[@id='modal']")

        # Modal remains hidden after refresh
        assert not new_modal.is_displayed()
        assert wait.until(ec.presence_of_element_located((By.ID, "modal")))
