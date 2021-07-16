class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION  # per kilometer

    def drive(self, kilometers):
        fuel_needed = kilometers * self.fuel_consumption
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
