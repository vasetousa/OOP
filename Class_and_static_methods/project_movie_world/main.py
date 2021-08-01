from Class_and_static_methods.project_movie_world.customer import Customer
from Class_and_static_methods.project_movie_world.dvd import DVD
from Class_and_static_methods.project_movie_world.movie_world import MovieWorld

c2 = Customer("Anna", 55, 2)
c3 = Customer("Pesho", 18, 1)

d2 = DVD("A", 2, 1254, "February", 5)
d1 = DVD("Black Widow", 3, 2020, "April", 3)

movie_world = MovieWorld("The Best Movie Shop")


movie_world.add_customer(c2)
movie_world.add_customer(c3)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 2))   # Pesho
print(movie_world.rent_dvd(2, 3))   # Pesho
print(movie_world.rent_dvd(1, 3))   # Anna
print(movie_world.return_dvd(1, 2)) # Pesho
print(movie_world.return_dvd(1, 2)) # Pesho


print(movie_world)