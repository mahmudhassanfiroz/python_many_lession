
# Base Class
class Vehicle:
    def __init__(self, make, model):
        self.make = make 
        self.model = model 
    def start_engine(self):
        # print("Start engine")
        return "Engine Started"
    def stop_engine(self):
        return "Engine Stopped"
# Derived Class 
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors 
    def start_engine(self):
        return f"Car engine started: {self.make} {self.model}"
    def get_doors(self):
        return f"Number of doors: {self.num_doors}"

# Derived Class
class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar
    def start_engine(self):
        return f"Motorcycle engine started: {self.make} {self.model}"
    def has_sidecar_info(self):
        return "Has sidecar" if self.has_sidecar else "No sidecar"
# Usage 
my_car = Car("Toyota", "Camry", 4)
print(my_car.start_engine())
print(my_car.get_doors())
my_motorcycle = Motorcycle("Harley", "Sportster", True)
print(my_motorcycle.start_engine())
print(my_motorcycle.has_sidecar_info())