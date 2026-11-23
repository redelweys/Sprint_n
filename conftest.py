import pytest
from selenium import webdriver

from data import DESTINATION_ADDRESS, FAST_MODE, START_ADDRESS
from pages.routes_page import RoutesPage
from pages.taxi_order_page import TaxiOrderPage


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Запустить Chrome без окна")


@pytest.fixture
def browser(pytestconfig):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1440,1000")
    if pytestconfig.getoption("--headless"):
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def routes_page(browser):
    page = RoutesPage(browser)
    page.open()
    return page


@pytest.fixture
def route_with_addresses(routes_page):
    routes_page.enter_route(START_ADDRESS, DESTINATION_ADDRESS)
    return routes_page


@pytest.fixture
def taxi_order_page(route_with_addresses, browser):
    route_with_addresses.select_mode(FAST_MODE)
    route_with_addresses.open_taxi_order_form()
    return TaxiOrderPage(browser)
