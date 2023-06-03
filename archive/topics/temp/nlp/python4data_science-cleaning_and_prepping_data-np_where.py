# -*- coding: utf-8 -*-
"""
python4data_science-cleaning_and_prepping_data-np_where.py
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


#%%###################################################
# np.where( if_this_is_true, do_this, else_do_that ) #
######################################################

# If you want to do some basic cleaning or feature engineering quickly,
#   np.where is how you can do it.
#
# Consider if you're evaluating a column, 
#   and you want to know if the values are strictly greater than 10.
# If they are y

df['new_column'] = np.where( df[i]>10, 'foo','bar' )

# More complex example
df['new_column'] = np.where( df['col'].str.startswith('foo') and not df['col'].str.endswith('bar'),
                             True, df['col'])

# Even more effective, you can start to nest your np.where
#   so they stack on each other.
# Similar to how you would stack ternay operations,
#   make sure they are readable as yuou can get into a mess quickly with
#   heavily nested statements.

# Three level nesting with np.where

np.where( if_this_is_true_one, do_this,
  np.where( if_this_is_true_two, do_that,
    np.where( if_this_is_true_three, do_foo, do_bar )))

# An example
df=['foo'] = np.where( df['bar']==0,'Zero',
               np.where( df['bar']==1, 'One',
                 np.where( df['bar']==2, 'two', 'three')))