
"""

Why is this here?

I'm having an issue where I don't know how to make the class manipulate
a object it created because my code just references itself.

Thus, this are is where I am going to make two bank accounts, with balances
and transfer those balances succesfully.

Thus, maybe I can apply the concepts I learn here to transfering the category
balances which are stored in dictionaries in budget_app.py

This is a lesson from http://www.alan-g.me.uk/tutor/tutclass.htm

"""

# Create a class the throws an error for testing or if balance invalid
class BalanceError(Exception):
    value = "Sorry you only have $%6.2f in your account"

class BankAccount:

    # initize the bank account and require it have a starting balance attribute
    def __init__(self, initialAmount):
        self.balance = initialAmount
       print(f"Account created with balance {self.balance}")
