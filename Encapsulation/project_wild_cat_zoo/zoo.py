class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: object):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker: str):
        for employee in self.workers:
            if employee.name == worker:
                self.workers.remove(employee)
                return f"{worker} fired successfully"
        return f"There is no {worker} in the zoo"

    def pay_workers(self):
        # sum_all_salaries = 0
        # for employee in self.workers:
        #     sum_all_salaries += employee.salary
        sum_all_salaries = sum(map(lambda worker: worker.salary, self.workers))

        if self.__budget >= sum_all_salaries:
            self.__budget -= sum_all_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_all_animals_expenses = sum(map(lambda animal: animal.money_for_care, self.animals))
        if sum_all_animals_expenses <= self.__budget:
            self.__budget -= sum_all_animals_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = 0
        lions_info = []
        tigers = 0
        tigers_info = []
        cheetahs = 0
        cheetahs_info = []

        nl = "\n"
        result = f"You have {len(self.animals)} animals" + nl

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions += 1
                lions_info.append(repr(animal))
            elif animal.__class__.__name__ == "Tiger":
                tigers += 1
                tigers_info.append(repr(animal))
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs += 1
                cheetahs_info.append(repr(animal))

        result += f"----- {lions} Lions:" + nl
        lions_data = nl.join(lions_info)
        result += lions_data + nl

        result += f"----- {tigers} Tigers:" + nl
        tigers_data = nl.join(tigers_info)
        result += tigers_data + nl

        result += f"----- {cheetahs} Cheetahs:" + nl
        cheetahs_data = nl.join(cheetahs_info)
        result += cheetahs_data

        return result

    def workers_status(self):
        caretakers = 0
        caretakers_info = []
        keepers = 0
        keepers_info = []
        vets = 0
        vets_info = []

        nl = "\n"
        result = f"You have {len(self.workers)} workers" + nl

        for employee in self.workers:
            if employee.__class__.__name__ == "Caretaker":
                caretakers += 1
                caretakers_info.append(repr(employee))
            elif employee.__class__.__name__ == "Keeper":
                keepers += 1
                keepers_info.append(repr(employee))
            elif employee.__class__.__name__ == "Vet":
                vets += 1
                vets_info.append(repr(employee))

        result += f"----- {keepers} Keepers:" + nl
        keepers_data = nl.join(keepers_info)
        result += keepers_data + nl

        result += f"----- {caretakers} Caretakers:" + nl
        caretakers_data = nl.join(caretakers_info)
        result += caretakers_data + nl

        result += f"----- {vets} Vets:" + nl
        vets_data = nl.join(vets_info)
        result += vets_data

        return result