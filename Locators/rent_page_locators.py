from selenium.webdriver.common.by import By


class RentLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']") # поле имя
    SECOND_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]') # поле фамилия
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]') # поле адресс
    METRO_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]') # поле метро
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]') # поле телефон
    NEXT_BUTTON = (By.XPATH, '//button[contains(text(), "Далее")]') # кнопка дальше
    CALENDAR_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]') # поле календарь
    CALENDAR_DATE = (By.XPATH, '//div[@aria-label="Choose понедельник, 31-е июля 2023 г."]') # дата в календаре
    RENT_TIME_FIELD = (By.XPATH, '//div[@class="Dropdown-control"]') # поле срок аренды
    RENT_TIME_ONE_DAY = (By.XPATH, '//div[@class="Dropdown-menu"]/div[contains(text(), "сутки")]') # аренда 1 день
    BLACK_COLOR_CHECK_BOX = (By.ID, 'black') # чек бокс черног цвета
    ABOUT_RENT_TEXT = (By.XPATH, '//div[@class="Order_Header__BZXOb"]') # текст о аренде
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]') # поле комментарий
    ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]') # кнопка заказать
    CONFIRM_WINDOW_YES = (By.XPATH, '//button[contains(text(), "Да")]') # кнопка да
    SUCCESS_TEXT = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']") # текст со статусом заказа
