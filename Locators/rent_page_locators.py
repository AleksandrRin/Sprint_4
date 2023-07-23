from selenium.webdriver.common.by import By


class RentLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SECOND_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[contains(text(), "Далее")]')
    CALENDAR_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    CALENDAR_DATE = (By.XPATH, '//div[@aria-label="Choose понедельник, 31-е июля 2023 г."]')
    RENT_TIME_FIELD = (By.XPATH, '//div[@class="Dropdown-control"]')
    RENT_TIME_ONE_DAY = (By.XPATH, '//div[@class="Dropdown-menu"]/div[contains(text(), "сутки")]')
    BLACK_COLOR_CHECK_BOX = (By.ID, 'black')
    ABOUT_RENT_TEXT = (By.XPATH, '//div[@class="Order_Header__BZXOb"]')
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    CONFIRM_WINDOW_YES = (By.XPATH, '//button[contains(text(), "Да")]')
    SUCCESS_TEXT = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
