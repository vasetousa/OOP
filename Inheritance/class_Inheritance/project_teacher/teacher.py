from Inheritance.class_Inheritance.project_teacher.person import Person
from Inheritance.class_Inheritance.project_teacher.employee import Employee


class Teacher(Person, Employee):
    def __init__(self):
        Person.__init__(self)
        Employee.__init__(self)

    @staticmethod
    def teach():
        return "teaching..."


t = Teacher()
print(t.teach())
print(t.sleep())
print(t.get_fired())
