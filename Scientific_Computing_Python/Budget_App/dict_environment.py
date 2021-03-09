
# I need this playground area to replace a dictionary key value on a small
# scale

from collections import defaultdict

# ASSIGN A NEW VALUE TO AN EXISTING KEY TO CHANGE THE VALUE
# Use the format dict[key] = value to assign a new value to an existing key.

a_dictionary = {"a": 1, "b": 2}

a_dictionary["b"] = 3

# USE dict.update() TO CHANGE MULTIPLE VALUES IN A DICTIONARY
# Call dict.update(other) using a collection of key: value pairs as other
# to update the values of the dictionary.

b_dictionary = {"a": 1, "b": 2}

b_dictionary.update({"a": 3, "b": 4})

# However, in budget.py it's a list of a dictionary

# * A `deposit` method that accepts an amount and description. If no description
#   is given, it should default to an empty string. The method should append an
#   object to the ledger list in the form of
#   `{"amount": amount, "description": description}`.

ledger = [
            {"amount": 1, "description": 'aaa'},
            {"amount": 22, "description": 'bbb'},
            {"amount": 333, "description": 4}
            ]

print(ledger)
