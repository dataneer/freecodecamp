import copy
import random
from collections import Counter

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

        # A hat will always be created with at least one ball. The arguments
        # passed into the hat object upon creation should be converted to a
        # `contents` instance variable. `contents` should be a list of strings
        # containing one item for each ball in the hat. Each item in the list
        # should be a color name representing a single ball of that color.

        # Append k to self.contents N times based on v
        # use range() to loop N times based on v
        # use items() to access the keys and values in self.balls
        self.contents = [k for k,v in self.balls.items() for i in range(v)]

        # Comment: I think list comprehensions are ugly

    def __repr__(self):
        return f'Balls: {self.balls}'
        # return f'Balls: {self.balls} \n   Contents: {self.contents}'

    # The `Hat` class should have a `draw` method that accepts an argument
    # indicating the number of balls to draw from the hat. This method should
    # remove balls at random from `contents` and return those balls as a list
    # of strings.
    def draw(self,num):
        # Assign an empty list variable of removed balls
        removed_balls = []

        # Store a copy of self.contents here that will always remain
        # the same
        copy_contents = copy.copy(self.contents)

        for i in range(num):
            # print('Draw:', i)
            if len(removed_balls) < 0:
                for i in removed_balls:
                    self.contents.append(i)

            # Assign a random index to rand_index_ball_dict based on a number
            # between 0 and the length of the dictionary minus one (1)
            rand_index_ball_dict = random.randint(0,len(self.balls)-1)

            # Use the dictionary as a fixed point for what balls should be in
            # the balls_list

            # Create a empty single_ball string
            single_ball = ''

            # Enumate the keys of the dictionary

            for i, key in enumerate(self.balls.keys()):
                # Check if the enumrated i matches the random index
                if i == rand_index_ball_dict:
                    # Concatentate the string key to the single_ball string variable
                    single_ball += key

            # Check if the single_ball is in copy_contents AND
            # in self.contents list to ensure that if a ball is not in
            # self.contents this if statement will not run
            if single_ball in copy_contents:

                # Append the single_ball to removed_balls
                removed_balls.append(single_ball)

                # Remove the single_ball from self.contents
                self.contents.remove(single_ball)

            # Else the single_ball is not in self.contents
            else:
                # Use a while loop to infinitely loop over removed_balls until
                # the condition of all the balls removed is satisfied
                while removed_balls.count(single_ball) > 0:
                    self.contents.append(single_ball)
                    removed_balls.remove(single_ball)
            # print(removed_balls)
        print('----New Draw----')
        print('removed_balls:', removed_balls)
        print('self.contents:', self.contents)

        removed_balls = sorted(removed_balls)
        return removed_balls




# Next, create an `experiment` function in `prob_calculator.py` (not inside
# the `Hat` class). This function should accept the following arguments:

# hat`: A hat object containing balls that should be copied inside the
# function

# expected_balls`: An object indicating the exact group of balls to
# attempt to draw from the hat for the experiment. For example, to determine
# the probability of drawing 2 blue balls and 1 red ball from the hat, set
# `expected_balls` to `{"blue":2, "red":1}`.

# `num_balls_drawn`: The number of balls to draw out of the hat in each
# experiment.

# `num_experiments`: The number of experiments to perform. (The more
# experiments performed, the more accurate the approximate probability
# will be.)ls)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # The `experiment` function should return a probability.

    # For example, let's say that you want to determine the probability of
    # getting at least 2 red balls and 1 green ball when you draw 5 balls from
    # a hat containing 6 black, 4 red, and 3 green.

    # To do this, we perform `N` experiments, count how many times `M` we get
    # at least 2 red balls and 1 green ball, and estimate the probability as
    # `M/N`. Each experiment consists of starting with a hat containing the
    # specified balls, drawing a number of balls, and checking if we got the
    # balls we were attempting to draw.
    M = 0
    N = num_experiments

    for i in range(num_experiments):
        # declare a third variable list to store the balls that are drawn
        drawn_balls_list = hat.draw(num_balls_drawn)

        # Convert the drawn_balls_list into a dictionary by counting the
        # frequencies in the list
        drawn_balls_dict = {}
        for i in drawn_balls_list:
            drawn_balls_dict[i] = drawn_balls_list.count(i)

        # Now I didn't know how to compare two dictionaries with base Python 3 code
        # so people smarter than me on the internet suggested I try using
        # Counter from the collections module

        # expected_balls and drawn_balls_dict are both dicts and I want to
        # check if key value pairs of drawn_balls_dict is greater than or equal
        # to the key value pairs of expected_balls

        # First use Counter() to convert both dicts into a collections.Counter object
        expected = Counter(expected_balls)
        observed = Counter(drawn_balls_list)

        # print('expected:', expected)
        # print('observed:', observed)

        # Ok so & is a bitwise operator that compares binary numbers
        # "Sets each bit to 1 if both bits are 1"
        if expected & observed == expected:
            M = M + 1
        else:
            M = M

    probability = M / N

    return probability


# hat = Hat(red=4, green=3)
# probability = experiment(hat=hat,
#                   expected_balls={"red":2,"green":1},
#                   num_balls_drawn=5,
#                   num_experiments=1)

# hat = Hat(red=5,blue=2)
# actual = hat.draw(2)
# len_contents = len(hat.contents)
# print(len_contents)


hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat,
                    expected_balls={"blue":2,"green":1},
                    num_balls_drawn=4,
                    num_experiments=5)
actual = probability
print(actual)
