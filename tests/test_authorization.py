import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAuthorizationInStellarBurgers:

    @pytest.mark.parametrize('button', ["//button[contains(@class,'button_button_type_primary')]", "//p[contains(text(),'Личный Кабинет')]"])
    def test_authorization_through_home_page_button_successful_authorization(self, driver, button):
        driver.find_element(By.XPATH, button).click()
        driver.find_element(By.XPATH, "//fieldset[1]//input").send_keys('pavel@lunin.ru')
        driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys('111111')
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()

        assert WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element_attribute((By.XPATH, "//li[1]//input"), 'value', 'Павел'))


    def test_authorization_through_registration_form_successful_authorization(self, driver):
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        driver.find_element(By.XPATH, "//fieldset[1]//input").send_keys('pavel@lunin.ru')
        driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys('111111')
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()

        assert WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element_attribute((By.XPATH, "//li[2]//input"), 'value', 'pavel@lunin.ru'))


    def test_authorization_through_password_recovery_form_successful_authorization(self, driver):
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        driver.find_element(By.XPATH, "//fieldset[1]//input").send_keys('pavel@lunin.ru')
        driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys('111111')
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()

        assert WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element_attribute((By.XPATH, "//li[2]//input"), 'value', 'pavel@lunin.ru'))