from Locators.rent_page_locators import RentLocators


class RentPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_name_field(self, name):
        self.driver.find_element(*RentLocators.NAME_FIELD).send_keys(name)

    def fill_second_name_field(self, second_name):
        self.driver.find_element(*RentLocators.SECOND_NAME_FIELD).send_keys(second_name)
