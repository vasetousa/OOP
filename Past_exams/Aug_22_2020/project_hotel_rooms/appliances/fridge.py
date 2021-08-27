from rename_to_project_and_finish.appliances.appliance import Appliance


class Fridge(Appliance):
    def __init__(self):
        super().__init__(1.2)