from selenium.webdriver import Keys
from Locators.rent_page_locators import RentLocators
from Locators.main_page_locators import MainPageLocators
from Locators.base_locators import BaseLocators


class RentPage:
    def __init__(self, driver):
        self.driver = driver

    def open_rent_from_header_button(self):
        self.driver.find_element(*MainPageLocators.order_button_from_header).click()

    def open_rent_from_body_button(self):
        self.driver.find_element(*MainPageLocators.order_button_from_body).click()

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

    def click_on_calendar(self):
        self.driver.find_element(*RentLocators.CALENDAR_FIELD).click()

    def enter_date_in_calendar(self):
        self.driver.find_element(*RentLocators.CALENDAR_DATE).send_keys(Keys.ENTER)

    def click_on_rent_time_field(self):
        self.driver.find_element(*RentLocators.RENT_TIME_FIELD).click()

    def check_about_rent_form(self):
        about_rent_form_text = self.driver.find_element(*RentLocators.ABOUT_RENT_TEXT).text
        assert 'Про аренду' in about_rent_form_text

    def enter_rent_time(self):
        self.driver.find_element(*RentLocators.RENT_TIME_ONE_DAY).click()

    def enter_black_color(self):
        self.driver.find_element(*RentLocators.BLACK_COLOR_CHECK_BOX).click()

    def fill_comment_field(self, comment):
        self.driver.find_element(*RentLocators.COMMENT_FIELD).send_keys(comment)

    def click_on_order_button(self):
        self.driver.find_element(*RentLocators.ORDER_BUTTON).click()

    def click_on_yes_button(self):
        self.driver.find_element(*RentLocators.CONFIRM_WINDOW_YES).click()

    def check_success_text(self):
        order_status = self.driver.find_element(*RentLocators.SUCCESS_TEXT).text
        assert "Заказ оформлен" in order_status

    def click_on_scooter_logo(self):
        self.driver.find_element(*BaseLocators.LOGO_SCOOTER).click()

    def check_click_on_scooter_logo(self):
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def click_on_yandex_logo(self):
        self.driver.find_element(*BaseLocators.LOGO_YANDEX).click()

    def check_click_on_yandex_logo(self):
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'

    def switch_window(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[1])