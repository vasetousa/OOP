class Equipment:
    ID = 0

    def __init__(self, name):
        self.name = name
        Equipment.ID += 1
        self.id = Equipment.ID

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.ID + 1
