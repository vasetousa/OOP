from class_Inheritance.project_zoo import Car


class SportsCar(Car):

    def race(self):
        return "racing..."


sc = SportsCar()
print(sc.drive())
print(sc.move())
print(sc.race())
