from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import generate_registration_data
from locators import Locators
from curl import url

class TestRegistrationWithNewCredentials:

    def test_sucsess_registration(self, driver):
        #arrange
        driver.get(url.registration_site)
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.NAME).send_keys(name)       
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        #act
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(*Locators.SIGN_BUTTON))
        #assert
        assert driver.current_url == url.login_site