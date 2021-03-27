import random
import itertools
from collections import Counter

{'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}

balls_dict = {'black': 3, 'green': 2, 'red': 2}
balls_list = ['black', 'black', 'black', 'green', 'green', 'red', 'red']

removed_balls = []

"""
The `Hat` class should have a `draw` method that accepts an argument
indicating the number of balls to draw from the hat. This method should
remove balls at random from `contents` and return those balls as a list
of strings. The balls should not go back into the hat during the draw,
similar to an urn experiment without replacement.

If the number of balls to draw exceeds the available quantity,
return all the balls.
"""

def draw(num):
    # Use the dictionary as a fixed point for what balls should be in
    # the balls_list

    # Get the key black

    # Create a empty ball string
    ball = ''
    # enumerate the keys of the dictionary
    for i, key in enumerate(balls_dict.keys()):
        # 'black' is on index 0
        if i == 0:
            ball += key

    for i in range(num):
        print('Draw a ball:', i)
        if ball in balls_list:
            # print('Remove')
            removed_balls.append(ball)
            balls_list.remove(ball)
        else:
            # Infinitely loop ove removed balls until the count of ball
            # is 0
            while removed_balls.count(ball) != 0:
                # print('Count of ball:', removed_balls.count(ball))
                # print(i)
                removed_balls.remove(ball)
                balls_list.append(ball)
                # print('Replace')

"""
expected_balls={"A": 2,"B": 1}
collected_balls = {'A': 3, 'B': 1, 'C': 2}

expected = Counter(expected_balls)
observed_1 = Counter(collected_balls)

if expected & observed_1 == expected:
    print(True)
else:
    print(False)

"""
