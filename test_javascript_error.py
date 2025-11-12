import pytest
import allure

class TestJavascriptError:

    @pytest.mark.error
    def test_javascript_error(self, driver):

        driver.get("https://the-internet.herokuapp.com/javascript_error")
        logs = driver.get_log('browser')

        errors = [entry for entry in logs if entry['level'] in ('SEVERE', 'ERROR')]

        for e in errors:
            allure.attach(
                f"Javascript Error: {e}",
                name="JS Error",
                attachment_type=allure.attachment_type.TEXT
            )

        assert len(errors) != 0

