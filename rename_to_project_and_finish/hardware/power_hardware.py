from rename_to_project_and_finish.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Power", capacity * 0.25, memory * 1.75)