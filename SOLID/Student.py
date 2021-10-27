class Student:
    _id = 0
    def __init__(self, name: str):
        self.name = name
        self.id = Student._id + 1
        Student._id += 1

    def get_name(self):
        return f"Last registered name was: {self.name}. "

    def __str__(self):
        return

class Register:
    def __init__(self, obj):
        self.students = []

    def register_student(self, obj):
        with open("students.txt", "a") as file:
            file.write(str(obj))

    def get_student(self):
        with open("students.txt", "r") as file:
            for line in file.readlines():
                if id in line:
                    return line
        return None

