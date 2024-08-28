
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass # Abstract method no implementation
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat (Animal):
    def sound(self):
        return "Meow"
# Creating objects
dog = Dog()
cat = Cat()
print(dog.sound(), cat.sound())