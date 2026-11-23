import allure

from locators.routes_locators import RoutesLocators
from pages.base_page import BasePage
from urls import ROUTES_URL


class RoutesPage(BasePage):
    @allure.step("Открыть Яндекс.Маршруты")
    def open(self):
        self.open_url(ROUTES_URL)

    @allure.step("Указать адреса «Откуда» и «Куда»")
    def enter_route(self, start, destination):
        self.fill(RoutesLocators.START_ADDRESS_INPUT, start)
        self.fill(RoutesLocators.DESTINATION_ADDRESS_INPUT, destination)
        self.press_tab(RoutesLocators.DESTINATION_ADDRESS_INPUT)

    @allure.step("Проверить отображение точки начала маршрута")
    def is_start_pin_visible(self):
        return self.is_visible(RoutesLocators.START_PIN)

    @allure.step("Проверить отображение точки конца маршрута")
    def is_destination_pin_visible(self):
        return self.is_visible(RoutesLocators.DESTINATION_PIN)

    @allure.step("Проверить отображение блока выбора маршрута")
    def is_route_selection_visible(self):
        return self.is_visible(RoutesLocators.ROUTE_SELECTION_BLOCK)

    @allure.step("Прочитать сводку маршрута")
    def get_route_summary(self):
        summary = self.get_visible_text(RoutesLocators.ROUTE_SUMMARY)
        return " ".join(summary.split())

    @allure.step("Выбрать режим «{name}»")
    def select_mode(self, name):
        self.click(RoutesLocators.mode(name))

    @allure.step("Прочитать название активного режима")
    def get_active_mode(self):
        return self.get_visible_text(RoutesLocators.ACTIVE_MODE)

    @allure.step("Проверить доступность транспорта «{icon_name}»")
    def is_transport_available(self, icon_name):
        return self.is_visible(RoutesLocators.available_transport(icon_name))

    @allure.step("Выбрать транспорт «{icon_name}»")
    def select_transport(self, icon_name):
        self.click(RoutesLocators.available_transport(icon_name), record_pointer_events=True)

    @allure.step("Проверить, что стоимость и время в пути отображаются")
    def are_route_metrics_visible(self):
        return bool(
            self.get_visible_text(RoutesLocators.ROUTE_COST).strip()
            and self.get_visible_text(RoutesLocators.ROUTE_DURATION).strip()
        )

    @allure.step("Дождаться сводки для транспорта «{name}»")
    def is_transport_summary_visible(self, name):
        return self.is_visible(RoutesLocators.summary_for_transport(name))

    def describe_transport_selection(self):
        mode = self.get_current_text(RoutesLocators.ACTIVE_MODE)
        icon = self.get_current_attribute(RoutesLocators.ACTIVE_TRANSPORT_ICON, "src")
        summary = self.get_current_text(RoutesLocators.ROUTE_SUMMARY)
        events = self.get_pointer_events()
        return (
            f"Активный режим: {mode!r}, иконка транспорта: {icon!r}, сводка: {summary!r}. "
            f"События мыши: {events!r}"
        )

    @allure.step("Нажать «Вызвать такси»")
    def open_taxi_order_form(self):
        self.click(RoutesLocators.CALL_TAXI_BUTTON)

    @allure.step("Проверить, что форма заказа такси открыта")
    def is_taxi_order_form_visible(self):
        return self.is_visible(RoutesLocators.TAXI_ORDER_FORM_BUTTON)

    @allure.step("Нажать «Забронировать» в Драйве")
    def open_drive_booking_form(self):
        self.click(RoutesLocators.RESERVE_DRIVE_BUTTON)

    @allure.step("Проверить, что форма бронирования Драйва открыта")
    def is_drive_booking_form_visible(self):
        return self.is_visible(RoutesLocators.DRIVE_BOOKING_FORM_BUTTON)
