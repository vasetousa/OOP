from Encapsulation.project_wild_cat_zoo import Product

class Food(Product):
    name: str
    QUANTITY = 15
    def __init__(self, name):
        super().__init__(name, self.__class__.QUANTITY)
