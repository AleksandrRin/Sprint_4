import allure
from selenium.webdriver import Keys
from Locators.rent_page_locators import RentLocators
from Locators.main_page_locators import MainPageLocators
from Methods.base_page_methods import BasePage


class RentPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    @allure.step('Нажатие на кнопку заказать в хедере')
    def open_rent_from_header_button(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_FROM_HEADER).click()

    @allure.step('Нажатие на кнопку заказать в теле')
    def open_rent_from_body_button(self):
        item = self.driver.find_element(*MainPageLocators.ORDER_BUTTON_FROM_BODY)
        self.driver.execute_script("arguments[0].scrollIntoView();", item)
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_FROM_BODY).click()

    @allure.step('Клик на поле календарь')
    def click_on_calendar(self):
        self.driver.find_element(*RentLocators.CALENDAR_FIELD).click()

    @allure.step('Выбор даты в календаре')
    def enter_date_in_calendar(self, tomorrow):
        self.driver.find_element(*RentLocators.CALENDAR_FIELD).send_keys(tomorrow.strftime("%d.%m.%Y"))
        self.driver.find_element(*RentLocators.CALENDAR_FIELD).send_keys(Keys.ENTER)

    @allure.step('Клик по полю время аренды')
    def click_on_rent_time_field(self):
        self.driver.find_element(*RentLocators.RENT_TIME_FIELD).click()

    @allure.step('Проверка текста')
    def check_about_rent_form(self):
        about_rent_form_text = self.driver.find_element(*RentLocators.ORDER_BUTTON)
        assert about_rent_form_text.is_displayed()

    @allure.step('Клик по времени аренды')
    def enter_rent_time(self):
        self.driver.find_element(*RentLocators.RENT_TIME_ONE_DAY).click()

    @allure.step('Выбор черного самоката')
    def enter_black_color(self):
        self.driver.find_element(*RentLocators.BLACK_COLOR_CHECK_BOX).click()

    @allure.step('Заполнить поле комментарий')
    def fill_comment_field(self, comment):
        self.driver.find_element(*RentLocators.COMMENT_FIELD).send_keys(comment)

    @allure.step('Клик по кнопке заказать')
    def click_on_order_button(self):
        self.driver.find_element(*RentLocators.ORDER_BUTTON).click()

    @allure.step('Подтверждение заказа')
    def click_on_yes_button(self):
        self.driver.find_element(*RentLocators.CONFIRM_WINDOW_YES).click()

    @allure.step('Проверка успеха заказа')
    def check_success_text(self):
        order_status = self.driver.find_element(*RentLocators.SUCCESS_TEXT).text
        assert "Заказ оформлен" in order_status

    @allure.step('Клик по кнопке самокат')
    def click_on_scooter_logo(self):
        self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).click()

    # @allure.step('Проверка перехода на главную')
    # def check_click_on_scooter_logo(self):
    #     assert self.driver.find_element(*MainPageLocators.ORDER_BUTTON_FROM_HEADER).is_displayed()

    @allure.step('Клик по кнопке яндекс')
    def click_on_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.LOGO_YANDEX).click()

    # @allure.step('Проверка перехода на главную страницу яндекса')
    # def check_click_on_yandex_logo(self):
    #     assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'

    # @allure.step('Переключение на вторую вкладку')
    # def switch_window(self):
    #     all_tabs = self.driver.window_handles
    #     self.driver.switch_to.window(all_tabs[1])

    @allure.step("Заполнение формы аренды")
    def fill_about_form(self, name, second_name, address, phone):
        self.driver.find_element(*RentLocators.NAME_FIELD).send_keys(name)
        self.driver.find_element(*RentLocators.SECOND_NAME_FIELD).send_keys(second_name)
        self.driver.find_element(*RentLocators.ADDRESS_FIELD).send_keys(address)
        self.driver.find_element(*RentLocators.METRO_FIELD).click()
        self.driver.find_element(*RentLocators.METRO_FIELD).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(*RentLocators.METRO_FIELD).send_keys(Keys.ENTER)
        self.driver.find_element(*RentLocators.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(*RentLocators.NEXT_BUTTON).click()
