from project_restaurant.vehicle import Vehicle
from project_restaurant.family_car import FamilyCar
from project_restaurant.sport_car import SportCar
from project_restaurant.motorcycle import Motorcycle
from project_restaurant.race_motorcycle import RaceMotorcycle
from project_restaurant.cross_motorcycle import CrossMotorcycle
from project_restaurant.car import Car


vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)