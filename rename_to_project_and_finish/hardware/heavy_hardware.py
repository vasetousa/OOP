from rename_to_project_and_finish.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Heavy", capacity * 2, memory * 0.75)