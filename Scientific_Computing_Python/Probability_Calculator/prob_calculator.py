import copy
import random
# Consider using the modules imported above.

# First, create a `Hat` class in `prob_calculator.py`. The class should
# take a variable number of arguments that specify the number of balls
# of each color that are in the hat. For example, a class object could
# be created in any of these ways:

# hat1 = Hat(yellow=3, blue=2, green=6)
# hat2 = Hat(red=5, orange=4)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

class Hat:

    # Originally here I used an *args before I discovered **kwargs so
    # I am going to write the differences betweent the two here for my future
    # reference

    # *args is used to pass non-key worded, variable-length arguments
    # You can take in more arguments than the # of formal arguments that you
    # previously defined with. Any extra arguements can be tacked onto your
    # current formal paramaters (including zero extra arguments)

    # **kwargs is used to pass keyworded, variable-length arguments
    # One can thnk of wards being a dictionary that maps each keyword to the
    # value that we pass alongside it. That's why when we iterate over the
    # kwargs there doesn't seem to beany order in which they were printed out

    # args: ('geeks', 'for', 'geeks')
    # kwargs {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}
    def __init__(self,**balls):
        self.balls = balls

    def __repr__(self):
        return f'Balls: {self.balls}'

    # `expected_balls`: An object indicating the exact group of balls to
    # attempt to draw from the hat for the experiment. For example, to determine
    # the probability of drawing 2 blue balls and 1 red ball from the hat, set
    # `expected_balls` to `{"blue":2, "red":1}`.

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

hat1 = Hat(yellow=3, blue=2, green=6)
print(hat1)
