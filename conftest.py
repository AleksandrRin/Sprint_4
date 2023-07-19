from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    base_url = 'https://qa-scooter.praktikum-services.ru/order'
    driver = webdriver.Firefox()
    driver.get(base_url)
    yield driver
    driver.quit()
