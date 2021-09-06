import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
-----------------
--- Refresher ---
-----------------

This part is a refresher so I can understand the new libaries freeCodeCamp
asks I use for this project.

--- NumPy ---

Created in 2005 by Travis Oliphant, it is an open source project used for
working with arrays. Its functions are for working in the domain of linear
algebra, fourior transform, and matrices.

The basis is that Python's base data structures like lists require a lot of
memory. One (1) integer in stored in a Python variable is 28 bytes.

>>> sys.getsizeof(1)
>>> 28

Versus through NumPy the size of the integer is less.

>>> np.dtype(np.int8).itemsize

This is crucial for performance. NumPy allows higher level mathematical
calculations to be evaluated on larger datasets for less resources.

--- Pandas ---

Pandas is a popular Python package for data science and with good reason: it
offers powerful, expressive and flexible data structures that make data
manipulation and analysis easy, among many other things.

Dataframes are the same ((as far as I know)) as data frames in R. Storing data
in retangular grids that can easily be overviewed. Each row of these corresponds
to measurements for values of an instance, while each column is a vector
containing data for a specific variable. This means that a data frame's rows
do not need to contain, but can contain, the same type of values: numeric,
character, logical, etc.

Dataframes are defined as two-dimensional labeled data structures with columns
of potentially different types. Generally, dataframes can be thought to have
three main components: the data, the index, and the columns.

1. The DataFrame can contain data that is:

    * a Pandas Dataframe
    * a Pandas Series: a one-dimensional labeled array capable of holding any
      data type with axis labels or index. An example of a Series object is one
      column from a DataFrame.
    * a NumPy ndarray, which can be a record or structured
    * a two-dimensional ndarray
    * dictionaries of one-dimensional ndarray's, lists, dictionaries, or Series

**Note** the difference between np.ndarray and np.array(). The former is an
actual data type, while the latter is a function to make arrays from other
data structures.

2. Besides data, you can also specify the index and column names for your
DataFrame. The index, on the one hand, indicates the difference in rows, while
the column names indicate the difference in columns. You will see later that
these two components of the DataFrame will come in handy when you´re manipulating
data.

*** Should I use pandas or NumPy? ***

Numpy is memory efficient. Pandas has a better performance when number of rows
is 500K or more. Numpy has a better performance when number of rows is 50K or
less. Indexing of the pandas series is very slow as compared to numpy arrays.

- https://www.geeksforgeeks.org/difference-between-pandas-vs-numpy/

--- matplotlib ---

Matplotlib is a comprehensive library for creating static, animated, and
interactive visualizations in Python.

Matplotlib produces publication-quality figures in a variety of hardcopy formats
and interactive environments across platforms. Matplotlib can be used in Python
scripts, the Python and IPython shell, web application services, and various
graphical user interface toolkits.


"Matplotlib does not, in fact, make any sense. Maybe someday we'll have a
charting library written by actual programmers."
- https://www.reddit.com/r/learnpython/comments/c3ut7p/does_matplotlib_ever_actually_make_sense_or_do/

However reddit appears to hate matplotlib.

--- seaborn ---

Seaborn is a Python data visualization library based on matplotlib. It provides
a high-level interface for drawing attractive and informative statistical
graphics.

"""

# Import data
# >>> df.size
# >>> 910000
# File >500k means Pandas is absolutely appropriate
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
# To determine if a person is overweight, first calculate their BMI by
# dividing their weight in kilograms by the square of their height in meters.
# If that value is > 25 then the person is overweight. Use the value 0 for NOT
# overweight and the value 1 for overweight.
# --- Programmer notes ---
# Multiply height by 0.01 to convert to meters

df['overweight']=[0 if i > 25 else 1 for i in df["weight"]/(df["height"]*.01)**2]

# Normalize data by making 0 always good and 1 always bad. If the value of
# 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more
# than 1, make the value 1.

df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

print(df.head(10))

# Convert the data into long format and create a chart that shows the
# value counts of the categorical features using seaborn's `catplot()`.
# The dataset should be split by 'Cardio' so there is one chart for each
# `cardio` value. The chart should look like `examples/Figure_1.png.

cardio_melt = pd.melt(df, id_vars=['id'], value_vars=['cardio'])

print(cardio_melt.head(10))

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values
    # from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = None


    # Group and reformat the data to split it by 'cardio'. Show the counts
    # of each feature. You will have to rename one of the columns for the
    # catplot to work correctly.
    df_cat = None

    # Draw the catplot with 'sns.catplot()'



    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
