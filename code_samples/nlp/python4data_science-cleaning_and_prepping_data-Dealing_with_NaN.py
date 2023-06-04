# -*- coding: utf-8 -*-
"""
python4data_science-cleaning_and_prepping_data.py
Cleaning and Prepping Data with Python for Data Science
  — Best Practices and Helpful Packages
Robert R.F. DeFilippi
Oct 15, 2018 · 24 min read
https://medium.com/@rrfd/cleaning-and-prepping-data-with-python-for-data-science-best-practices-and-helpful-packages-af1edfbe2a3

"""
#%%
import pandas as pd

# Check the data quickly
df = pd.read_csv('data')
df.head(10)


#%%####################
# What to do with NaN #
#######################
# Use fillna() and dropna() methods.

# Fill NaN with ' '
df['col'] = df['col'].fillna(' ')

# Fill NaN with 99
df['col'] = df['col'].fillna('99')

# Fill NaN with the mean of the column
df['col'] = df['col'].fillna( df['col'].mean() )

# You can also propagate non-null values forward or backward
#   by putting method='pad'.
# limit=1 fills one value.
# Without this, it will fill the next value in the datafram with the previous
# non-NaN value.

df = pd.DataFrame( data={'col1':[np.nan, np.nan, 2,3,4, np.nan,np.nan]})
#    col1
#0   NaN
#1   NaN
#2   2.0
#3   3.0
#4   4.0 # This is the value to fill forward
#5   NaN
#6   NaN

df.fillna( method='pad', limit=1 )
#    col1
#0   NaN
#1   NaN
#2   2.0
#3   3.0
#4   4.0
#5   4.0 # Filled forward
#6   NaN

#%% TODO: I'll skip this part.