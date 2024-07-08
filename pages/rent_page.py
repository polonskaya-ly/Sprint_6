from selenium.webdriver.common.by import By
import allure


class RentPage:
    delivery_date_field = [By.XPATH, './/input[@placeholder= "* Когда привезти самокат"]']
    rent_period_field = [By.CLASS_NAME, 'Dropdown-root']
    create_order_button = [By.XPATH, './/button[contains(@class,"Button_Middle__1CSJM") and text() = "Заказать"]']
    confirm_button = [By.XPATH, './/button[contains(@class,"Button_Middle__1CSJM") and text() = "Да"]']
    status_button = [By.XPATH, './/button[contains(text(),"Посмотреть статус")]']
    order_success_modal = [By.XPATH, './/div[text() = "Заказ оформлен"]']

    def __init__(self, driver):
        self.driver = driver

    def period(self, random_period):
        element = self.driver.find_element(By.XPATH, f'.//div[text()= "{random_period}"]')
        return element

    def day(self, random_day):
        element = self.driver.find_element(By.XPATH, f'.//div[contains(@aria-label,"{random_day}")]')
        return element

    def click_delivery_date_field(self):
        self.driver.find_element(*self.delivery_date_field).click()

    def click_delivery_date(self, random_day):
        self.day(random_day).click()

    def click_rent_period_field(self):
        self.driver.find_element(*self.rent_period_field).click()

    def click_period(self, random_period):
        self.period(random_period).click()

    def click_create_order_button(self):
        self.driver.find_element(*self.create_order_button).click()

    @allure.step('Заполнить условия аренды')
    def fill_rent_terms(self, random_period, random_day):
        self.click_delivery_date_field()
        self.click_delivery_date(random_day)
        self.click_rent_period_field()
        self.click_period(random_period)
        self.click_create_order_button()

    @allure.step('Подтвердить заказ')
    def click_confirm_create_order(self):
        self.driver.find_element(*self.confirm_button).click()

    def check_success_order_message(self):
        assert self.driver.find_element(*self.order_success_modal).is_displayed()

    @allure.step('Перейти на страницу с трекером заказа')
    def click_status_button(self):
        self.driver.find_element(*self.status_button).click()




