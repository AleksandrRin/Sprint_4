import allure
import pytest

from Locators.main_page_locators import MainPageLocators
from Questions.qusestions import list_of_answers
from Methods.main_page_methods import MainPage


class TestMainPage:
    @allure.title('Проверка вопросов и ответов')
    @pytest.mark.parametrize("index", range(len(list_of_answers)))
    def test_questions(self, driver, index):
        main_page = MainPage(driver)
        element = driver.find_element(*MainPageLocators.QUESTS_BLOCK)
        main_page.scroll(element)
        main_page.click_on_cookies()
        main_page.check_question(index)
