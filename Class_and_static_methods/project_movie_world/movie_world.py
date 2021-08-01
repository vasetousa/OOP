from Class_and_static_methods.project_movie_world.customer import Customer
from Class_and_static_methods.project_movie_world.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers = []  # customers list -> objects
        self.dvds = []  # dvd list -> objects

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)
            return True
        return False

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)
            return True
        return False

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer: Customer = [c for c in self.customers
                              if c.id == customer_id][0]
        dvd: DVD = [d for d in self.dvds if d.id == dvd_id][0]
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least" \
                   f" {dvd.age_restriction} to rent this movie"
        if dvd.is_rented:
            return "DVD is already rented"
        else:
            customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer: Customer = [c for c in self.customers
                              if c.id == customer_id][0]
        dvd: DVD = [d for d in self.dvds if d.id == dvd_id][0]
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        nl = '\n'
        customer_data = nl.join([repr(c).strip() for c in self.customers])  # repr(c) == c.__repr__() !!!!
        dvd_data = nl.join([d.__repr__().strip() for d in self.dvds])
        return customer_data + nl + dvd_data
