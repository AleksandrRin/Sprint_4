import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Скролл")
    def scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключение на вторую вкладку')
    def switch_window(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[1])
