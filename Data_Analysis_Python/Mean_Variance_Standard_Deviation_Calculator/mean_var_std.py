import numpy as np
from collections import defaultdict
import pprint

"""
Create a function named `calculate()` in `mean_var_std.py` that uses Numpy to
output the mean, variance, standard deviation, max, min, and sum of the rows,
columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function
should convert the list into a 3 x 3 Numpy array, and then return a dictionary
containing the mean, variance, standard deviation, max, min, and sum along both
axes and for the flattened matrix.

The returned dictionary should follow this format:

{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}

If a list containing less than 9 elements is passed into the function, it
should raise a `ValueError` exception with the message: "List must contain
nine numbers." The values in the returned dictionary should be lists and not
Numpy arrays.

For example, `calculate([0,1,2,3,4,5,6,7,8])` should return:
```py
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}

"""

def calculate(list):
    calculations = {}
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        # ---------- Convert list into an array ----------
        list_array = np.array(list, dtype=float)

        # Shape list into a 3 x 3 array
        list_shape = list_array.reshape((3, 3))

        # ---------- Calculate mean ----------
        mean_axis_0 = list_shape.mean(axis=0) # axis=0 = columns
        mean_axis_1 = list_shape.mean(axis=1) # axis=1 is rows
        mean_array = list_shape.mean() # entire array

        # Append the arrays to a list of lists
        mean_list = []

        # array.tolist() returned array as a (possibly nested) list
        mean_list.append(mean_axis_0.tolist())
        mean_list.append(mean_axis_1.tolist())
        mean_list.append(mean_array.tolist())

        # Create a dictionary of the means with 'mean' as the key value
        mean_dict = {'mean': mean_list}

        # The update() method updates the dictionary with the elements from
        # the another dictionary object or from an iterable of key/value pairs
        calculations.update(mean_dict)

        # ---------- Calculate variance ----------
        var_axis_0 = list_shape.var(axis=0)
        var_axis_1 = list_shape.var(axis=1)
        var_array = list_shape.var()

        # Append the arrays to a list of lists
        var_list = []

        # array.tolist() returned array as a (possibly nested) list
        var_list.append(var_axis_0.tolist())
        var_list.append(var_axis_1.tolist())
        var_list.append(var_array.tolist())

        # Create a dictionary of the variances with 'variance' as the key value
        var_dict = {'variance': var_list}

        # The update() method updates the dictionary with the elements from
        # the another dictionary object or from an iterable of key/value pairs
        calculations.update(var_dict)

        # ---------- Calculate standard deviation ----------
        std_axis_0 = list_shape.std(axis=0)
        std_axis_1 = list_shape.std(axis=1)
        std_array = list_shape.std()

        # Append the arrays to a list of lists
        std_list = []

        # array.tolist() returned array as a (possibly nested) list
        std_list.append(std_axis_0.tolist())
        std_list.append(std_axis_1.tolist())
        std_list.append(std_array.tolist())

        # Create a dictionary of the standard deviations
        # with 'standard deviation' as the key value
        std_dict = {'standard deviation': std_list}

        # The update() method updates the dictionary with the elements from
        # the another dictionary object or from an iterable of key/value pairs
        calculations.update(std_dict)

        # ---------- Calculate max ----------

        # for the next three sections convert the numpy array from float to int
        list_shape_int = list_shape.astype(int)

        max_axis_0 = list_shape_int.max(axis=0)
        max_axis_1 = list_shape_int.max(axis=1)
        max_array = list_shape_int.max()

        # Append the arrays to a list of lists
        max_list = []

        # array.tolist() returned array as a (possibly nested) list
        max_list.append(max_axis_0.tolist())
        max_list.append(max_axis_1.tolist())
        max_list.append(max_array.tolist())

        # Create a dictionary of the max with 'max' as the key value
        max_dict = {'max': max_list}

        # The update() method updates the dictionary with the elements from
        # the another dictionary object or from an iterable of key/value pairs
        calculations.update(max_dict)

        # ---------- Calculate min ----------
        min_axis_0 = list_shape_int.min(axis=0)
        min_axis_1 = list_shape_int.min(axis=1)
        min_array = list_shape_int.min()

        # Append the arrays to a list of lists
        min_list = []

        # array.tolist() returned array as a (possibly nested) list
        min_list.append(min_axis_0.tolist())
        min_list.append(min_axis_1.tolist())
        min_list.append(min_array.tolist())

        # Create a dictionary of the min with 'min' as the key value
        min_dict = {'min': min_list}

        # The update() method updates the dictionary with the elements from
        # the another dictionary object or from an iterable of key/value pairs
        calculations.update(min_dict)

        # ---------- Calculate sum ----------
        sum_axis_0 = list_shape_int.sum(axis=0)
        sum_axis_1 = list_shape_int.sum(axis=1)
        sum_array = list_shape_int.sum()

        # Append the arrays to a list of lists
        sum_list = []

        # array.tolist() returned array as a (possibly nested) list
        sum_list.append(sum_axis_0.tolist())
        sum_list.append(sum_axis_1.tolist())
        sum_list.append(sum_array.tolist())

        # Create a dictionary of the min with 'min' as the key value
        sum_dict = {'sum': sum_list}

        # The update() method updates the dictionary with the elements from
        # the another dictionary object or from an iterable of key/value pairs
        calculations.update(sum_dict)


    return calculations

# pprint.pprint((calculate([2,6,2,8,4,0,1,5,7])), sort_dicts=False)
