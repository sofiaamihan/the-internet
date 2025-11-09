from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
import pytest

class TestHovers:

    @pytest.mark.hovers
    def test_hovers(self, driver):
        driver.get("https://the-internet.herokuapp.com/hovers")
        wait = WebDriverWait(driver, 10)

        images = driver.find_elements(By.CSS_SELECTOR, "img[src='/img/avatar-blank.jpg']")

        image1 = images[0]
        actions = ActionChains(driver)
        actions.move_to_element(image1).perform()
        assert wait.until(visibility_of_element_located((By.XPATH, "//div[@class='figure'][1]//h5")))

        image2 = images[1]
        actions = ActionChains(driver)
        actions.move_to_element(image2).perform()
        assert wait.until(visibility_of_element_located((By.XPATH, "//div[@class='figure'][2]//h5")))

        image3 = images[2]
        actions = ActionChains(driver)
        actions.move_to_element(image3).perform()
        assert wait.until(visibility_of_element_located((By.XPATH, "//div[@class='figure'][3]//h5")))
