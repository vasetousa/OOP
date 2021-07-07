class Person:
    country = "American"

    def __init__(self, name: str, race: str, language: str, education: str, age: int):
        self.name = name
        self.race = race
        self.language = language
        self.education = education
        self.age = age

    """ use as a function with this method, attributes from row 4 are not used here """

    @staticmethod
    def something(*args):
        return  # some result

    """ directly call the function, no need to create an instance (row 26) -> Person.no_instance(). cls = self
    """

    @classmethod
    def no_instance(cls):
        return "Hello " + cls.country


print(Person.no_instance())  # same as row 26-27 when @classmethod
p = Person
print(p.no_instance())