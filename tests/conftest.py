import random
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

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
    browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    driver.find_element(By.XPATH, "//fieldset[1]//input").send_keys('pavel@lunin.ru')
    driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys('111111')
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()