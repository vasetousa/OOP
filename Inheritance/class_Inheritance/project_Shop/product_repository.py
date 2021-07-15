from Encapsulation.project_wild_cat_zoo import Product


class ProductRepository:
    products: list

    def __init__(self):
        self.products = []

    def add(self, prd: Product):
        self.products.append(prd)

    def find(self, product: str):
        for prod in self.products:
            if prod.name == product:
                return prod

    def remove(self, product_name: str):
        for indx, pr in enumerate(self.products):
            if pr.name == product_name:
                self.products.pop(indx)
                return

    def __repr__(self):
        string = []
        nr = "\n"
        for el in self.products:
            string.append(str(el))

        return nr.join(string)