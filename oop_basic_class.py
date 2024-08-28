
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
    
    def display_info(self):
        print(f"Car: {self.make} {self.model}, Year: {self.year}")
my_car = Car("Toyota", "Corolla", 2020)
#my_car.display_info() # Object mehtod 
#print(my_car.make) # Object's attributs
class Phone:
    name = "Samsung"
    color = 'Black'
    price = 25000

my_phone = Phone()
# print(my_phone)
# print(my_phone.name, my_phone.color, my_phone.price)
class Shop:
    cart = []
    def __init__(self, buyer):
        self.buyer = buyer 
    
    def add_to_cart(self, item):
        self.cart.append(item)

Shoper_1 = Shop('Alu Khan')
Shoper_1.add_to_cart('Laptop')
print(Shoper_1.cart)
Shoper_2 = Shop('Chanachur Khan')
Shoper_2.add_to_cart('Mobile')
print(Shoper_2.cart)
