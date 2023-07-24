import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self):
        element = self.driver.find_element(*MainPageLocators.QUESTS_BLOCK)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on_question(self):
        for index in range(8):
            element_id = f'accordion__heading-{index}'
            self.driver.find_element(By.ID, element_id).click()
            time.sleep(1)

    def click_on_cookies(self):
        self.driver.find_element(*MainPageLocators.COOKIES).click()

