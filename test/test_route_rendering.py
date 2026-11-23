import allure

from data import DESTINATION_ADDRESS, START_ADDRESS


class TestRouteRendering:
    @allure.title("На карте видны точки начала и конца маршрута")
    def test_route_displays_start_and_destination_pins(self, routes_page):
        routes_page.enter_route(START_ADDRESS, DESTINATION_ADDRESS)

        assert routes_page.is_start_pin_visible(), "На карте нет точки начала маршрута"
        assert routes_page.is_destination_pin_visible(), "На карте нет точки конца маршрута"
