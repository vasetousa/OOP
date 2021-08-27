from rename_to_project_and_finish.appliances.fridge import Fridge
from rename_to_project_and_finish.appliances.stove import Stove
from rename_to_project_and_finish.appliances.tv import TV
from rename_to_project_and_finish.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * 2
        self.calculate_expenses(self.appliances)