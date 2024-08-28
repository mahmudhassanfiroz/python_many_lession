
""" class myclass:
    def __init__(self, value):
        self.__value = value # Private Attribute
    # Private Method 
    def __display(self):
        print(self.__value)
    def public_display(self):
        self.__display() # Accessing private method internally 

call_myclass = myclass(20)
print(myclass)
print(call_myclass)
print(call_myclass.public_display) 
print(call_myclass.public_display()) 
print(call_myclass.__display) """

""" class Myclass:
    def __init__(self, value):
        self._value = value # protected attribute 
    # protected method 
    def _display(self):
        print(self._value)


call_myclass = Myclass(20)
print(call_myclass._display())
print(call_myclass._value) """

class Myclass:
    def __init__(self, value):
        self.__value = value # Private attribute 
    # Getter Method 
    def get_value(self):
        return self.__value
    # Setter Method 
    def set_value(self, new_value):
        if isinstance(new_value, int):
            self.__value = new_value
        else:
            print("Value must be integer")
# Creating an object
obj = Myclass(10)
# Accessing private attribute 
print(obj.get_value())
# Changing value of private attribute / Modifying value using setter
obj.set_value(20)
# Accessing private attribute after changing value
print(obj.get_value())
# Attempting to set an invalid value
obj.set_value("hello")

    