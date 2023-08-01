import pytest
from selenium import webdriver
from locators import Locators
from urls import Urls

url = Urls().urls()

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.PERS_ACC_BUTTON).click()
    driver.find_element(*Locators.LOG_FIELD).send_keys('pavel@lunin.ru')
    driver.find_element(*Locators.PASS_FIELD).send_keys('111111')
    driver.find_element(*Locators.LOG_BUTTON).click()