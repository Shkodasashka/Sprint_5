from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import generate_registration_data
from locators import Locators
from curl import url
from data import Credentials

class TestInConstructorGoToSectionBread:

    def test_success_in_constructor_go_to_section_bread(self, driver):

        driver.get(url.main_site)
        driver.find_element(*Locators.SAUCE_SWITCHER).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SELECTED_SAUCE_SWITCHER))

        driver.find_element(*Locators.BREAD_SWITCHER).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SELECTED_BREAD_SWITCHER))

        assert driver.find_element(*Locators.SELECTED_BREAD_SWITCHER).get_attribute("class") == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'