from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPersonalAccountPageInStellarBurgers:

    def test_constructor_button_constructor_page_opens(self, login, driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]")))

    def test_stellar_burgers_button_constructor_page_opens(self, login, driver):
        driver.find_element(By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]").click()
        driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]")))