import os
import time
from selenium.webdriver.common.by import By
import pytest

class TestSecureFileDownload:

    @pytest.mark.download
    def test_secure_file_download(self, driver, download_dir):

        driver.get("https://admin:admin@the-internet.herokuapp.com/download_secure")

        link = driver.find_element(By.XPATH, "//a[contains(text(), 'test.txt')]")
        filename = link.text
        link.click()

        file_path = os.path.join(download_dir, filename)

        timeout = 15
        while timeout > 0 and not os.path.exists(file_path):
            time.sleep(1)
            timeout -= 1

        assert os.path.isfile(file_path), f"File was not downloaded: {file_path}"
