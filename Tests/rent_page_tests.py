import time

from Methods.rent_page_methods import RentPage


class TestRent:
    def test_rent(self, driver):
        name = 'Александр'
        second_name = 'Петров'
        phone = '88005553535'
        address = 'Черкизовская д.123'

        rent_page = RentPage(driver)
        rent_page.fill_name_field(name)
        rent_page.fill_second_name_field(second_name)
        rent_page.fill_address_field(address)
        rent_page.click_on_metro_field()
        rent_page.check_metro_station()
        rent_page.enter_on_metro_station()
        rent_page.fill_phone_field(phone)
        rent_page.click_on_next_button()

