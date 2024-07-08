import allure

from selenium.webdriver.common.by import By


class OrderPage:
    name_field = [By.XPATH, './/input[@placeholder= "* Имя"]']
    surname_field = [By.XPATH, './/input[@placeholder= "* Фамилия"]']
    address_field = [By.XPATH, './/input[@placeholder= "* Адрес: куда привезти заказ"]']
    metro_field = [By.XPATH, './/input[@placeholder= "* Станция метро"]']
    telephone_field = [By.XPATH, './/input[@placeholder= "* Телефон: на него позвонит курьер"]']
    then_button = [By.XPATH, './/button[contains(text(),"Далее")]']

    def __init__(self, driver):
        self.driver = driver

    def metro(self, random_metro):
        element = self.driver.find_element(By.XPATH, f'.//div[text() = "{random_metro}"]')
        return element

    def click_name_field(self):
        self.driver.find_element(*self.name_field).click()

    def click_surname_field(self):
        self.driver.find_element(*self.surname_field).click()

    def click_address_field(self):
        self.driver.find_element(*self.address_field).click()

    def click_metro_field(self):
        self.driver.find_element(*self.metro_field).click()

    def click_station_list(self, random_metro):
        self.metro(random_metro).click()

    def click_telephone_field(self):
        self.driver.find_element(*self.telephone_field).click()

    def click_then_button(self):
        self.driver.find_element(*self.then_button).click()

    def input_name_to_field(self, rent_name):
        name = rent_name[0]
        self.driver.find_element(*self.name_field).send_keys(name)

    def input_surname_to_field(self, rent_name):
        surname = rent_name[1]
        self.driver.find_element(*self.surname_field).send_keys(surname)

    def input_address_to_field(self, rent_data):
        address = rent_data[0]
        self.driver.find_element(*self.address_field).send_keys(address)

    def input_telephone_to_field(self, rent_data):
        phone = rent_data[1]
        self.driver.find_element(*self.telephone_field).send_keys(phone)

    @allure.step('Заполнить форму заказа')
    def fill_order_form(self, rent_name, rent_data, random_metro):
        self.click_name_field()
        self.input_name_to_field(rent_name)
        self.click_surname_field()
        self.input_surname_to_field(rent_name)
        self.click_address_field()
        self.input_address_to_field(rent_data)
        self.click_metro_field()
        self.click_station_list(random_metro)
        self.click_telephone_field()
        self.input_telephone_to_field(rent_data)
        self.click_then_button()
