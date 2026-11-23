import allure

from data import DESTINATION_ADDRESS, SAME_ADDRESS_ROUTE_SUMMARY, START_ADDRESS


class TestRouteSelection:
    @allure.title("При разных адресах отображается блок выбора маршрута")
    def test_different_addresses_show_route_selection(self, routes_page):
        routes_page.enter_route(START_ADDRESS, DESTINATION_ADDRESS)

        assert routes_page.is_route_selection_visible(), "Блок выбора маршрута не появился"

    @allure.title("При одинаковых адресах поездка на авто бесплатная и занимает 0 минут")
    def test_same_address_shows_free_zero_minute_route(self, routes_page):
        routes_page.enter_route(START_ADDRESS, START_ADDRESS)

        assert routes_page.get_route_summary() == SAME_ADDRESS_ROUTE_SUMMARY
