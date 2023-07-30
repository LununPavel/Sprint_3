import random
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators

@pytest.fixture
def generator_password():
    password = random.randint(100000, 999999)

    return password

@pytest.fixture
def generator_email():
    faker = Faker()
    email = faker.email()

    return email

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.PERS_ACC_BUTTON).click()
    driver.find_element(*Locators.LOG_FIELD).send_keys('pavel@lunin.ru')
    driver.find_element(*Locators.PASS_FIELD).send_keys('111111')
    driver.find_element(*Locators.LOG_BUTTON).click()