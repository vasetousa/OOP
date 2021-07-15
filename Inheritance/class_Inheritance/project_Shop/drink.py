from Encapsulation.project_wild_cat_zoo import Product

class Drink(Product):
    name: str
    QUANTITY = 10

    def __init__(self, name):
        super().__init__(name, self.__class__.QUANTITY)
