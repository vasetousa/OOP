from rename_to_project_and_finish.hardware.hardware import Hardware
from rename_to_project_and_finish.hardware.heavy_hardware import HeavyHardware
from rename_to_project_and_finish.hardware.power_hardware import PowerHardware
from rename_to_project_and_finish.software.express_software import ExpressSoftware


class System:
    _hardware = []
    _software = []
    total_memory_used = 0
    total_capacity_used = 0

    @staticmethod
    def check_for_memory_and_capacity(softwar, hardwar):
        try:
            current_memory_hardwar = hardwar.memory
            current_capacity_hardwar = hardwar.capacity
            current_memory_softwar = softwar.memory_consumption
            current_capacity_softwar = softwar.capacity_consumption

            hard_mem = sum([el.memory for el in System._hardware])  # total hardwar memory
            hard_cap = sum([el.capacity for el in System._hardware])  # total hardwar capacity

            if current_memory_hardwar < current_memory_softwar or current_capacity_hardwar < current_capacity_softwar:
                raise Exception("Software cannot be installed")
        except:
            return Exception("Software cannot be installed")
        System.total_memory_used += current_memory_softwar
        System.total_capacity_used += current_capacity_softwar
        return True

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        phdr = PowerHardware(name, capacity, memory)
        System._hardware.append(phdr)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        hhhdr = HeavyHardware(name, capacity, memory)
        System._hardware.append(hhhdr)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hard = [h for h in System._hardware if h.name == hardware_name][0]
        if not hard:
            return "Hardware does not exist"
        exprsftr = ExpressSoftware(name, capacity_consumption, memory_consumption)
        result = System.check_for_memory_and_capacity(exprsftr, hard)
        if result == True:
            Hardware.install(exprsftr)
            System._software.append(exprsftr)
        else:
            return result

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardo = [h for h in System._hardware if h.name == hardware_name][0]
        if not hardo:
            return "Hardware does not exist"
        lghtsftr = ExpressSoftware(name, capacity_consumption, memory_consumption)
        result = System.check_for_memory_and_capacity(lghtsftr, hardo)
        if result:
            Hardware.install(hardo)
            System._software.append(lghtsftr)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hard = [h for h in System._hardware if h.name == hardware_name]
        if hard:
            hard = hard[0]
        soft = [s for s in System._software if s.name == software_name]
        if soft:
            soft = soft[0]
        if not hard or not soft:
            return "Some of the components do not exist"
        if hard and soft:
            result = Hardware.uninstall(soft)

    @staticmethod
    def analyze():
        string = ""
        string = "System Analysis\n" + f"Hardware Components: {len(System._hardware)}\n" \
                 + f"Software Components: {len(Hardware.components)}\n"
        hard_mem = sum([el.memory for el in System._hardware])
        soft_mem = sum([el.memory_consumption for el in System._software])
        hard_cap = sum([el.capacity for el in System._hardware])
        soft_cap = sum([el.capacity_consumption for el in System._software])
        string += f"Total Operational Memory: {System.total_memory_used} / {int(hard_mem)}\n"
        string += f"Total Capacity Taken: {System.total_capacity_used} / {int(hard_cap)}"
        return string

    @staticmethod
    def system_split():
        pass
