from project_Animal.animals.animal import Mammal
from project_Animal.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_required = [Fruit, Vegetable]
        self.weight_per_food = 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_required = [Meat]
        self.weight_per_food = 0.4

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_required = [Meat, Vegetable]
        self.weight_per_food = 0.3

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_required = [Meat]
        self.weight_per_food = 1

    def make_sound(self):
        return "ROAR!!!"
