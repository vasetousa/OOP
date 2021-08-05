from project_Animal.animals.animal import Bird
from project_Animal.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)
        self.food_required = [Meat]
        self.weight_per_food = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)
        self.food_required = [Meat, Vegetable, Fruit, Seed]
        self.weight_per_food = 0.35

    def make_sound(self):
        return "Cluck"

