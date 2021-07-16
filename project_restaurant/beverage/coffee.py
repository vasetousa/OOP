from project_restaurant.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    __caffeine: float
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, self.__class__.PRICE, self.__class__.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
