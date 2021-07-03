class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = int(health)

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"

# po = Pokemon("Koko-Boko", 100)
# print(po.pokemon_details())