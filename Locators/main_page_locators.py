from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_FROM_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g') # кнопка заказать в хедере
    ORDER_BUTTON_FROM_BODY = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM') # кнопка заказать в теле
    QUESTS_BLOCK = (By.XPATH, "//div[@class='accordion']") # блок с вопросами
    QUESTION_FIELD1 = (By.ID, 'accordion__heading-0') # поле с вопросом
    COOKIES = (By.ID, 'rcc-confirm-button') # кнопка подтверждения куки
