class Trainer:
    ID = 0

    def __init__(self, name):
        self.name = name
        Trainer.ID += 1
        self.id = Trainer.ID

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.ID + 1