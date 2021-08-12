from unittest import TestCase, main

from Code_testing_Unittests.Tests.car_manager import Car


class TestCar(TestCase):
    def setUp(self) -> None:
        self.car = Car(make="Audi", model="A6", fuel_consumption=1, fuel_capacity=4)

    def test_are_all_atributes_set_while_init(self):
        self.assertEqual("Audi", self.car.make)
        self.assertEqual(0, self.car.fuel_amount)
        self.assertEqual("A6", self.car.model)
        self.assertEqual(1, self.car.fuel_consumption)
        self.assertEqual(4, self.car.fuel_capacity)

    def test_is_adds_fuel_to_the_car(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(2)
        self.assertEqual(2, self.car.fuel_amount)

    def test_negative_fuel_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -2
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))
        self.car.fuel_capacity = 10
        self.assertEqual(10, self.car.fuel_capacity)

    def test_negative_fuel_consumption_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -2
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))
        self.car.fuel_consumption = 10
        self.assertEqual(10, self.car.fuel_consumption)

    def test_negative_refuel_amount_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-2)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.car.fuel_amount = 10
        self.assertEqual(10, self.car.fuel_amount)

    def test_empty_model_name_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))
        self.assertEqual("A6", self.car.model)

    def test_empty_make_name_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))
        self.assertEqual("Audi", self.car.make)

    def test_drive_car(self):
        self.car.fuel_amount = 0
        with self.assertRaises(Exception) as ex:
            self.car.drive(6)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
        self.car.refuel(10)
        self.car.drive(2)
        self.assertEqual(3.98, self.car.fuel_amount)




if __name__ == "__main__":
    main()

