from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        count = len(children) + 2
        super().__init__(family_name, salary_one + salary_two, count)
        self.room_cost = 30
        self.appliances = [TV(), Fridge(), Laptop()] * count
        self.children = list(children)

        self.calculate_expenses(self.appliances, self.children)