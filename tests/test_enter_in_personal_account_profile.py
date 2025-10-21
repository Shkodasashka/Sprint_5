from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import url
from data import Credentials


class TestEnterInPersonalAccountProfile:

    def test_success_sign_click_on_enter_in_personal_account(self, driver):
        driver.get(url.main_site)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SIGN_BUTTON))
        driver.find_element(*Locators.EMAIL_SIGN).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_SIGN).send_keys(Credentials.password)
        driver.find_element(*Locators.SIGN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE))
