from abc import ABC, abstractmethod


""" Main class for all Shapes"""
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


""" Different shapes, calculate their areas """
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, side, h):
        self.side = side
        self.h = h

    def calculate_area(self):
        return (self.side * self.h)/2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.1415

    def calculate_area(self):
        return (self.radius ** 2) * self.pi


""" Checks if the shapes value given is a list, if all list items are object of Shape
 and calculates the total area of all Shape areas combined """
class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total

    def add_shape(self, shape):
        self.shapes.append(shape)

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise TypeError("Should be of type list")
        res = [shape for shape in value if not isinstance(shape, Shape)] # empty when all objects are Shape
        if res:
            raise TypeError("All elements must be of type Shape")
        self.__shapes = value


shapes = [Rectangle(1, 6), Triangle(2, 3), Circle(6)]
# shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)

calculator.add_shape(Triangle(100, 3))
print(f"Adding the shape ...")

print("The total area is: ", calculator.total_area)

