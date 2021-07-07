from typing import List

class Smartphone:
    def __init__(self, memory:int):
        self.memory = memory
        self.is_on: bool = False
        self.apps: List[str] = []   # Pycharm will let me know if I try to add anything, but a string to self.apps

    def power(self):
        if not self.is_on:
            self.is_on = True
        else:
            self.is_on = False

    def install(self, app: str, app_memory: int):
        if app_memory <= self.memory and self.is_on:
            self.memory -= app_memory
            self.apps.append(app)
            return f"Installing {app}"

        elif app_memory <= self.memory and not self.is_on:
            return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"




smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())