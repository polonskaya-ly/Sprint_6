import time
import allure

from selenium.webdriver.common.by import By
from ..url_config import UrlConfig


class TrackPage:
    logo_button = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    yandex_button = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на лого Самоката')
    def click_logo_button(self):
        self.driver.find_element(*self.logo_button).click()

    @allure.step('Нажать на лого Яндекса')
    def click_yandex_button(self):
        self.driver.find_element(*self.yandex_button).click()
        time.sleep(2)

    def check_move_to_home_page(self):
        self.click_logo_button()
        assert self.driver.current_url == UrlConfig.domain

    def move_to_another_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
