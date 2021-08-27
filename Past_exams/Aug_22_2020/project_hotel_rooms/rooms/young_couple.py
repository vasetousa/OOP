from rename_to_project_and_finish.appliances.fridge import Fridge
from rename_to_project_and_finish.appliances.laptop import Laptop
from rename_to_project_and_finish.appliances.tv import TV
from rename_to_project_and_finish.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * 2
        self.calculate_expenses(self.appliances)