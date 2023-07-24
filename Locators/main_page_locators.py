from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_FROM_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON_FROM_BODY = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM')
    QUESTS_BLOCK = (By.XPATH, "//div[@class='accordion']")
    QUESTION_FIELD1 = (By.ID, 'accordion__heading-0')
    COOKIES = (By.ID, 'rcc-confirm-button')
