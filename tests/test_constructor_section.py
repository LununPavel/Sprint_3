import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConstructorSectionInStellarBurgers:

    @pytest.mark.parametrize('element,section', [
        ['Биокотлета из марсианской Магнолии', 3],
        ['Соус традиционный галактический', 2],
        ['Флюоресцентная булка R2-D3', 1]
    ])
    def test_switching_between_sections_desired_section_is_displayed(self, login, driver, element, section):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]")))
        scroll = driver.find_element(By.XPATH, f"//img[contains(@alt, '{element}')]")
        driver.execute_script("arguments[0]. scrollIntoView();", scroll)

        assert WebDriverWait(driver, 3).until(
            EC.text_to_be_present_in_element_attribute((By.XPATH, f"//div[{section}][contains(@class, 'tab_tab')]"), 'class', 'tab_tab_type_current'))