from Methods.rent_page_methods import RentPage


class TestRent:
    def test_rent(self, driver):
        name = 'Александр'
        second_name = 'Петров'

        rent_page = RentPage(driver)
        rent_page.fill_name_field(name)
        rent_page.fill_second_name_field(second_name)
