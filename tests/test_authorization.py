import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestAuthorizationInStellarBurgers:

    @pytest.mark.parametrize("button", [Locators.ENT_ACC_BUTTON, Locators.PERS_ACC_BUTTON])
    def test_authorization_through_enter_account_button_successful_authorization(self, driver, button):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(button)).click()
        driver.find_element(*Locators.LOG_FIELD).send_keys('pavel@lunin.ru')
        driver.find_element(*Locators.PASS_FIELD).send_keys('111111')
        driver.find_element(*Locators.LOG_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PERS_ACC_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(Locators.PROF_NAME_FIELD, 'value', 'Павел'))


    def test_authorization_through_registration_form_successful_authorization(self, driver):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ENT_ACC_BUTTON)).click()
        driver.find_element(*Locators.TRANS_REG_BUTTON).click()
        driver.find_element(*Locators.REG_LOG_BUTTON).click()
        driver.find_element(*Locators.LOG_FIELD).send_keys('pavel@lunin.ru')
        driver.find_element(*Locators.PASS_FIELD).send_keys('111111')
        driver.find_element(*Locators.LOG_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PERS_ACC_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(Locators.PROF_EMAIL_FIELD, 'value', 'pavel@lunin.ru'))


    def test_authorization_through_password_recovery_form_successful_authorization(self, driver):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ENT_ACC_BUTTON)).click()
        driver.find_element(*Locators.TRANS_PASS_REC_BUTTON).click()
        driver.find_element(*Locators.REG_LOG_BUTTON).click()
        driver.find_element(*Locators.LOG_FIELD).send_keys('pavel@lunin.ru')
        driver.find_element(*Locators.PASS_FIELD).send_keys('111111')
        driver.find_element(*Locators.LOG_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PERS_ACC_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(Locators.PROF_EMAIL_FIELD, 'value', 'pavel@lunin.ru'))