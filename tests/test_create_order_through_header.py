import allure
import pytest

from ..pages.yandex_page import YandexPage
from ..pages.track_page import TrackPage
from ..pages.rent_page import RentPage
from ..pages.home_page import HomePage
from ..pages.order_page import OrderPage


@pytest.mark.usefixtures("driver")
class TestCreateOrder:

    driver = None

    @allure.title("Создание заказа через хейдер")
    def test_create_order_through_small_order_button(self, rent_name, rent_data, random_metro, random_period, random_day):
        home_page = HomePage(self.driver)
        home_page.click_order_button_small()
        order_page = OrderPage(self.driver)
        order_page.fill_order_form(rent_name, rent_data, random_metro)
        rent_page = RentPage(self.driver)
        rent_page.fill_rent_terms(random_period, random_day)
        rent_page.click_confirm_create_order()
        rent_page.check_success_order_message()
        rent_page.click_status_button()
        track_page = TrackPage(self.driver)
        track_page.check_move_to_home_page()

    @allure.title("Создание заказа через большую кнопку заказа")
    def test_create_order_through_big_order_button(self, rent_name,rent_data, random_metro, random_period, random_day):
          home_page = HomePage(self.driver)
          home_page.scroll_to_order_button_big()
          home_page.click_order_button_big()
          order_page = OrderPage(self.driver)
          order_page.fill_order_form(rent_name, rent_data, random_metro)
          rent_page = RentPage(self.driver)
          rent_page.fill_rent_terms(random_period, random_day)
          rent_page.click_confirm_create_order()
          rent_page.check_success_order_message()
          rent_page.click_status_button()
          track_page = TrackPage(self.driver)
          track_page.click_yandex_button()
          track_page.move_to_another_window()
          yandex_page = YandexPage(self.driver)
          yandex_page.check_dzen_page_url()
