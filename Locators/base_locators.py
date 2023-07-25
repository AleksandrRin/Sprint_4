from selenium.webdriver.common.by import By


class BaseLocators:
    LOGO_SCOOTER = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]') # лого самокат
    LOGO_YANDEX = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]') # лого яндекс

