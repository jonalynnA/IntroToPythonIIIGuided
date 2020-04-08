'''
A store can have multiple departments. A department can hold multiple products. 
The store has a name. Departments have names. Products have names and prices.

Nouns tend to be classes
If a noun"has" something, that something tends to be an attribute.
Verbs tend to be methods.

'''


class Store:
    """ Holds info about a Store aka documentation string"""

    def __init__(self, name, departments=None):
        """ Construct a new Store"""
        self.name = name
        self.departments = []

        if departments is None:
            self.departments = []
        else:
            self.departments = departments


class Departments:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_products(self, product):
        self.products.append(product)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


soccer_ball = Product("Soccer Ball", 14.99)

sporting_goods = Departments("Sporting Goods")

# sporting_goods.products.append(soccer_ball)
# if you don't have a method "add_product" use ^^^ but its ugly

sporting_goods.add_products(soccer_ball)
# if you have a method "add_product" use ^^

