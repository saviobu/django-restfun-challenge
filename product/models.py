class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Drink(Product):
    def __init__(self, name, price, option):
        super().__init__(name, price)
        self.option = option

class Food(Product):
    def __init__(self, name, price, option):
        super().__init__(name, price)
        self.option = option
        
class Tea(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.name = 'Tea'

class InstantiateAll:
    def __call__(self):

        products = [{ "name":"Latte", "option": "Milk skim", "price": "10.00" },{ "name":"Latte", "option": "Milk semi", "price": "12.00" },
{ "name":"Latte", "option": "Milk whole", "price": "15.00" },{ "name":"Cappuccino", "option": "small", "price": "5.00" },
{ "name":"Cappuccino", "option": "medium", "price": "7.00" },{ "name":"Cappuccino", "option": "large", "price": "9.00" },
{ "name":"Espresso", "option": "single", "price": "7.50" },{ "name":"Espresso", "option": "double", "price": "8.50" },
{ "name":"Espresso", "option": "triple", "price": "9.50" },{ "name":"Tea", "option": "", "price": "5.00" },
{ "name":"Hot chocolate", "option": "small", "price": "3.00" },{ "name":"Hot chocolate", "option": "medium", "price": "4.20" },
{ "name":"Hot chocolate", "option": "large", "price": "5.80" },{ "name":"Cookie", "option": "chocolate chip", "price": "1.80" },
{ "name":"Cookie", "option": "ginger", "price": "2.50" }]
       
        objects = list()
        for product in products:
            objectproduct=None

            if product['name'] =='Tea':
                objectproduct = Tea('',product['price'])
            elif product['name'] =='Cookie':
                objectproduct = Food(product['name'],product['price'],product['option'])
            else:
                objectproduct = Drink(product['name'],product['price'],product['option'])
            objects.append(objectproduct)
        return objects           