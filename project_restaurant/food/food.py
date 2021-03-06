from project_restaurant.product import Product


class Food(Product):
    __grams: float

    def __init__(self, name, price, grams: float):
        super().__init__(name, price)
        self.__grams = grams


    @property
    def grams(self):
        return self.__grams

