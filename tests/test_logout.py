from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogoutInStellarBurgers:

    def test_logout(self, login, driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'Account_button')]"))).click()

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//form[contains(@class, 'Auth_form')]")))