
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount} New balance: {self.__balance}"
        return "Deposit amount must be positive"
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdraw {amount}. New balance: {self.__balance}"
        return "Insufficient funds or invalid amount"
    def get_balance(self):
        return f"Current balance: {self.__balance}"
    def get_account_holder(self):
        return self.__account_holder
    def get_account_number(self):
        return self.__account_number
# Usage 
my_account = BankAccount("123456", "John Smith", 1000)
print(my_account.deposit(500))
print(my_account.withdraw(200))
print(my_account.get_balance())