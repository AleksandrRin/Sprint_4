from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_FROM_HEADER = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[contains(text(), "Заказать")]')  # кнопка заказать в хедере
    ORDER_BUTTON_FROM_BODY = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button[contains(text(), "Заказать")]')  # кнопка заказать в теле
    QUESTS_BLOCK = (By.XPATH, "//div[@class='accordion']")  # блок с вопросами
    COOKIES = (By.ID, 'rcc-confirm-button')  # кнопка подтверждения куки
    LOGO_SCOOTER = (By.XPATH, '//a[@href="/"]')  # лого самокат
    LOGO_YANDEX = (By.XPATH, '//a[@href="//yandex.ru"]')  # лого яндекс
