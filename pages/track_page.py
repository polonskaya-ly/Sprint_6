import time
import allure
from ..url_config import UrlConfig
from ..locators import TrackPageLocators


class TrackPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на лого Самоката')
    def click_logo_button(self):
        self.driver.find_element(*TrackPageLocators.LOGO_BUTTON).click()

    @allure.step('Нажать на лого Яндекса')
    def click_yandex_button(self):
        self.driver.find_element(*TrackPageLocators.YANDEX_BUTTON).click()
        time.sleep(2)

    def check_move_to_home_page(self):
        self.click_logo_button()
        assert self.driver.current_url == UrlConfig.domain

    def move_to_another_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
