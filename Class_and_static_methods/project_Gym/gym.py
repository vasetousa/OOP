class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        result = ''
        current_id = [el.ID for el in self.subscriptions if el.ID == subscription_id]
        for sub in self.subscriptions:
            if sub.ID == subscription_id:
                subscription_needed = sub
                cus_id = sub.customer_id
                tr_id = sub.trainer_id
                eq_id = tr_id
                plan_id = cus_id

                customer_needed = [cus for cus in self.customers if cus.ID == cus_id]
                trainer_needed = [tr for tr in self.trainers if tr.ID == tr_id]
                plan_needed = [pl for pl in self.plans if pl.ID == tr_id]
                equipment_needed = [eq for eq in self.equipment if eq.ID == cus_id]

        nl = '\n'
        result += str(subscription_needed).strip("[]") + nl
        result += str(customer_needed).strip("[]") + nl
        result += str(trainer_needed).strip("[]") + nl
        result += str(equipment_needed).strip("[]") + nl
        result += str(plan_needed).strip("[]")
        return result
