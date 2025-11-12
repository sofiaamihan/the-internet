from selenium.webdriver.common.by import By
import pytest

class TestDynamicContent:

    @pytest.mark.dynamic
    def test_dynamic_content_all(self, driver):
        """Not Dynamic but works fine for optional assertions."""
        driver.get("https://the-internet.herokuapp.com/dynamic_content")
        rows = driver.find_elements(By.XPATH, "//div[@class='large-10 columns']")
        row1 = rows[0].text
        row2 = rows[1].text
        row3 = rows[2].text
        pictures = driver.find_elements(By.XPATH, "//div[@class='large-2 columns']/img")
        pic1 = pictures[0].get_attribute("src")
        pic2 = pictures[1].get_attribute("src")
        pic3 = pictures[2].get_attribute("src")
        driver.refresh()
        rows = driver.find_elements(By.XPATH, "//div[@class='large-10 columns']")
        row1_new = rows[0].text
        row2_new = rows[1].text
        row3_new = rows[2].text
        pictures = driver.find_elements(By.XPATH, "//div[@class='large-2 columns']/img")
        pic1_new = pictures[0].get_attribute("src")
        pic2_new = pictures[1].get_attribute("src")
        pic3_new = pictures[2].get_attribute("src")
        assert row1 != row1_new or row2 != row2_new or row3 != row3_new
        assert pic1 != pic1_new or pic2 != pic2_new or pic3 != pic3_new

    @pytest.mark.dynamic
    def test_static_content(self, driver):
        """Ensures that the first 2 content boxes remain constant throughout reloads."""
        driver.get("https://the-internet.herokuapp.com/dynamic_content?with_content=static")
        rows = driver.find_elements(By.XPATH, "//div[@class='large-10 columns']")
        row1 = rows[0].text
        row2 = rows[1].text
        pictures = driver.find_elements(By.XPATH, "//div[@class='large-2 columns']/img")
        pic1 = pictures[0].get_attribute("src")
        pic2 = pictures[1].get_attribute("src")
        driver.refresh()
        rows = driver.find_elements(By.XPATH, "//div[@class='large-10 columns']")
        row1_new = rows[0].text
        row2_new = rows[1].text
        pictures = driver.find_elements(By.XPATH, "//div[@class='large-2 columns']/img")
        pic1_new = pictures[0].get_attribute("src")
        pic2_new = pictures[1].get_attribute("src")
        assert row1 == row1_new
        assert row2 == row2_new
        assert pic1 == pic1_new
        assert pic2 == pic2_new