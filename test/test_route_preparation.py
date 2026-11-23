import allure
import pytest

from data import CUSTOM_MODE, DRIVE, MODE_SCENARIOS, TAXI, TRANSPORT_NAMES


class TestRoutePreparation:
    @pytest.mark.parametrize("initial_mode, mode", MODE_SCENARIOS, ids=("optimal", "fast"))
    @allure.title("Режим «{mode}» становится активным, видны стоимость и время в пути")
    def test_selected_mode_shows_route_metrics(self, route_with_addresses, initial_mode, mode):
        route_with_addresses.select_mode(initial_mode)
        route_with_addresses.select_mode(mode)

        assert route_with_addresses.get_active_mode() == mode
        assert route_with_addresses.are_route_metrics_visible(), "Стоимость или время в пути отсутствуют"

    @allure.title("Режим «Свой» позволяет выбрать шесть видов транспорта")
    def test_custom_mode_shows_available_transports(self, route_with_addresses):
        route_with_addresses.select_mode(CUSTOM_MODE)

        assert route_with_addresses.get_active_mode() == CUSTOM_MODE
        assert all(
            route_with_addresses.is_transport_available(transport)
            for transport in TRANSPORT_NAMES
        ), "В режиме «Свой» доступны не все виды транспорта"

    @pytest.mark.parametrize(
        "transport, name",
        (
            pytest.param("walk", TRANSPORT_NAMES["walk"], id="walk"),
            pytest.param(TAXI, TRANSPORT_NAMES[TAXI], id=TAXI),
            pytest.param(
                "car",
                TRANSPORT_NAMES["car"],
                id="car",
                marks=pytest.mark.xfail(
                    reason=(
                        "Стенд иногда оставляет такси активным после нативного "
                        "клика по карточке «Авто» в режиме «Свой»"
                    ),
                    raises=pytest.RaisesExc(
                        AssertionError,
                        match=r"^После выбора транспорта «Авто» его сводка не появилась\.",
                    ),
                    strict=False,
                ),
            ),
            pytest.param(
                "bike",
                TRANSPORT_NAMES["bike"],
                id="bike",
                marks=pytest.mark.xfail(
                    reason=(
                        "Стенд иногда оставляет такси активным после нативного "
                        "клика по карточке «Велосипед» в режиме «Свой»"
                    ),
                    raises=pytest.RaisesExc(
                        AssertionError,
                        match=r"^После выбора транспорта «Велосипед» его сводка не появилась\.",
                    ),
                    strict=False,
                ),
            ),
            pytest.param(
                "scooter",
                TRANSPORT_NAMES["scooter"],
                id="scooter",
                marks=pytest.mark.xfail(
                    reason=(
                        "Стенд иногда оставляет такси активным после клика "
                        "по карточке самоката в режиме «Свой»"
                    ),
                    raises=pytest.RaisesExc(
                        AssertionError,
                        match=r"^После выбора транспорта «Самокат» его сводка не появилась\.",
                    ),
                    strict=False,
                ),
            ),
            pytest.param(DRIVE, TRANSPORT_NAMES[DRIVE], id=DRIVE),
        ),
    )
    @allure.title("В режиме «Свой» в сводке указан выбранный транспорт «{name}»")
    def test_custom_mode_shows_selected_transport_metrics(
        self, route_with_addresses, transport, name
    ):
        route_with_addresses.select_mode(CUSTOM_MODE)
        route_with_addresses.select_transport(transport)

        assert route_with_addresses.is_transport_summary_visible(name), (
            f"После выбора транспорта «{name}» его сводка не появилась. "
            f"{route_with_addresses.describe_transport_selection()}"
        )
        assert route_with_addresses.are_route_metrics_visible(), "Стоимость или время в пути отсутствуют"

    @allure.title("Кнопка «Вызвать такси» открывает форму заказа")
    def test_taxi_button_opens_order_form(self, route_with_addresses):
        route_with_addresses.select_mode(CUSTOM_MODE)
        route_with_addresses.select_transport(TAXI)
        route_with_addresses.open_taxi_order_form()

        assert route_with_addresses.is_taxi_order_form_visible(), "Форма заказа такси не открылась"

    @allure.title("Кнопка «Забронировать» открывает форму бронирования Драйва")
    def test_drive_button_opens_booking_form(self, route_with_addresses):
        route_with_addresses.select_mode(CUSTOM_MODE)
        route_with_addresses.select_transport(DRIVE)
        route_with_addresses.open_drive_booking_form()

        assert route_with_addresses.is_drive_booking_form_visible(), "Форма бронирования не открылась"
