import os
import time
import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestUploadingAndDownloading:

    @pytest.mark.upload
    def test_uploading(self, driver):

        driver.get("https://the-internet.herokuapp.com/upload")

        choose_file_button = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        choose_file_button.send_keys("/Users/sofiaamihan/Downloads/ZZZ.txt")

        upload_button = driver.find_element(By.XPATH, "//input[@id='file-submit']")
        upload_button.click()

        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'File Uploaded!')]")))
        assert wait.until(ec.presence_of_element_located((By.ID, "uploaded-files")))

    @pytest.mark.download
    def test_downloading(self):

        download_dir = "/Users/sofiaamihan/Downloads"

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True
        })

        driver = webdriver.Chrome(options=options)
        driver.get("https://the-internet.herokuapp.com/download")

        link = driver.find_element(By.XPATH, "//a[contains(text(), 'sample.txt')]")
        filename = link.text
        link.click()

        file_path = os.path.join(download_dir, filename)

        timeout = 15
        while timeout > 0 and not os.path.exists(file_path):
            time.sleep(1)
            timeout -= 1

        driver.quit()

        assert os.path.isfile(file_path), f"File was not downloaded: {file_path}"

