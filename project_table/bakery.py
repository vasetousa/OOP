from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        searched_food = [f for f in self.food_menu if f.name == name]
        if searched_food:
            raise Exception(f"{food_type} {name} is already in the menu!")
        
        if food_type == "Bread":
            self.food_menu.append(Bread(name, price))
        elif food_type == "Cake":
            self.food_menu.append(Cake(name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if drink_type == "Water":
            drink = Water(name, portion, brand)
        else:
            drink = Tea(name, portion, brand)
        self.food_menu.append(drink)
        return f"Added {drink.name} ({drink_type}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        find_table = [t for t in self.tables_repository if t.table_number == table_number]
        if find_table:
            find_table = find_table[0]
            raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
        else:
            table = InsideTable(table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        table = [t.capacity for t in self.tables_repository if t.capacity <= number_of_people][0]
        table.is_reserved = True
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number, *food_name):
        find_table = [t for t in self.tables_repository if t.table_number == table_number]
        if not find_table:
            raise Exception(f"Could not find table {table_number}")
        find_table = find_table[0]
        food_to_order = [f for f in self.food_menu if f.name in food_name]

    def order_drink(self, table_number, *drinks_name):
        pass

    def leave_table(self, table_number):
        pass

    def get_free_tables_info(self):
        pass

    def get_total_income(self):
        return f"Total income: {self.total_income}lv"




from project_astro.baked_food.bread import Bread
from project_astro.baked_food.cake import Cake
from project_astro.drink.tea import Tea
from project_astro.drink.water import Water
from project_astro.table.inside_table import InsideTable
from project_astro.table.outside_table import OutsideTable



# b = Bakery("Gusto")
# print(b)
# print(b.add_food("Bread", 150)) # name, portion
# print(b.add_drink("Water", "Water", 1, "tea")) # name, portion, price, brand
# print()
# print(b.add_table("OutsideTable", 1, 5))
