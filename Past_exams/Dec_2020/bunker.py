class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        foods = [fo for fo in self.supplies if fo.__class__.__name__ == "FoodSupply"]
        if not foods:
            raise IndexError("There are no food supplies left!")
        return foods

    @property
    def water(self):
        waters = [wo for wo in self.supplies if wo.__class__.__name__ == "WaterSupply"]
        if not waters:
            raise IndexError("There are no water supplies left!")
        return waters

    @property
    def painkillers(self):
        painkillers = [pain for pain in self.medicine if pain.__class__.__name__ == "Painkiller"]
        if not painkillers:
            raise IndexError("There are no painkillers left!")
        return painkillers

    @property
    def salves(self):
        salves = [sal for sal in self.medicine if type(sal).__class__.__name__ == "Salve"]
        if not salves:
            raise IndexError("There are no salves left!")
        return salves

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        meds = [x for x in self.medicine if x.__class__.__name__ == medicine_type]
        if survivor.needs_healing:
            last_pill = meds.pop()
            last_pill.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        susts = [x for x in self.medicine if x.__class__.__name__ == sustenance_type]
        if survivor.needs_sustenance:
            last_sust = susts.pop()
            last_sust.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for sur in self.survivors:
            sur.needs -= sur.age * 2

        for sur1 in self.survivors:
            self.sustain(sur1, "WaterSupply")
            self.sustain(sur1, "FoodSupply")


#
# from Dec_2020.medicine.painkiller import Painkiller
# from Dec_2020.medicine.salve import Salve
# from Dec_2020.survivor import Survivor
#
#
# b = Bunker()
# s = Survivor("Pesho", 30)
# b.add_medicine(Salve)
# b.add_medicine(Salve)
# b.add_medicine(Painkiller)
# b.add_medicine(Painkiller)
# print(b.medicine)
# b.heal(s, Painkiller)
