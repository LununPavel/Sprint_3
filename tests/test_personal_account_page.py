from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestPersonalAccountPageInStellarBurgers:

    def test_constructor_button_constructor_page_opens(self, login, driver):
        driver.find_element(*Locators.PERS_ACC_BUTTON).click()
        driver.find_element(*Locators.CONST_BUTTON).click()

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MENU_BURG_INGR))

    def test_stellar_burgers_button_constructor_page_opens(self, login, driver):
        driver.find_element(*Locators.LOGO).click()
        driver.find_element(*Locators.CONST_BUTTON).click()

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MENU_BURG_INGR))