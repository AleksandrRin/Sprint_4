import allure
from selenium.webdriver.common.by import By
from Methods.base_page_methods import BasePage
from Questions.qusestions import list_of_answers
from Locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Клик по кукам')
    def click_on_cookies(self):
        self.driver.find_element(*MainPageLocators.COOKIES).click()

    @allure.step('Проверка соответствия вопросов с ответами')
    def check_question(self, index):
        question_id = f'accordion__heading-{index}'
        answer_id = f'accordion__panel-{index}'

        self.driver.find_element(By.ID, question_id).click()
        expected_text = list_of_answers[index]
        actual_text = self.driver.find_element(By.ID, answer_id).text
        assert actual_text == expected_text

    @allure.step('Проверка перехода на главную')
    def check_click_on_scooter_logo(self):
        assert self.driver.find_element(*MainPageLocators.ORDER_BUTTON_FROM_HEADER).is_displayed()

    @allure.step('Проверка перехода на главную страницу яндекса')
    def check_click_on_yandex_logo(self):
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'
