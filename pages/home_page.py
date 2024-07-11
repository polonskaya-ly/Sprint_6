import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..locators import HomePageLocators


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def question_locator(self, question):
        question_locator = [By.XPATH, f'.//div[text() = "{question}"]']
        return question_locator

    def element_question(self, question):
        element = self.driver.find_element(*self.question_locator(question))
        return  element

    @allure.step('Перейти к форме заказа через кнопку в хейдере')
    def click_order_button_small(self):
        self.driver.find_element(*HomePageLocators.ORDER_BUTTON_SMALL).click()

    @allure.step('Перейти к форме заказа')
    def click_order_button_big(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((HomePageLocators.ORDER_BUTTON_BIG)))
        self.driver.find_element(*HomePageLocators.ORDER_BUTTON_BIG).click()

    def wait_for_clickable_question(self, question):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((self.question_locator(question))))

    @allure.step('Проскроллить до "Вопросы о важном"')
    def scroll_to_question(self, question):
        element = self.element_question(question)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Проскроллить до большой кнопки заказа')
    def scroll_to_order_button_big(self):
        element = self.driver.find_element(*HomePageLocators.ORDER_BUTTON_BIG)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажать на вопрос')
    def click_question(self, question):
        self.wait_for_clickable_question(question)
        element = self.element_question(question)
        element.click()

    def check_answers(self, answer):
        answer_text = self.driver.find_element(By.XPATH, f'.//p[text() = "{answer}"]')
        assert answer_text.is_displayed()

    def check_answers_to_questions(self, question, answer):
        self.scroll_to_question(question)
        self.click_question(question)
        self.check_answers(answer)
