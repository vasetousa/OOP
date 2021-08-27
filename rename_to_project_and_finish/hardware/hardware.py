class Hardware:
    components = []

    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = Hardware.components

    @staticmethod
    def install(software):
        Hardware.components.append(software)

    @staticmethod
    def uninstall(software):
        Hardware.components.remove(software)
