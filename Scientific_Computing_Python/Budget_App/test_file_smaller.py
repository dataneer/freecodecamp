
# This is just a development playground

from budget import *

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
actual = food.ledger[0]


food.deposit(45.56)
actual = food.ledger[0]


food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")


food.deposit(900, "deposit")
good_withdraw = food.withdraw(45.67)

food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")


food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
good_transfer = food.transfer(20, entertainment)


food.deposit(10, "deposit")
actual = food.check_funds(20)

food.deposit(100, "deposit")
good_withdraw = food.withdraw(100.10)

food.deposit(100, "deposit")
good_transfer = food.transfer(200, entertainment)


food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)

print(food)
print('-----------------------------------------')
expected = f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
print(expected)
