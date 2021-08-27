from rename_to_project_and_finish.appliances.fridge import Fridge
from rename_to_project_and_finish.appliances.laptop import Laptop
from rename_to_project_and_finish.appliances.tv import TV
from rename_to_project_and_finish.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        count = len(children) + 2
        super().__init__(family_name, salary_one + salary_two, count)
        self.room_cost = 30
        self.appliances = [TV(), Fridge(), Laptop()] * count
        self.children = list(children)

        self.calculate_expenses(self.appliances, self.children)