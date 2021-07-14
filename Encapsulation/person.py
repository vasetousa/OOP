# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age


# person = Person("George", 32)
# print(person.get_name())
# print(person.get_age())
#

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):   # value == age from line 4
        if value <= 0:
            raise Exception("Age must be greater than zero!")
        self.__age = value



person = Person("George", 32)
print(person.name)
print(person.age)