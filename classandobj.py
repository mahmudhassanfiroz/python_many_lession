""" 
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year 
    
    def display_info(self):
        print(f"Car: {self.make} {self.model}, Year: {self.year}")
# Create an object of the car class
my_car = Car("Toyota", "Corolla", 2020)
# Access object's attributs
print(my_car)
# Call object's method 
my_car.display_info()
 """
class car:
    # class attribute
    wheels = 4
    
    # Instance Method
    def __init__(self, make, model):
        # instance attributes
        self.make = make
        self.model = model
    # Class Method 
    @classmethod
    def change_wheels(cls, new_wheel_count):
        cls.wheels = new_wheel_count
""" # Create objects
car1 = car("Toyota", "Corolla")
car2 = car("Honda", "Civic")
# Accessing Instance Attribute
print(car1.make, car2.model)
# Accessing Class Attribute
print(car1.wheels, car2.wheels, car.wheels)
# Calling class mehtod 
car.change_wheels(6)
print(car1.wheels, car2.wheels, car.wheels) """
class person:
    def __inti__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)