from project_astro.astronaut.astronaut_repository import AstronautRepository
from project_astro.astronaut.biologist import Biologist
from project_astro.astronaut.geodesist import Geodesist
from project_astro.astronaut.meteorologist import Meteorologist
from project_astro.planet.planet import Planet
from project_astro.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.number_of_successful_missions = 0
        self.number_of_not_completed_missions = 0

    def add_astronaut(self, astronaut_type, name):

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        if astronaut_type == "Biologist":
            self.astronaut_repository.astronauts.append(Biologist(name))  # create the type astro
            return f"Successfully added {astronaut_type}: {name}."
        elif astronaut_type == "Geodesist":
            self.astronaut_repository.astronauts.append(Geodesist(name))
            return f"Successfully added {astronaut_type}: {name}."
        elif astronaut_type == "Meteorologist":
            self.astronaut_repository.astronauts.append(Meteorologist(name))
            return f"Successfully added {astronaut_type}: {name}."
        else:
            raise Exception("Astronaut type is not valid!")

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)  # create a planet
        planet.items = items.split(", ")  # add the items to the list
        self.planet_repository.planets.append(planet)  # add the planet to the repo
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exists!")

        self.astronaut_repository.astronauts.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        astro_count = 0
        planet = [pl for pl in self.planet_repository.planets if pl.name == planet_name][0]
        if not planet:
            raise Exception("Invalid planet name!")

        sorted_astronauts = sorted([astron for astron in self.astronaut_repository.astronauts if astron.oxygen > 30],
                                   key=lambda x: -x.oxygen)  # list of all astronauts with oxy above 30
        counter = 0     # astro counter

        if not sorted_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        for astronaut in sorted_astronauts:
            if planet.items:
                counter += 1
                for item in planet.items[::-1]:

                    astronaut.backpack.append(item)
                    planet.items.remove(item)
                    astronaut.breathe()
                    if astronaut.oxygen <= 0:
                        break
            else:
                self.number_of_successful_missions += 1
                return f"Planet: {planet_name} was explored. {counter} astronauts participated" \
                       f" in collecting items."

        return "Mission is not completed."

    def report(self):
        nl = "\n"
        result = [f"{self.number_of_successful_missions} successful missions!",
                  f"{self.number_of_not_completed_missions} missions were not completed!",
                  f"Astronauts' info:"]
        for astro in self.astronaut_repository.astronauts:
            result.extend([f"Name: {astro.name}",
                           f"Oxygen: {astro.oxygen}",
                           f"Backpack items: {', '.join(astro.backpack) if astro.backpack else 'none'}"])

        return nl.join(result)




