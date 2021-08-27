from rename_to_project_and_finish.appliances.appliance import Appliance
from rename_to_project_and_finish.people.child import Child


class Room:
    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):  # *args = [[appliances], [children]]
        total_expenses = 0
        for list_el in args:
            for element in list_el:
                if isinstance(element, Appliance):
                    total_expenses += element.get_monthly_expense()
                elif isinstance(element, Child):
                    total_expenses += element.cost * 30
        self.expenses = total_expenses
