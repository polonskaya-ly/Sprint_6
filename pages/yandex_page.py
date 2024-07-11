from ..url_config import UrlConfig
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class YandexPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_yandex_page(self):
        WebDriverWait(self.driver, 2).until_not(expected_conditions.url_to_be('about:blank'))

    def check_yandex_page_url(self):
        self.wait_for_load_yandex_page()
        assert self.driver.current_url == UrlConfig.yandex_page
