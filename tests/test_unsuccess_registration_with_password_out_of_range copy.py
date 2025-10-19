from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import generate_registration_data
from locators import Locators
from curl import url

class TestRegistrationWithPasswordOutOfRange:

    def test_unsuccess_registration_with_invalid_password(self, driver):
        #arrange
        driver.get(url.registration_site)
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.NAME).send_keys(name)       
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password[:5])

        #act
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        popup_text=WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.INVALID_PASSWORD_POPUP)).text
        #assert
        assert popup_text == 'Некорректный пароль'