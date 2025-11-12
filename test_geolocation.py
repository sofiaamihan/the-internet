from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest

class TestGeolocation:

    @pytest.mark.geo
    def test_geolocation(self):
        options = Options()
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.geolocation": 1  # allow
        })

        driver = webdriver.Chrome(options=options)
        driver.get("https://the-internet.herokuapp.com/geolocation")

        button = driver.find_element(By.XPATH, "//button")
        button.click()

        wait = WebDriverWait(driver, 10)
        latitude = wait.until(ec.visibility_of_element_located((By.ID, "lat-value"))).text
        longitude = wait.until(ec.visibility_of_element_located((By.ID, "long-value"))).text

        google = driver.find_elements(By.XPATH, "//a")[1]
        google.click()

        google_coords = wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='bwoZTb fontBodyMedium']/span"))).text.split(', ')
        google_lat = google_coords[0][:5]
        google_long = google_coords[1][:5]

        assert google_lat in latitude
        assert google_long in longitude