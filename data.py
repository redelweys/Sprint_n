START_ADDRESS = "Хамовнический вал, 34"
DESTINATION_ADDRESS = "Зубовский бульвар, 37"
SAME_ADDRESS_ROUTE_SUMMARY = "Авто Бесплатно В пути 0 мин."

OPTIMAL_MODE = "Оптимальный"
FAST_MODE = "Быстрый"
CUSTOM_MODE = "Свой"

TAXI = "taxi"
DRIVE = "drive"

TRANSPORT_NAMES = {
    "car": "Авто",
    "walk": "Пешком",
    TAXI: "Такси",
    "bike": "Велосипед",
    "scooter": "Самокат",
    DRIVE: "Драйв",
}

MODE_SCENARIOS = (
    (FAST_MODE, OPTIMAL_MODE),
    (OPTIMAL_MODE, FAST_MODE),
)

TAXI_TARIFFS = (
    "Рабочий",
    "Сонный",
    "Отпускной",
    "Разговорчивый",
    "Утешительный",
    "Глянцевый",
)

TAXI_TARIFF_DESCRIPTIONS = {
    "Рабочий": "Для деловых особ, которых отвлекают",
    "Сонный": "Для тех, кто не выспался",
    "Отпускной": "Если пришла пора отдохнуть",
    "Разговорчивый": "Если мысли не выходят из головы",
    "Утешительный": "Если хочется свернуться калачиком",
    "Глянцевый": "Если нужно блистать",
}

WORK_TARIFF = "Рабочий"
