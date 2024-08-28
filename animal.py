
from abc import ABC , abstractmethod 
class Animal(ABC):
    def __init__(self, name):
        self.name = name 
    @abstractmethod
    def sound(self):
        pass
    def sleep(self):
        return f"{self.name} is sleeping"
class Dog(Animal):
    def make_sound(self):
        return "Noof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
# Usage
# my_dog = Dog("Bruno")
# my_cat = Cat("Kitty")
my_dog = Dog("Buddy")
# print(my_dog.name, my_dog.make_sound(), my_cat.name, my_cat.make_sound(), my_cat.sleep())
print(my_dog.make_sound())
print(my_dog.sleep())
my_cat = Cat("Whiskers")
print(my_cat.make_sound())
print(my_cat.sleep())