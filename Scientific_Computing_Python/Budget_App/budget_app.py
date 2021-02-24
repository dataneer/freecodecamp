"""

Complete the `Category` class in `budget.py`. It should be able to instantiate
objects based on different budget categories like *food*, *clothing*, and
*entertainment*. When objects are created, they are passed in the name of
the category. The class should have an instance variable called `ledger`
that is a list. The class should also contain the following methods:

    *   A `deposit` method that accepts an amount and description. If no
        description is given, it should default to an empty string. The
        method should append an object to the ledger list in the form of
        `{"amount": amount, "description": description}`.
    *   A `withdraw` method that is similar to the `deposit` method, but the
        amount passed in should be stored in the ledger as a negative number.
        If there are not enough funds, nothing should be added to the ledger.
        This method should return `True` if the withdrawal took place, and
        False` otherwise.
    *   A `get_balance` method that returns the current balance of the budget
        category based on the deposits and withdrawals that have occurred.
    *   A `transfer` method that accepts an amount and another budget category
        as arguments. The method should add a withdrawal with the amount and
        the description "Transfer to [Destination Budget Category]". The method
        should then add a deposit to the other budget category with the amount
        and the description "Transfer from [Source Budget Category]". If there
        are not enough funds, nothing should be added to either ledgers. This
        method should return `True` if the transfer took place, and `False`
        otherwise.
    *   A `check_funds` method that accepts an amount as an argument. It
        returns `False` if the amount is greater than the balance of the budget
        category and returns `True` otherwise. This method should be used by
        both the `withdraw` method and `transfer` method.

When the budget object is printed it should display:

    *   A title line of 30 characters where the name of the category is
        centered in a line of `*` characters.
    *   A list of the items in the ledger. Each line should show the
        description and amount. The first 23 characters of the description
        should be displayed, then the amount. The amount should be right
        aligned, contain two decimal places, and display a maximum of 7
        characters.
    *   A line displaying the category total.

Here is an example of the output:

    *************Food*************
    initial deposit        1000.00
    groceries               -10.15
    restaurant and more foo -15.89
    Transfer to Clothing    -50.00
    Total: 923.96

"""

# Ugh already stress about this one because I truly don't understand classes
# that well yet but I know they're like a template for a objects

# RealPython:
# Classes are used to create user-defined data structures
# Classes define functions called methods, which identify the behaviors and
# actions that an object created from the class can perform with its data

# It's a blueprint, an **instance** is an object that is built from a class
# and contains real data. An instance of the Dog class is not a blueprint
# anymore but an actual dog with a name, age, etc

class Category:

    def __init__(self,category):
        self.category = category
        # The class should have an instance variable called `ledger` that is a
        # list.
        self.ledger = []

    # A `deposit` method that accepts an amount and description. If no
    # description is given, it should default to an empty string. The method
    # should append an object to the ledger list in the form of
    # `{"amount": amount, "description": description}`.
    def deposit(self, deposit_amt, description):
        self.deposit_amt = deposit_amt
        self.description = description
        # First make the dictionary with your two variables
        dict = {"amount": deposit_amt, "description": description}
        # Append the dictionary to the instance variable list of ledger
        self.ledger.append(dict)

    # A `withdraw` method that is similar to the `deposit` method, but the
    # amount passed in should be stored in the ledger as a negative number.
    # If there are not enough funds, nothing should be added to the ledger.
    # This method should return `True` if the withdrawal took place, and
    # False` otherwise.
    def withdraw(self, withdraw_amt, description):
        self.withdraw_amt = withdraw_amt
        self.description = description
        # If the withdraw amt is greater than the deposit amt then returns
        # False
        if self.withdraw_amt < self.deposit_amt:
            dict = {"amount": 1 - withdraw_amt, "description": description}
            self.ledger.append(dict)
            return True
        # Else, return True that the user can withdraw successfully
        else:
            return False

    # A `get_balance` method that returns the current balance of the budget
    # category based on the deposits and withdrawals that have occurred.
    def get_balance(self):
        for i in self.ledger:
            balance = sum(item['amount'] for item in self.ledger)
        return balance

    # A `transfer` method that accepts an amount and another budget category
    # as arguments. The method should add a withdrawal with the amount and
    # the description "Transfer to [Destination Budget Category]". The method
    # should then add a deposit to the other budget category with the amount
    # and the description "Transfer from [Source Budget Category]". If there
    # are not enough funds, nothing should be added to either ledgers. This
    # method should return `True` if the transfer took place, and `False`
    # otherwise.

    def transfer(self, amount, description):
        self.amount = amount
        description = description
        # The method should add a withdrawal with the amount and
        # the description "Transfer to [Destination Budget Category]"
        # Wtf does this mean
        print(f"Transfer to {self.description}")



"""
Besides the `Category` class, create a function (outside of the class) called
`create_spend_chart` that takes a list of categories as an argument. It should
return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the
function. The percentage spent should be calculated only with withdrawals and
not with deposits. Down the left side of the chart should be labels 0 - 100.
 "bars" in the bar chart should be made out of the "o" character. The height
 of each bar should be rounded down to the nearest 10. The horizontal line
 below the bars should go two spaces past the final bar. Each category name
 should be written vertically below the bar. There should be a title at the
 top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the
output matches the example exactly.
"""


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)


def Account(self, name):
    self.name = name

    def deposit(self, amt, description):
        self.amt = amt
        self.description = description

    def transfer(self, amt, name):
        self.amt = amt
        self.name = names
        # self.decsription only prints the object gibberish by the way
        print(f"Transfer to {self.description}")
        # . . . ??? ? I don´t know how else to proceed from here

account_a = Account("Account A")
account_a.deposit(500,"Starting balance")
account_b = Account("Account B")
account_a.transfer(100, account_b)
