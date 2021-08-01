from project_restaurant.product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters: float):
        self.__milliliters = milliliters
        super().__init__(name, price)

    @property
    def milliliters(self):
        return self.__milliliters
