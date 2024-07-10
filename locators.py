from selenium.webdriver.common.by import By


class HomePageLocators:
    ORDER_BUTTON_SMALL = [By.CLASS_NAME, 'Button_Button__ra12g']
    ORDER_BUTTON_BIG = [By.XPATH, './/div[contains(@class,"Home_FinishButton")]/button[text() = "Заказать"]']


class OrderPageLocators:
    NAME_FIELD = [By.XPATH, './/input[@placeholder= "* Имя"]']
    SURNAME_FIELD = [By.XPATH, './/input[@placeholder= "* Фамилия"]']
    ADDRESS_FIELD = [By.XPATH, './/input[@placeholder= "* Адрес: куда привезти заказ"]']
    METRO_FIELD = [By.XPATH, './/input[@placeholder= "* Станция метро"]']
    PHONE_FIELD = [By.XPATH, './/input[@placeholder= "* Телефон: на него позвонит курьер"]']
    THEN_BUTTON = [By.XPATH, './/button[contains(text(),"Далее")]']

class RentPageLocators:
    DELIVERY_DATE_FIELD = [By.XPATH, './/input[@placeholder= "* Когда привезти самокат"]']
    RENT_PERIOD_FIELD = [By.CLASS_NAME, 'Dropdown-root']
    CREATE_ORDER_BUTTON = [By.XPATH, './/button[contains(@class,"Button_Middle__1CSJM") and text() = "Заказать"]']
    CONFIRM_BUTTON = [By.XPATH, './/button[contains(@class,"Button_Middle__1CSJM") and text() = "Да"]']
    STATUS_BUTTON = [By.XPATH, './/button[contains(text(),"Посмотреть статус")]']
    ORDER_SUCCESS_MODAL = [By.XPATH, './/div[text() = "Заказ оформлен"]']

class TrackPageLocators:
    LOGO_BUTTON = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    YANDEX_BUTTON = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']