import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestSecureFileDownload:

    @pytest.mark.download
    def test_secure_file_download(self):

        download_dir = "/Users/sofiaamihan/Downloads"
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True
        })

        driver = webdriver.Chrome(options=options)
        driver.get("https://admin:admin@the-internet.herokuapp.com/download_secure")

        link = driver.find_element(By.XPATH, "//a[contains(text(), 'large-test-file.txt')]")
        filename = link.text
        link.click()

        file_path = os.path.join(download_dir, filename)

        timeout = 15
        while timeout > 0 and not os.path.exists(file_path):
            time.sleep(1)
            timeout -= 1

        driver.quit()

        assert os.path.isfile(file_path), f"File was not downloaded: {file_path}"
