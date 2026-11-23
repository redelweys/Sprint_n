import allure
import pytest

from data import TAXI_TARIFF_DESCRIPTIONS, TAXI_TARIFFS, WORK_TARIFF


class TestTaxiOrder:
    @allure.title("Форма заказа содержит шесть тарифов и один активный")
    def test_order_form_has_all_tariffs_and_one_active(self, taxi_order_page):
        assert taxi_order_page.get_tariff_names() == list(TAXI_TARIFFS)
        assert taxi_order_page.has_one_active_tariff(), "В форме должен быть выбран ровно один тариф"

    @pytest.mark.parametrize(
        "tariff, description",
        (
            pytest.param("Рабочий", TAXI_TARIFF_DESCRIPTIONS["Рабочий"], id="work"),
            pytest.param(
                "Сонный",
                TAXI_TARIFF_DESCRIPTIONS["Сонный"],
                id="sleepy",
                marks=pytest.mark.xfail(
                    reason="Описание тарифа «Сонный» не соответствует ТЗ",
                    raises=AssertionError,
                    strict=False,
                ),
            ),
            pytest.param("Отпускной", TAXI_TARIFF_DESCRIPTIONS["Отпускной"], id="vacation"),
            pytest.param(
                "Разговорчивый",
                TAXI_TARIFF_DESCRIPTIONS["Разговорчивый"],
                id="talkative",
                marks=pytest.mark.xfail(
                    reason="Описание тарифа «Разговорчивый» не соответствует ТЗ",
                    raises=AssertionError,
                    strict=False,
                ),
            ),
            pytest.param("Утешительный", TAXI_TARIFF_DESCRIPTIONS["Утешительный"], id="comforting"),
            pytest.param("Глянцевый", TAXI_TARIFF_DESCRIPTIONS["Глянцевый"], id="glossy"),
        ),
    )
    @allure.title("Описание тарифа «{tariff}» соответствует ТЗ")
    def test_tariff_info_matches_specification(self, taxi_order_page, tariff, description):
        taxi_order_page.hover_tariff_info(tariff)

        assert description in taxi_order_page.get_tariff_description(tariff)

    @allure.title("Форма заказа содержит обязательные поля")
    def test_order_form_has_required_fields(self, taxi_order_page):
        assert taxi_order_page.are_order_fields_visible(), "В форме заказа отсутствуют обязательные поля"

    @allure.title("Заказ рабочего тарифа проходит полный сценарий")
    def test_work_tariff_order_flow(self, taxi_order_page):
        taxi_order_page.select_tariff(WORK_TARIFF)
        tariff_price = taxi_order_page.get_tariff_price(WORK_TARIFF)
        taxi_order_page.enable_laptop_table()
        taxi_order_page.submit_order()

        assert taxi_order_page.is_waiting_for_car_visible(), "Окно поиска машины не соответствует ТЗ"
        assert taxi_order_page.is_completed_order_visible(), "Окно совершенного заказа не соответствует ТЗ"

        taxi_order_page.open_order_details()

        assert taxi_order_page.get_order_cost() == tariff_price

        taxi_order_page.cancel_order()

        assert taxi_order_page.is_order_window_closed(), "Окно заказа не закрылось"
