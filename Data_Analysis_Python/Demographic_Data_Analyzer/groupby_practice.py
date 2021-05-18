# This is just pandas practice not relevant to the demographic_data_analyzer
# project

# https://realpython.com/pandas-groupby/

import pandas as pd

# Use 3 decimal places in output display
pd.set_option("display.precision", 3)

# Don't wrap rep(DataFrame) across additional lines
pd.set_option("display.expand_frame_repr", False)

# Set max rows displayed in output to 25
pd.set_option("display.max_rows", 25)

# dtypes save on space efficiency
# Reducing the memory load on your machine

dtypes = {
    "first_name": "category",
    "gender": "category",
    "type": "category",
    "state": "category",
    "party": "category",
}

df = pd.read_csv(
     "groupby-data/legislators-historical.csv",
     dtype=dtypes,
     usecols=list(dtypes) + ["birthday", "last_name"],
     parse_dates=["birthday"]
     )

# Count of congress members by State
# You call .groupby() and pass the name of the column you want to group
# on, which is 'state' - then, you use ['last_name'] to specify
# the column on which you want to perform the actual aggregation
n_by_state = df.groupby("state")["last_name"].count()
# print(type(n_by_state))
# print(n_by_state.head(10))

# You can pass any of the follwoing:
# A list of multiple column names
# A dict or Pandas series
# A NumPy array or Pandas Index, or an array-like iterable of these

by_state = df.groupby("state")
# print(by_state)
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000175F0F42A00>

"""
The object's .__str__() doesn't give you much information into what it
actually is or how it works. The reason that a DataFrameGroupBy object
can be difficult to wrap your head around is that it is **lazy** in nature
It doesn't really do any operations to product a useful result unless
you say so

One term that's frequently used alongside .groupby() is **split-apply-combine**
This refers to three steps:

    1. Split a table into groups
    2. Apply some operations to each of those smaller tables
    3. Combine the results

It can be diffuclt to inspect df.groupby("state") because it does virtually
none of these things until you do something with the resulting object. Again,
a Pandas GroupBy obj is lazy. It delays vitually every part of the split-
apply-combine process until you invoke a method on it.

So, how can you mentally seperate the split, apply, and combine stages if
you can't see any of them happening in isolation? One useful way to inspect
a Pandas GroupBy obj and see the splitting in action is to iterate over it.
This is implemented in DataFrameGroupBy.__iter__() and produces an iterator
of (group, DataFrame) pairs for DataFrames
"""

for state, frame in by_state:
    print(f"First 2 entries for {state!r}")
    print("------------------------")
    print(frame.head(2), end=("\n\n"))






#
