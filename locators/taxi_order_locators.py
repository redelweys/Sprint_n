from selenium.webdriver.common.by import By


class TaxiOrderLocators:
    TARIFF_CARDS = (By.CSS_SELECTOR, ".tariff-picker.shown .tcard")
    TARIFF_NAMES = (By.CSS_SELECTOR, ".tariff-picker.shown .tcard .tcard-title")
    ACTIVE_TARIFF = (By.CSS_SELECTOR, ".tariff-picker.shown .tcard.active")
    PHONE_FIELD = (
        By.XPATH,
        "//div[contains(@class, 'tariff-picker') and contains(@class, 'shown')]"
        "//*[normalize-space(.) = 'Телефон']",
    )
    PAYMENT_METHOD = (
        By.XPATH,
        "//div[contains(@class, 'tariff-picker') and contains(@class, 'shown')]"
        "//*[normalize-space(.) = 'Способ оплаты']",
    )
    COMMENT_FIELD = (By.ID, "comment")
    REQUIREMENTS_HEADER = (By.CSS_SELECTOR, ".tariff-picker.shown .reqs-header")
    LAPTOP_TABLE_SWITCH = (
        By.CSS_SELECTOR,
        ".tariff-picker.shown .r-type-switch .slider",
    )
    ORDER_BUTTON = (By.CSS_SELECTOR, ".smart-button")
    WAITING_ORDER_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'order') and contains(@class, 'shown')]"
        "//*[normalize-space(.) = 'Поиск машины']",
    )
    ORDER_TIMER = (
        By.XPATH,
        "//div[contains(@class, 'order') and contains(@class, 'shown')]"
        "//*[contains(normalize-space(.), ':') and not(*)]",
    )
    CANCEL_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'order') and contains(@class, 'shown')]"
        "//div[contains(@class, 'order-btn-group')][.//div[normalize-space(.) = 'Отменить']]"
        "//button",
    )
    ORDER_DETAILS_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'order') and contains(@class, 'shown')]"
        "//div[contains(@class, 'order-btn-group')][.//div[normalize-space(.) = 'Детали']]"
        "//button",
    )
    COMPLETED_ORDER_TITLE = (
        By.CSS_SELECTOR,
        ".order.shown .order-header-title",
    )
    CAR_NUMBER = (By.CSS_SELECTOR, ".order.shown .order-number .number")
    CAR_IMAGE = (By.CSS_SELECTOR, ".order.shown .order-number img")
    DRIVER_RATING = (By.CSS_SELECTOR, ".order.shown .order-btn-rating")
    DRIVER_NAME = (
        By.XPATH,
        "//div[contains(@class, 'order') and contains(@class, 'shown')]"
        "//div[contains(@class, 'order-btn-group')][.//div[contains(@class, 'order-btn-rating')]]"
        "/div[last()]",
    )
    ORDER_COST = (
        By.XPATH,
        "//div[contains(@class, 'order-details-row')][.//div[normalize-space(.) = 'Еще про поездку']]"
        "//div[contains(@class, 'o-d-sh')]",
    )
    ORDER_WINDOW = (By.CSS_SELECTOR, ".order.shown")

    @staticmethod
    def tariff_card(name):
        return (
            By.XPATH,
            "//div[contains(@class, 'tariff-picker') and contains(@class, 'shown')]"
            "//div[contains(@class, 'tcard')][.//div[contains(@class, 'tcard-title')"
            f" and normalize-space(.) = '{name}']]",
        )

    @staticmethod
    def tariff_info_button(name):
        return (
            By.XPATH,
            TaxiOrderLocators.tariff_card(name)[1] + "//button[contains(@class, 'tcard-i')]",
        )

    @staticmethod
    def tariff_tooltip(name):
        return (
            By.XPATH,
            TaxiOrderLocators.tariff_card(name)[1] + "//*[@data-id = 'tooltip']",
        )

    @staticmethod
    def tariff_price(name):
        return (
            By.XPATH,
            TaxiOrderLocators.tariff_card(name)[1]
            + "//div[contains(@class, 'tcard-price')]",
        )
