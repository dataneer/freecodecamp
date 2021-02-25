
# This is a file belonging to internet moniker 'dataneer' as
# I try to solve the freecodecamp arithmetic_arranger project

# Function recives list of strings that are arithmetic problems
# and returns the problems arranged vertically and side-by-side
# Optional second option if 'True' displays answers

# --- Rules ---
# problems are properly formatted, otherwise, it will **return**
# a **string** that describes an error that is meaningful to the user.

# This challenge sort of reminds me of
# https://www.hackerrank.com/challenges/list-comprehensions/problem
# I'll solve this first to get an understanding of how to


def arithmetic_arranger(problems, bool=False):

    # Create empty arranged_problems list.
    arranged_problems = []

    # create three lists for four lines of code
    first = []
    second = []
    third = []
    fourth = []

    arranged_lsts = []

    # split the elements of the list by looping over problems
    for i in problems:
        # split i based on the space symbol
        y = i.split(' ')
        # y returns [#, + ,#]
        # convert and append the first string number at index 0
        first.append(int(y[0]))
        # append the string operand at index 1
        second.append(y[1])
        # convert and append the second string number at index 2
        second.append(int(y[2]))
        x = int(y[0]) + int(y[2])
        fourth.append(x)


    # if option second boolean argument True append first,
    # second, third, fourth to arranged_lsts
    if bool == True:
        arranged_lsts.append(first)
        arranged_lsts.append(second)
        arranged_lsts.append(third)
        arranged_lsts.append(fourth)
    # Else if optional second boolean argument False append first,
    # second, third to arranged_lsts
    else:
        arranged_lsts.append(first)
        arranged_lsts.append(second)
        arranged_lsts.append(fourth)


    # format your lists . . . somehow
