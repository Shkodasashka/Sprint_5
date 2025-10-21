from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import url


class TestInConstructorGoToSections:

    def test_success_in_constructor_go_to_section_staffing(self, driver):
        driver.get(url.main_site)
        driver.find_element(*Locators.STAFFING_SWITCHER).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SELECTED_STAFFING_SWITCHER))

    def test_success_in_constructor_go_to_section_sauce(self, driver):
        driver.get(url.main_site)
        driver.find_element(*Locators.SAUCE_SWITCHER).click() 
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SELECTED_SAUCE_SWITCHER))

    def test_success_in_constructor_go_to_section_bread(self, driver):
        driver.get(url.main_site)
        driver.find_element(*Locators.SAUCE_SWITCHER).click()      
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SELECTED_SAUCE_SWITCHER))
        driver.find_element(*Locators.BREAD_SWITCHER).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SELECTED_BREAD_SWITCHER))
