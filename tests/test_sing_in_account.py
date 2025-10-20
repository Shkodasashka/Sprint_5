from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import generate_registration_data
from locators import Locators
from curl import url
from data import Credentials

class TestSignInAccount:

    def test_success_sign_click_on_sign_in_account(self, driver):

        driver.get(url.main_site)
        driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SIGN_BUTTON))
     
        driver.find_element(*Locators.EMAIL_SIGN).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_SIGN).send_keys(Credentials.password)
        driver.find_element(*Locators.SIGN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER))

        assert driver.current_url == url.sign_site


    def test_success_sign_click_on_sign_in_personal_account(self, driver):

        driver.get(url.main_site)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SIGN_BUTTON))
     
        driver.find_element(*Locators.EMAIL_SIGN).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_SIGN).send_keys(Credentials.password)
        driver.find_element(*Locators.SIGN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER))

        assert driver.current_url == url.sign_site


    def test_success_sign_click_on_sign_sing_in_form_of_registration(self, driver):

        driver.get(url.registration_site)
        driver.find_element(*Locators.SIGN_IN_REGISTER_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SIGN_BUTTON))
     
        driver.find_element(*Locators.EMAIL_SIGN).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_SIGN).send_keys(Credentials.password)
        driver.find_element(*Locators.SIGN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER))

        assert driver.current_url == url.sign_site


    def test_success_sign_click_on_sign_sing_in_forgot_password_form(self, driver):

        driver.get(url.forgot_password_site)
        driver.find_element(*Locators.SIGN_IN_FORGOT_PASSWORD_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SIGN_BUTTON))
     
        driver.find_element(*Locators.EMAIL_SIGN).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_SIGN).send_keys(Credentials.password)
        driver.find_element(*Locators.SIGN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER))

        assert driver.current_url == url.sign_site       