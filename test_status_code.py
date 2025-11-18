import allure
import pytest

class TestStatusCode:

    @pytest.mark.code
    def test_status_code(self, driver):
        driver.get("https://www.google.com")

        for request in driver.requests:
            if request.response:
                # request.response.headers['Content-Type']
                allure.attach(
                    f"URL: {request.url}\nCODE: {request.response.status_code}",
                    name= "Status Code",
                    attachment_type=allure.attachment_type.TEXT
                )
        assert len(driver.requests) != 0
