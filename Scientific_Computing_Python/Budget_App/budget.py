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
    def deposit(self, amount, description=''):
        self.description = description
        # First make the dictionary with your two variables
        dict = {"amount": amount, "description": description}
        # Append the dictionary to the instance variable list of ledger
        self.ledger.append(dict)

    # A `get_balance` method that returns the current balance of the budget
    # category based on the deposits and withdrawals that have occurred.
    def get_balance(self):
        for i in self.ledger:
            balance = sum(item['amount'] for item in self.ledger)
            return balance

    # A `check_funds` method that accepts an amount as an argument. It
    # returns `False` if the amount is greater than the balance of the budget
    # category and returns `True` otherwise. This method should be used by
    # both the `withdraw` method and `transfer` method.

    # Oh snap this is what I don't get for reading the instrunctions in full
    # because I coded the other methods before doing check_funds, and this was
    # at the bottom of the requirements
    # but this probably replicated the need or change is business demands

    def check_funds(self,amount):
        self.amount = amount
        balance = sum(item['amount'] for item in self.ledger)
        if amount > balance:
            return False
            print('False')
        else:
            return True
            print('True')

    # A `withdraw` method that is similar to the `deposit` method, but the
    # amount passed in should be stored in the ledger as a negative number.
    # If there are not enough funds, nothing should be added to the ledger.
    # This method should return `True` if the withdrawal took place, and
    # False` otherwise.
    def withdraw(self, withdraw_amt, description=''):
        # save the variables entered in the method to reference
        self.description = description
        for i in self.ledger:
            # BIG MOMENT: here I was originally doing just
            # 'check_funds(withdraw_amt)' as a function which is incorrect, it's
            # a method that needs to act upon itself
            if self.check_funds(withdraw_amt):
                # subtract the withdraw at by 0 to get the negative value
                dict = {"amount": 0 - withdraw_amt, "description": description}
                # TODO: I think this is really bad Pythonic fix later
                self.ledger.append(dict)
                return True
            # Else, return True that the user can withdraw successfully
            else:
                # print("Testing: no money")
                return False

    # A `transfer` method that accepts an amount and another budget category
    # as arguments. The method should add a withdrawal with the amount and
    # the description "Transfer to [Destination Budget Category]". The method
    # should then add a deposit to the other budget category with the amount
    # and the description "Transfer from [Source Budget Category]". If there
    # are not enough funds, nothing should be added to either ledgers. This
    # method should return `True` if the transfer took place, and `False`
    # otherwise.

    # This section was really difficult for me because I didn't know
    # how to make the class acknowledge another object instance and get
    # that object instance's name

    # So for a long time I thought it was self.category
    # But that's referencing the category of the object I am using the
    # .transfer method on

    # My breakthrough was understanding I need to use destination.category
    # because I want the category attribute of THAT specific object and
    # destination.category works because destination has the category attribute
    # of category

    # This is really hard to explain no wonder a lot of people struggle

    # I really don't know how I maed this connection but playing around with
    # bankaccount_class.py helped me understand classes a lot

    def transfer(self, trnsfr_amt, destination):
        for i in self.ledger:
            # get the balance of the current object that transfer is being
            # acted upon - sorry I konw there's a correct technical term
            # TODO: find the correct technical term^
            if self.check_funds(trnsfr_amt):
                # this part was really funny because it returned an error
                # because I spelled description as deCsription
                self.withdraw(trnsfr_amt, f"Transfer to {destination.category}")
                dict = {"amount": trnsfr_amt, "description": f"Transfer from {self.category}"}
                # TODO: I think this is really bad Pythonic fix later
                destination.ledger.append(dict)
                return True
                break
            else:
                return False

    """
    When the budget object is printed it should display:
    * A title line of 30 characters where the name of the category is centered
      in a line of `*` characters.
    * A list of the items in the ledger. Each line should show the description
      and amount. The first 23 characters of the description should be
      displayed, then the amount. The amount should be right aligned,
      contain two decimal places, and display a maximum of 7 characters.
    * A line displaying the category total.

    Here is an example of the output:
    ```
    *************Food*************
    initial deposit        1000.00
    groceries               -10.15
    restaurant and more foo -15.89
    Transfer to Clothing    -50.00
    Total: 923.96
    ```
    """

    def getName(self):
        return self.__class__.__name__

    def __repr__(self):
        rep = self.category
        return rep

    def __str__(self):

        # For this section I getting assistance from page 133 of
        # Automate the Boring Stuff by Al Sweigart

        # To accurate we're going to have to remove the values
        # from the ledger and make the decsription the keys assign the values
        # as the new
        # To accomplish this make two seperate lists we can append to
        description =[]
        amount = []

        # Loop over each item the ledger which is a list of dictionaries
        for i in self.ledger:
            # Enumerate just the values so we can index each value
            for index,value in enumerate(i.values()):
                # then based on the mod of the index append to one of our two lists
                if index % 2 != 0:
                    description.append(value)
                else:
                    amount.append(value)

        # Combine the two lists into one dictionary with a dictionary
        # comprehension maybe if I keep writing them I'll fully
        # understand them one day

        total = sum(amount)

        new_dict = {description[i]: amount[i] for i in range(len(description))}

        # Remove the blank string where no description is provided
        # because that's not what the output wants
        new_dict = {k: v for k, v in new_dict.items() if k != ''}
        total_sum = sum(new_dict.values())


        # Store the title of the category with formatting of 30 characters *
        title = str(self.category).center(30, '*')

        output = title + '\n'
        for k,v in new_dict.items():
            output += k[:23].ljust(23, ' ') + "{:.2f}".format(v).rjust(7) + '\n'
        output = output + 'Total: ' + str(total_sum)

        return output

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

def create_spend_chart(x):
    pass
