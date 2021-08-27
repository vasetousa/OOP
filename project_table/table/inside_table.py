from project_astro.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value not in range(1, 51):
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        self.__capacity = value
