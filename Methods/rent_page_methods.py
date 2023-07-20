from selenium.webdriver import Keys
from Locators.rent_page_locators import RentLocators


class RentPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_name_field(self, name):
        self.driver.find_element(*RentLocators.NAME_FIELD).send_keys(name)

    def fill_second_name_field(self, second_name):
        self.driver.find_element(*RentLocators.SECOND_NAME_FIELD).send_keys(second_name)

    def fill_address_field(self, address):
        self.driver.find_element(*RentLocators.ADDRESS_FIELD).send_keys(address)

    def click_on_metro_field(self):
        self.driver.find_element(*RentLocators.METRO_FIELD).click()

    def check_metro_station(self):
        self.driver.find_element(*RentLocators.METRO_FIELD).send_keys(Keys.ARROW_DOWN)

    def enter_on_metro_station(self):
        self.driver.find_element(*RentLocators.METRO_FIELD).send_keys(Keys.ENTER)

    def fill_phone_field(self, phone):
        self.driver.find_element(*RentLocators.PHONE_FIELD).send_keys(phone)

    def click_on_next_button(self):
        self.driver.find_element(*RentLocators.NEXT_BUTTON).click()
