import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Methods.main_page_methods import MainPage
from Methods.rent_page_methods import RentPage
from Data import data


class TestRent:

    @allure.title('Заполнение формы аренды')
    @pytest.mark.parametrize("entry_point", ["header", "body"])
    def test_rent_form(self, driver, entry_point):
        rent_page = RentPage(driver)
        if entry_point == "header":
            rent_page.open_rent_from_header_button()
        elif entry_point == "body":
            rent_page.open_rent_from_body_button()
        rent_page.fill_about_form(data.name, data.second_name, data.address, data.phone)
        rent_page.check_about_rent_form()

    @allure.title('Заполнение формы куда привезти')
    def test_about_rent_page(self, driver):
        driver.get(data.order_page)
        rent_about_page = TestRent()
        entry_point = "header"
        rent_about_page.test_rent_form(driver, entry_point)
        rent_about_page = RentPage(driver)
        rent_about_page.click_on_calendar()
        rent_about_page.enter_date_in_calendar()
        rent_about_page.click_on_rent_time_field()
        rent_about_page.enter_rent_time()
        rent_about_page.enter_black_color()
        rent_about_page.fill_comment_field(data.comment)
        rent_about_page.click_on_order_button()
        rent_about_page.click_on_yes_button()
        rent_about_page.check_success_text()

    @allure.title('Проверка клика по лого самокат')
    def test_click_on_scooter_logo(self, driver):
        driver.get(data.order_page)
        check_click_on_logo = RentPage(driver)
        check_click_on_logo.click_on_scooter_logo()
        check_click_on_logo = MainPage(driver)
        check_click_on_logo.check_click_on_scooter_logo()

    @allure.title('Проверка клика по лого яндекс')
    def test_click_on_yandex_logo(self, driver):
        driver.get(data.order_page)
        check_click_on_logo = RentPage(driver)
        check_click_on_logo.click_on_yandex_logo()
        check_click_on_logo.switch_window()
        WebDriverWait(driver, 10).until(EC.url_contains(data.yandex_page))
        check_click_on_logo = MainPage(driver)
        check_click_on_logo.check_click_on_yandex_logo()
