from selenium.webdriver.common.by import By


class RentLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SECOND_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[contains(text(), "Далее")]')
    CALENDAR_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENT_TIME_FIELD = (By.XPATH, '//div[@class="Dropdown-control"]')
    RENT_TIME_ONE_DAY = (By.XPATH, '//div[@class="Dropdown-menu"]/div[contains(text(), "сутки")]')