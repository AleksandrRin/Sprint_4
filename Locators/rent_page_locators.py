from selenium.webdriver.common.by import By


class RentLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")  # поле имя
    SECOND_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')  # поле фамилия
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')  # поле адресс
    METRO_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')  # поле метро
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')  # поле телефон
    NEXT_BUTTON = (By.XPATH, '//button[contains(text(), "Далее")]')  # кнопка дальше
    CALENDAR_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')  # поле календарь
    RENT_TIME_FIELD = (By.XPATH, '//div[contains(text(), "* Срок аренды")]')  # поле срок аренды
    RENT_TIME_ONE_DAY = (By.XPATH, '//div[@class="Dropdown-menu"]/div[contains(text(), "сутки")]')  # аренда 1 день
    BLACK_COLOR_CHECK_BOX = (By.ID, 'black')  # чек бокс черного цвета
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')  # поле комментарий
    ORDER_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[contains(text(), "Заказать")]')  # кнопка заказать
    CONFIRM_WINDOW_YES = (By.XPATH, '//button[contains(text(), "Да")]')  # кнопка да
    SUCCESS_TEXT = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")  # текст со статусом заказа
