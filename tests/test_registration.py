import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from generator_data import GeneratorData


email = GeneratorData().generator_email()
password = GeneratorData().generator_password()

class TestRegistrationInStellarBurgers():

    def test_registration_valid_data_successful_registration(self, driver):


        driver.find_element(*Locators.ENT_ACC_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TRANS_REG_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REG_HEADER))
        driver.find_element(*Locators.REG_NAME_FIELD).send_keys('Павел')
        driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.REG_PASS_FIELD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.AUTH_PANEL))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOG_FIELD))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PASS_FIELD))
        time.sleep(3)
        driver.find_element(*Locators.LOG_FIELD).send_keys(email)
        driver.find_element(*Locators.PASS_FIELD).send_keys(password)
        driver.find_element(*Locators.LOG_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PERS_ACC_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element_attribute(Locators.PROF_EMAIL_FIELD, 'value', email))


    def test_registration_invalid_password_unsuccessful_registration(self, driver):


        driver.find_element(*Locators.ENT_ACC_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.TRANS_REG_BUTTON)).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.REG_HEADER))
        driver.find_element(*Locators.REG_NAME_FIELD).send_keys('Павел')
        driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.REG_PASS_FIELD).send_keys('12345')
        driver.find_element(*Locators.REG_BUTTON).click()
        incorrect_password = driver.find_element(*Locators.INCORR_PASS).text

        assert incorrect_password == 'Некорректный пароль'
