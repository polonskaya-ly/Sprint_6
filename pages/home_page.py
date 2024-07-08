import time
import allure
from selenium.webdriver.common.by import By


class HomePage:
    order_button_small = [By.XPATH, './/button[@class = "Button_Button__ra12g" and text() = "Заказать"]']
    order_button_big = [By.XPATH, './/button[contains(@class,"Button_Middle__1CSJM") and text() = "Заказать"]']

    def __init__(self, driver):
        self.driver = driver

    def element_question(self, question):
        element = self.driver.find_element(By.XPATH, f'.//div[text() = "{question}"]')
        return  element

    @allure.step('Перейти к форме заказа через кнопку в хейдере')
    def click_order_button_small(self):
        self.driver.find_element(*self.order_button_small).click()

    def click_order_button_big(self):
        self.driver.find_element(*self.order_button_big).click()

    @allure.step('Проскроллить до "Вопросы о важном"')
    def scroll_to_question(self, question):
        element = self.element_question(question)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Проскроллить до большой кнопки заказа')
    def scroll_to_order_button_big(self):
        element = self.driver.find_element(*self.order_button_big)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    @allure.step('Нажать на вопрос')
    def click_question(self, question):
        time.sleep(1)
        element = self.element_question(question)
        element.click()

    def check_answers(self, answer):
        answer_text = self.driver.find_element(By.XPATH, f'.//p[text() = "{answer}"]')
        assert answer_text.is_displayed()

    def check_answers_to_questions(self, question, answer):
        self.scroll_to_question(question)
        self.click_question(question)
        self.check_answers(answer)
