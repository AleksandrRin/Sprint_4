from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Methods.rent_page_methods import RentPage


class TestRent:
    name = 'Александр'
    second_name = 'Петров'
    phone = '88005553535'
    address = 'Черкизовская д.123'
    comment = 'Домофон не работает'
    order_page = 'https://qa-scooter.praktikum-services.ru/order'

    def test_rent_from_header_button(self, driver):
        rent_page = RentPage(driver)
        rent_page.open_rent_from_header_button()
        rent_page.fill_name_field(self.name)
        rent_page.fill_second_name_field(self.second_name)
        rent_page.fill_address_field(self.address)
        rent_page.click_on_metro_field()
        rent_page.check_metro_station()
        rent_page.enter_on_metro_station()
        rent_page.fill_phone_field(self.phone)
        rent_page.click_on_next_button()
        rent_page.check_about_rent_form()

    def test_rent_from_body_button(self, driver):
        rent_page = RentPage(driver)
        rent_page.open_rent_from_header_button()
        rent_page.fill_name_field(self.name)
        rent_page.fill_second_name_field(self.second_name)
        rent_page.fill_address_field(self.address)
        rent_page.click_on_metro_field()
        rent_page.check_metro_station()
        rent_page.enter_on_metro_station()
        rent_page.fill_phone_field(self.phone)
        rent_page.click_on_next_button()
        rent_page.check_about_rent_form()

    def test_about_rent_page(self, driver):
        driver.get(self.order_page)
        rent_about_page = TestRent()
        rent_about_page.test_rent_from_body_button(driver)
        rent_about_page = RentPage(driver)
        rent_about_page.click_on_calendar()
        rent_about_page.enter_date_in_calendar()
        rent_about_page.click_on_rent_time_field()
        rent_about_page.enter_rent_time()
        rent_about_page.enter_black_color()
        rent_about_page.fill_comment_field(self.comment)
        rent_about_page.click_on_order_button()
        rent_about_page.click_on_yes_button()
        rent_about_page.check_success_text()

    def test_click_on_scooter_logo(self, driver):
        driver.get(self.order_page)
        check_click_on_logo = RentPage(driver)
        check_click_on_logo.click_on_scooter_logo()
        check_click_on_logo.check_click_on_scooter_logo()

    def test_click_on_yandex_logo(self, driver):
        driver.get(self.order_page)
        check_click_on_logo = RentPage(driver)
        check_click_on_logo.click_on_yandex_logo()
        WebDriverWait(driver, 10).until(EC.url_changes(self.order_page))
        current_url = driver.current_url
        print("Текущий URL страницы:", current_url)
        # check_click_on_logo.check_click_on_yandex_logo()


