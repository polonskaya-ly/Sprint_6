from ..url_config import UrlConfig


class YandexPage:

    def __init__(self, driver):
        self.driver = driver

    def check_dzen_page_url(self):
        assert self.driver.current_url == UrlConfig.yandex_page


