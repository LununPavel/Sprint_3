from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestLogoutInStellarBurgers:

    def test_logout(self, login, driver):
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.PERS_ACC_BUTTON)).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.PROF_EXIT_BUTTON)).click()

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.AUTH_PANEL))