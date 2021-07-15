
from Encapsulation.project_wild_cat_zoo import Food
from Encapsulation.project_wild_cat_zoo import Drink
from Encapsulation.project_wild_cat_zoo import ProductRepository


pr = ProductRepository()

pizza = Food('pizza')
beer = Drink('beer')

pizza.increase(1)
beer.decrease(2)

pr.add(beer)
pr.add(pizza)

print('-'*8)

print(pr)
pr.remove('pizza')

print('-'*8)

print(pr)