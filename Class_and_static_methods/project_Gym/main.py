from Class_and_static_methods.project_Gym.customer import Customer
from Class_and_static_methods.project_Gym.equipment import Equipment
from Class_and_static_methods.project_Gym.exercise_plan import ExercisePlan
from Class_and_static_methods.project_Gym.gym import Gym
from Class_and_static_methods.project_Gym.subscription import Subscription
from Class_and_static_methods.project_Gym.trainer import Trainer

# c = Customer("Gosho", "1 rue ......", "abv@abv.bg")
# print(c)
# cc = Customer("Pesho", "15 rue ......", "abvP@abv.bg")
# print(cc)
# print(Customer.get_next_id())
# e = Equipment("Wheels")
# print(e)
# plan = ExercisePlan(3, 1, 30)
# print(plan)
# s = Subscription("14.05.2020", 1, 1, 1)
# print(s)
# print(Subscription.get_next_id())

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
