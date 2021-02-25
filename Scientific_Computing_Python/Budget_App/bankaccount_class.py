
"""

Why is this here?

I'm having an issue where I don't know how to make the class manipulate
a object it created because my code just references itself.

Thus, this are is where I am going to make two bank accounts, with balances
and transfer those balances succesfully.

Thus, maybe I can apply the concepts I learn here to transfering the category
balances which are stored in dictionaries in budget_app.py

This is a lesson from http://www.alan-g.me.uk/tutor/tutclass.html
However ^this is in Python 2 so I have to do slight edits to get it to
work in Python 3

"""

import argparse

# Create a class the throws an error for testing or if balance invalid
class BalanceError(Exception):
    value = "Sorry you do not have enough balance in your account"

class BankAccount:

    # initize the bank account and require it have a starting balance attribute
    def __init__(self, initialAmount):
        self.balance = initialAmount
        print(f"Account created with balance {self.balance}")

    # this lesson really illuminated to me that I didn't need to set a
    # self.amount attribute in the budget_app.py because setting it as a fixed
    # value messed with the other methods/functions
    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print(BalanceError.value)

    def checkBalance(self):
        return self.balance

    # Inherit the withdraw method and deposit method
    def transfer(self, amount, account):
        if self.balance >= amount:
            self.withdraw(amount)
            account.deposit(amount)
            # this next part of code confirmed for me that I can at least
            # enter an object name and ths function can act upon it
            print("transfer to", account)
        else:
            print(BalanceError.value)

a = BankAccount(500)
b = BankAccount(200)

a.transfer(100,b)

print("Bank Account A:", a.checkBalance())
print("Bank Account B", b.checkBalance())
print("--------------------------")

c = BankAccount(500)
d = BankAccount(200)


c.transfer(500,d)

print("Bank Account C:", c.checkBalance())
print("Bank Account D", d.checkBalance())
