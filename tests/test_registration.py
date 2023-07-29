from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationInStellarBurgers():

    def test_registration_valid_data_successful_registration(self, driver, generator_password, generator_email):
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Зарегистрироваться')]"))).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Регистрация')]")))
        driver.find_element(By.XPATH, "//fieldset[1]//input").send_keys('Павел')
        driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys(generator_email)
        driver.find_element(By.XPATH, "//fieldset[3]//input").send_keys(generator_password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        auth_form = driver.find_element(By.XPATH, "//form[contains(@class, 'Auth_form')]")

        assert EC.visibility_of_element_located((auth_form))


    def test_registration_invalid_password_unsuccessful_registration(self, driver, generator_email):
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Зарегистрироваться')]"))).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Регистрация')]")))
        driver.find_element(By.XPATH, "//fieldset[1]//input").send_keys('Павел')
        driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys(generator_email)
        driver.find_element(By.XPATH, "//fieldset[3]//input").send_keys('12345')
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        incorrect_password = driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text

        assert incorrect_password == 'Некорректный пароль'
