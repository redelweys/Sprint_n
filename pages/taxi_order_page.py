import re

import allure
from selenium.common.exceptions import TimeoutException

from locators.taxi_order_locators import TaxiOrderLocators
from pages.base_page import BasePage


class TaxiOrderPage(BasePage):
    @allure.step("Получить названия тарифов такси")
    def get_tariff_names(self):
        return self.get_visible_texts(TaxiOrderLocators.TARIFF_NAMES)

    @allure.step("Проверить, что выбран один тариф")
    def has_one_active_tariff(self):
        return self.count_visible_elements(TaxiOrderLocators.ACTIVE_TARIFF) == 1

    @allure.step("Навести курсор на описание тарифа «{name}»")
    def hover_tariff_info(self, name):
        self.select_tariff(name)
        self.hover(TaxiOrderLocators.tariff_info_button(name))

    @allure.step("Получить описание тарифа «{name}»")
    def get_tariff_description(self, name):
        return self.get_visible_text(TaxiOrderLocators.tariff_tooltip(name))

    @allure.step("Проверить поля формы заказа такси")
    def are_order_fields_visible(self):
        return all(
            self.is_visible(locator)
            for locator in (
                TaxiOrderLocators.PHONE_FIELD,
                TaxiOrderLocators.PAYMENT_METHOD,
                TaxiOrderLocators.COMMENT_FIELD,
                TaxiOrderLocators.REQUIREMENTS_HEADER,
            )
        )

    @allure.step("Выбрать тариф «{name}»")
    def select_tariff(self, name):
        self.click(TaxiOrderLocators.tariff_card(name))

    @allure.step("Получить стоимость тарифа «{name}»")
    def get_tariff_price(self, name):
        return self._price_amount(self.get_visible_text(TaxiOrderLocators.tariff_price(name)))

    @allure.step("Включить требование «Столик для ноутбука»")
    def enable_laptop_table(self):
        self.click(TaxiOrderLocators.REQUIREMENTS_HEADER)
        self.click(TaxiOrderLocators.LAPTOP_TABLE_SWITCH)

    @allure.step("Нажать «Ввести номер и заказать»")
    def submit_order(self):
        self.click(TaxiOrderLocators.ORDER_BUTTON)

    @allure.step("Проверить окно поиска машины")
    def is_waiting_for_car_visible(self):
        return all(
            self.is_visible(locator)
            for locator in (
                TaxiOrderLocators.WAITING_ORDER_TITLE,
                TaxiOrderLocators.ORDER_TIMER,
                TaxiOrderLocators.CANCEL_ORDER_BUTTON,
                TaxiOrderLocators.ORDER_DETAILS_BUTTON,
            )
        )

    @allure.step("Дождаться окна совершенного заказа")
    def is_completed_order_visible(self):
        try:
            self.wait_until(
                lambda _driver: re.fullmatch(
                    r"\d+ мин\. и приедет",
                    self.get_current_text(TaxiOrderLocators.COMPLETED_ORDER_TITLE) or "",
                ),
                timeout=40,
            )
        except TimeoutException:
            return False
        return all(
            self.is_visible(locator)
            for locator in (
                TaxiOrderLocators.CAR_NUMBER,
                TaxiOrderLocators.CAR_IMAGE,
                TaxiOrderLocators.DRIVER_RATING,
                TaxiOrderLocators.DRIVER_NAME,
                TaxiOrderLocators.CANCEL_ORDER_BUTTON,
                TaxiOrderLocators.ORDER_DETAILS_BUTTON,
            )
        )

    @allure.step("Открыть детали поездки")
    def open_order_details(self):
        self.click(TaxiOrderLocators.ORDER_DETAILS_BUTTON)

    @allure.step("Получить стоимость в деталях поездки")
    def get_order_cost(self):
        return self._price_amount(self.get_visible_text(TaxiOrderLocators.ORDER_COST))

    @allure.step("Отменить заказ")
    def cancel_order(self):
        self.click(TaxiOrderLocators.CANCEL_ORDER_BUTTON)

    @allure.step("Проверить, что окно заказа закрыто")
    def is_order_window_closed(self):
        return self.is_invisible(TaxiOrderLocators.ORDER_WINDOW)

    @staticmethod
    def _price_amount(value):
        return re.search(r"\d+", value).group()
