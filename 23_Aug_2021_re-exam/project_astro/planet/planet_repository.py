from project_astro.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        if planet in self.planets:
            self.planets.remove(planet)

    def remove(self, planet):
        self.planets.remove(planet)

    def find_by_name(self, name):
        planet = [pl for pl in self.planets if pl.name == name]
        if planet:
            return planet[0]
