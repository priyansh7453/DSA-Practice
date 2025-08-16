# Encapsulation Example
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private attribute

    # Public method to get balance
    def get_balance(self):
        return self.__balance
    
    # Public method to deposit money with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount!")
    
    # Public method to withdraw money with validation
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid or insufficient funds.")
            
# Usage
account = BankAccount(1000)
print(account.get_balance())  # Output: 1000
account.deposit(500)           # Output: Deposited: 500
print(account.get_balance())  # Output: 1500
account.withdraw(2000)         # Output: Invalid or insufficient funds.
# Direct access to __balance will fail
# print(account.__balance)  # Raises AttributeError: 'BankAccount' object has no attribute '__