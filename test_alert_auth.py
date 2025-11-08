import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# TODO - complex authentication with error checks, locking outs, etc, through forms as well

class TestBasicAuth:

    @pytest.mark.login
    @pytest.mark.parametrize("username, password",[
        ("admin", "admin"),
        ("incorrect-username", "admin"),
        ("admin", "incorrect-password"),
        ("incorrect", "incorrect")
    ], ids=['correct-login', 'incorrect-username', 'incorrect-password', 'incorrect-login'])
    def test_all_login_cases(self, driver, username, password):
        URL = "https://" + username + ":" + password + "@" + "the-internet.herokuapp.com/basic_auth"
        driver.get(URL)
        wait = WebDriverWait(driver, 10)
        if username == "admin" and password == "admin":
            text_locator = driver.find_element(By.XPATH, "//div[@class='example']/p")
            assert text_locator.is_displayed()
        else:
            assert wait.until(ec.none_of(ec.presence_of_element_located((By.XPATH, "//div[@class='example']/p"))))
