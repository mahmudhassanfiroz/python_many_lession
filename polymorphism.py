
# Mehtod Overloading
class Animal:
    def sound(self):
        print("Default Sound")

    def sound(self, sound):
        print(sound)

my_animal = Animal()
# my_animal.sound()

my_animal.sound("Meow")
class MathOperations:
    def add(self, a, b, c=0):
        return a+b+c
math_op = MathOperations()
print(math_op.add(5,10))
print(math_op.add(5,10,15))
# Mehtod Overriding
class Animal:
    def sound(self):
        print("Default Sound")

    def sound(self, sound):
        print(sound)

my_animal = Animal()
my_animal.sound("Meow")

# my_animal.sound()

class Animal:
    def sound(self):
        print("Some generic animal sound")
class Dog(Animal):
    # Overriding the parent class method 
    def sound(self):
        print("Bark")
#creating objects
animal = Animal()
dog = Dog()
animal.sound()
dog.sound()