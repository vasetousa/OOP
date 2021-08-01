class Product:
    name: str
    quantity: int

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}: {self.quantity}'

    def decrease(self, quantity: int):
        if quantity <= quantity:
            self.quantity -= quantity

    def increase(self, quantity: int):
        self.quantity += quantity
