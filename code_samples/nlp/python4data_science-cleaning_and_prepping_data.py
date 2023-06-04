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

column_names = df.columns
print( column_names )

df.dtypes

for i in column_names:
  print('{} is unique: {}'.format( i, df[i].is_unique ))

# Check the index values
#   AttributeError if 'function' object has no attribute 'index'
print( df.index.values )

# If index doesn't exit,
df.set_index('column_name2use', inplace=True )

# Create list comprehension of the columns to drop
columns2drop = [ column_names[i] for i in [1,3,5] ]  

# Drop unwanted columns
df.drop( columns2drop, inplace=True, axis=1)