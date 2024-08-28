
# Base Class
class Animal:
    def __init__(self, name):
        self.name = name 
    def sound(self):
        pass # Abstract method to be overridden by subclass 

# Sub Class / Derived Class 
class Dog(Animal):
    def sound(self):
        def sound(self):
            return "Bark"
# Derived class
class Cat(Animal):
    def sound(self):
        return "Meow"
# Creating objects
my_dog = Dog("Bruno")
my_cat = Cat("Kitty")
print(my_dog.name, my_dog.sound(), my_cat.name, my_cat.sound())