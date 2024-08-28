
class person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age 
        self.money = money
        
    def __add__(self, other):
        return self.money + other.money 
    

alim = person('Alim', 15, 500)
dalim = person('Dalim', 16, 600)
# print(alim + dalim)
# print(type(alim))
# print(alim + dalim)
