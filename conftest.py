import pytest
from selenium import webdriver
import random

from .constants import Constants
from .url_config import UrlConfig


@pytest.fixture()
def driver(request):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(UrlConfig.domain)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture
def rent_data():
    address = f"СПб {random.randint(10, 99)}"
    telephone_number = f"+7{random.randint(1000000000, 9999999999)}"
    return address,telephone_number


@pytest.fixture
def rent_name():
    letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'к', 'л', 'м', 'н']
    randomLetter = random.choice(letters)
    name = f"Любовь{randomLetter}"
    surname = f"Пол{randomLetter}"
    return name, surname


@pytest.fixture
def random_metro():
    metro_stations = Constants.metro_stations
    random_metro = random.choice(metro_stations)
    return random_metro


@pytest.fixture
def random_period():
    periods = Constants.periods
    random_period = random.choice(periods)
    return  random_period


@pytest.fixture
def random_day():
    days = Constants.days
    random_day = random.choice(days)
    return  random_day
