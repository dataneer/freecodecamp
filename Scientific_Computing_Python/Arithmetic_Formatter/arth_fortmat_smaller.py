
# Environment to play with smaller pieces of code so I can carry those
# concepts to the arithmetic_arranger.py file

"""
Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
"""



# Function to cnvert a list to string using join() function
def listToString(s):

    # initialize an empty string with four spaces to divide the 'columns'
    # of the problems by four spaces because that is what the output wants
    str1 = "    "

    # return string
    return (str1.join(s))

def arithmetic_arranger(problems,input=False):

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    arranged_problems = []

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for i in problems:
        # Split the entered problem into a list of three element
        x = i.split(" ")
        # Split those elements to give them variable names
        first_num = x[0]
        operand = x[1]
        second_num = x[2]

        # Check if operand is addition or subtraction
        if operand == '+' or operand == '-':
            # Check that both first_num and second_num are digits
            if first_num.isdigit() and second_num.isdigit():
                # Check if length of first_num and second_num are four or less
                if len(first_num) <= 4 and len(second_num) <= 4:
                    # Obtain the longest number - https://tinyurl.com/f9jb9w9s based on
                    # whether one is larger than the other
                    if len(first_num) < len(second_num):
                        # In this section the second_num is bigger than the first_num
                        # . . .
                        # Assign operand and second_num together with a single
                        # whitespace
                        op_second = operand + ' ' + second_num
                        # Calculate the length of the second_num appended w/ operand
                        # and add that much whitespace to the first_num
                        first_num = first_num.rjust(len(op_second))
                        # Assign an empty dashes string
                        dashes = ''
                        # Based on length of op_second we can add a number of dashes
                        # https://www.geeksforgeeks.org/python-append-k-character-n-times/
                        dashes = dashes.ljust(len(op_second),'-')
                    else:
                        # In this secion the first_num is bigger than the second_num
                        # or
                        # both numbers are the same length
                        # .. .
                        # Calculate how much whitespace should be between the operand and
                        # second number based on the length of the first number
                        # Always at least add 1 because there should at least be 1 space
                        # between the two
                        whitespace_counter = len(first_num) - len(second_num) + 1
                        # Add the length of the first number to the whitespace_counter
                        string_length = len(second_num) + whitespace_counter
                        # Assign the operand and second_num to one variable
                        op_second = operand + second_num.rjust(string_length," ")
                        # based on the length of op_second add that much whitespace
                        # to the first_num
                        first_num = first_num.rjust(len(op_second))
                        # Assign an empty dashes string
                        dashes = ''
                        # Based on length of op_second we can add a number of dashes
                        # https://www.geeksforgeeks.org/python-append-k-character-n-times/
                        dashes = dashes.ljust(len(op_second),'-')

                    # Append first_num to first_line
                    first_line.append(first_num)
                    # Append op_second to second_line
                    second_line.append(op_second)
                    # Append dashes to third_line
                    third_line.append(dashes)

                    if input == True:
                        if operand == '+':
                            calculated_answer = int(first_num) + int(second_num)
                        elif operand == '-':
                            calculated_answer = int(first_num) - int(second_num)
                        # Now we use the length of op_second to add leading whitespace with
                        # .rjust() method to the calculated_answer
                        calculated_answer = str(calculated_answer).rjust(len(op_second)," ")
                        # append formatted calculated_answer to fourth_line
                        fourth_line.append(calculated_answer)
                else:
                    return "Error: Numbers cannot be more than four digits."
            else:
                return "Error: Numbers must only contain digits."
        else:
            return "Error: Operator must be '+' or '-'."



    # Put this block of code in an if statement that checks if first_line has
    # content in it meaning the code ran successfully past the error checks
    if len(first_line) > 0:
        # convert everything to a string first
        first_line = listToString(first_line)
        second_line = listToString(second_line)
        third_line = listToString(third_line)

        if input == True:
            # convert fourth_line under the True conditional to save memory
            fourth_line = listToString(fourth_line)
            # If the user makes optional argument of input to True then
            # concatinate the four strings into a single list
            arranged_problems += [first_line, second_line, third_line, fourth_line]
            # Append that list with a newline using .join() method
            arranged_problems = '\n'.join(arranged_problems)
        else:
            # concatinate only the three strings into a single list
            arranged_problems += [first_line, second_line, third_line]
            # Append that list with a newline using .join() method
            arranged_problems = '\n'.join(arranged_problems)


    return arranged_problems


    """
    Edit: it appears the following code doesn't give the ouput of newlines
    that freeCodeCamp wants but I still like what I learned from it

    # Now we gotta format arranged_problems using code I stole from the
    # internet
    # Stack Overflow Question: https://tinyurl.com/yxtyf6rx
    # by Patrick Artner

    # I'm going to try to understand this code instead of copy it

    # Transpose the lists of list arranged_problems, get the max of each
    # column and store in as dict[column]=length

    # The following is a Nested List Comprehension
    # and I don't even 100% understand a single List Comprehension so let's goo

    # It appears nest list comps are best to operate on multidimensional arrays
    # because it acts on each dimension of the matrix
    col_len = {i:max(map(len,inner)) for i,inner in enumerate(zip(*arranged_problems))}

    # Print(col_len) gives an example: {0: 6, 1: 6, 2: 3, 3: 4}

    # Print using the column index from enumerate to lookup this columns length
    for inner in arranged_problems:
        # I'm going to try to understand this code instead of copy it

        #
        for col,word in enumerate(inner):
            print(f"{word:{col_len[col]}}",end="    ")
        print()

    """

# x = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
y = arithmetic_arranger(["3 - 698", "3801 - 2", "45 + 43", "123 + 49"], True)
print(y)



"""
# -------- FIGURE OUT STUFF


a = [['a', 'b', 'c'], ['aaaaaaaaaa', 'b', 'c'], ['a', 'b', 'c']]


data = [['FirstFirst', 'FirstSecond', 'FirstThird'],
        ['SecondFirst', 'SecondSecond', 'SecondThird'],
        ['ThirdFirst', 'ThirdSecond', 'ThirdThird'],
        ['foo', 'verylongwordinsidehere', 'bar', ]]    # changed to a longer one

data = [['1','11111111111','1'],
       ['+ 1', '+ 2'.rjust(10),'+ 1'],
       ['---','-----','---']]

# transpose the list, get the max of each column and store in
# as dict[column]=length

col_len = {i:max(map(len,inner)) for i,inner in enumerate(zip(*data))}

# print(col_len) # {0: 11, 1: 22, 2: 11}

# print using the column index from enumerate to lookup this columns lenght
for inner in data:
    for col,word in enumerate(inner):
        print(f"{word:{col_len[col]}}",end=" | ")
    print()
"""








# ...
