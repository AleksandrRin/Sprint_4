import allure

from Locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_quests(self):
        element = self.driver.find_element(*MainPageLocators.QUESTS_BLOCK)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключение на вторую вкладку')
    def switch_window(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[1])

    @allure.step('Проверка перехода на главную')
    def check_click_on_scooter_logo(self):
        assert self.driver.find_element(*MainPageLocators.ORDER_BUTTON_FROM_HEADER).is_displayed()

    @allure.step('Проверка перехода на главную страницу яндекса')
    def check_click_on_yandex_logo(self):
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'