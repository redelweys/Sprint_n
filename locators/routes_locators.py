from selenium.webdriver.common.by import By


class RoutesLocators:
    START_ADDRESS_INPUT = (By.ID, "from")
    DESTINATION_ADDRESS_INPUT = (By.ID, "to")
    START_PIN = (By.CSS_SELECTOR, '[class*="-route-pin__label-0"]')
    DESTINATION_PIN = (By.CSS_SELECTOR, '[class*="-route-pin__label-1"]')
    ROUTE_SELECTION_BLOCK = (By.CSS_SELECTOR, ".type-picker.shown")
    ROUTE_SUMMARY = (By.CSS_SELECTOR, ".type-picker.shown .results-text")
    ACTIVE_MODE = (By.CSS_SELECTOR, ".type-picker.shown .modes-container .mode.active")
    ACTIVE_TRANSPORT_ICON = (
        By.CSS_SELECTOR,
        ".type-picker.shown .types-container .type.active .type-icon",
    )
    ROUTE_COST = (By.CSS_SELECTOR, ".type-picker.shown .results-text .text")
    ROUTE_DURATION = (By.CSS_SELECTOR, ".type-picker.shown .results-text .duration")
    CALL_TAXI_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'results-text')]/button[normalize-space(.) = 'Вызвать такси']",
    )
    RESERVE_DRIVE_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'results-text')]/button[normalize-space(.) = 'Забронировать']",
    )
    TAXI_ORDER_FORM_BUTTON = (
        By.XPATH,
        "//button[@class='smart-button'][starts-with(normalize-space(.), 'Ввести номер и заказать')]",
    )
    DRIVE_BOOKING_FORM_BUTTON = (
        By.XPATH,
        "//button[@class='smart-button'][starts-with(normalize-space(.), 'Ввести права и забронировать')]",
    )

    @staticmethod
    def mode(name):
        return (
            By.XPATH,
            f"//div[contains(@class, 'type-picker') and contains(@class, 'shown')]"
            f"//div[@class='modes-container']/div[normalize-space(.) = '{name}']",
        )

    @staticmethod
    def available_transport(icon_name):
        return (
            By.CSS_SELECTOR,
            ".type-picker.shown .types-container .type:not(.disabled)"
            f':has(> .type-icon:is([src*="/{icon_name}."], [src*="/{icon_name}-"]))',
        )

    @staticmethod
    def summary_for_transport(name):
        return (
            By.XPATH,
            "//div[contains(@class, 'type-picker') and contains(@class, 'shown')]"
            "//div[@class='results-text']/div[@class='text']"
            f"[starts-with(normalize-space(.), '{name} ')]",
        )
