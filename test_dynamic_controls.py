from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestDynamicControls:

    @pytest.mark.dynamic
    def test_add_checkbox(self, driver):
        driver.get("https://the-internet.herokuapp.com/dynamic_controls")
        checkbox = driver.find_element(By.XPATH, "//div[@id='checkbox']/input")
        checkbox.click()
        assert checkbox.is_selected()
        remove = driver.find_element(By.XPATH, "//form[@id='checkbox-example']/button")
        remove.click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located((By.XPATH, "//div[@id='checkbox']/input")))
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']")))
        if wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']"))):
            remove_message = driver.find_element(By.XPATH, "//p[@id='message']").text
            assert remove_message == "It's gone!"

    @pytest.mark.dynamic
    def test_remove_checkbox(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.get("https://the-internet.herokuapp.com/dynamic_controls")
        checkbox = driver.find_element(By.XPATH, "//div[@id='checkbox']/input")
        checkbox.click()
        assert checkbox.is_selected()

        remove = driver.find_element(By.XPATH, "//form[@id='checkbox-example']/button")
        remove.click()
        assert wait.until(ec.invisibility_of_element_located((By.XPATH, "//div[@id='checkbox']/input")))
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']")))
        if wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']"))):
            remove_message = driver.find_element(By.XPATH, "//p[@id='message']").text
            assert remove_message == "It's gone!"

        add = driver.find_element(By.XPATH, "//form[@id='checkbox-example']/button")
        add.click()
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']")))
        if wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']"))):
            remove_message = driver.find_element(By.XPATH, "//p[@id='message']").text
            assert remove_message == "It's back!"
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//input[@id='checkbox']")))

    @pytest.mark.dynamic
    def test_add_remove_checkbox_twice(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.get("https://the-internet.herokuapp.com/dynamic_controls")
        checkbox = driver.find_element(By.XPATH, "//div[@id='checkbox']/input")
        checkbox.click()
        assert checkbox.is_selected()

        remove = driver.find_element(By.XPATH, "//form[@id='checkbox-example']/button")
        remove.click()
        assert wait.until(ec.invisibility_of_element_located((By.XPATH, "//div[@id='checkbox']/input")))
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']")))
        if wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']"))):
            remove_message = driver.find_element(By.XPATH, "//p[@id='message']").text
            assert remove_message == "It's gone!"

        add = driver.find_element(By.XPATH, "//form[@id='checkbox-example']/button")
        add.click()
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']")))
        if wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']"))):
            remove_message = driver.find_element(By.XPATH, "//p[@id='message']").text
            assert remove_message == "It's back!"
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//input[@id='checkbox']")))

        remove = driver.find_element(By.XPATH, "//form[@id='checkbox-example']/button")
        remove.click()
        assert wait.until(ec.invisibility_of_element_located((By.XPATH, "//input[@id='checkbox']")))
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']")))
        if wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']"))):
            remove_message = driver.find_element(By.XPATH, "//p[@id='message']").text
            assert remove_message == "It's gone!"

        add = driver.find_element(By.XPATH, "//form[@id='checkbox-example']/button")
        add.click()
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']")))
        if wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']"))):
            remove_message = driver.find_element(By.XPATH, "//p[@id='message']").text
            assert remove_message == "It's back!"
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//input[@id='checkbox']")))

    @pytest.mark.dynamic
    def test_enable(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.get("https://the-internet.herokuapp.com/dynamic_controls")
        enable = driver.find_element(By.XPATH, "//form[@id='input-example']/button")
        enable.click()

        assert wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']")))
        if wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']"))):
            remove_message = driver.find_element(By.XPATH, "//p[@id='message']").text
            assert remove_message == "It's enabled!"
        input_locator = driver.find_element(By.XPATH, "//form[@id='input-example']/input")
        assert input_locator.is_enabled()

    @pytest.mark.dynamic
    def test_disable(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.get("https://the-internet.herokuapp.com/dynamic_controls")
        enable = driver.find_element(By.XPATH, "//form[@id='input-example']/button")
        enable.click()

        assert wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']")))
        if wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']"))):
            remove_message = driver.find_element(By.XPATH, "//p[@id='message']").text
            assert remove_message == "It's enabled!"
        input_locator = driver.find_element(By.XPATH, "//form[@id='input-example']/input")
        assert input_locator.is_enabled()

        disable = driver.find_element(By.XPATH, "//form[@id='input-example']/button")
        disable.click()
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']")))
        if wait.until(ec.presence_of_element_located((By.XPATH, "//p[@id='message']"))):
            remove_message = driver.find_element(By.XPATH, "//p[@id='message']").text
            assert remove_message == "It's disabled!"
        input_locator = driver.find_element(By.XPATH, "//form[@id='input-example']/input")
        assert [True if input_locator.is_enabled() == False else False]