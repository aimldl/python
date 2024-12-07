#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pandas_for_everyone-2_5_making_changes_to_series_and_dataframes.py
2.5.Making Changes to Series and DataFrames
"""
###############################################
# 2.5.Making Changes to Series and DataFrames #
###############################################

#################################
# 2.5.1. Add Additional Columns #
#################################

# Object means strings

import pandas as pd

scientists = pd.read_csv('../data/scientists.csv')
print( scientists['Born'].dtype )
# object
print( scientists['Died'].dtype )
# object

print( scientists['Born'] )
#0    1920-07-25
#1    1876-06-13
#2    1820-05-12
#3    1867-11-07
#4    1907-05-27
#5    1813-03-15
#6    1912-06-23
#7    1777-04-30
#Name: Born, dtype: object

# format the 'Born' column as a datatime
born_datetime = pd.to_datetime( scientists['Born'], format='%Y-%m-%d')
print( born_datetime )
#0   1920-07-25
#1   1876-06-13
#2   1820-05-12
#3   1867-11-07
#4   1907-05-27
#5   1813-03-15
#6   1912-06-23
#7   1777-04-30
#Name: Born, dtype: datetime64[ns]
# Notice dtype is datetime64!
# The values may look the same dtype has been changed to datetime64.

# format the 'Died' column as a datetime
died_datetime = pd.to_datetime( scientists['Died'], format='%Y-%m-%d')
print( died_datetime )
#0   1958-04-16
#1   1937-10-16
#2   1910-08-13
#3   1934-07-04
#4   1964-04-14
#5   1858-06-16
#6   1954-06-07
#7   1855-02-23
#Name: Died, dtype: datetime64[ns]

# Use Python's multiple assignment syntax
scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
print( scientists.head() )
#                   Name        Born  ...    born_dt    died_dt
#0     Rosaline Franklin  1920-07-25  ... 1920-07-25 1958-04-16
#1        William Gosset  1876-06-13  ... 1876-06-13 1937-10-16
#2  Florence Nightingale  1820-05-12  ... 1820-05-12 1910-08-13
#3           Marie Curie  1867-11-07  ... 1867-11-07 1934-07-04
#4         Rachel Carson  1907-05-27  ... 1907-05-27 1964-04-14
#
#[5 rows x 7 columns]

###################################
# 2.5.2. Directly Change a Column #
###################################

# Before shuffling
print( scientists['Age'] )
#0    37
#1    61
#2    90
#3    66
#4    56
#5    45
#6    41
#7    77
#Name: Age, dtype: int64

# In this example, reset_index is necessary.
# If you try to reassign it or use it again,
#   the "scrambled" values will automatically align to the index
#   and order themselves back to the pre-sample order.

import random
# Set a seed (to 42 ) so the randomness is always the same
random.seed( 42 )

#https://docs.python.org/3.6/library/random.html#random.shuffle
#random.shuffle(x[, random])
#Shuffle the sequence x in place.
random.shuffle( scientists['Age'] )
print("Just shuffling won't shuffule the values")
print( scientists['Age'] )
#0    66
#1    56
#2    41
#3    77
#4    90
#5    45
#6    37
#7    61
#Name: Age, dtype: int64

# The drop=True parameter in reset_index tells Pandas
#   not to insert the index into the dataframe columns,
#   so that only the values are kept.
scientists['Age'] = scientists['Age'].\
  sample( len(scientists['Age']), random_state=24).\
  reset_index(drop=True)  # values stay randomized by dropping the index

print('After reset_index(drop=True)')
print( scientists['Age'] )

# Subtracting dates gives the number of days
scientists['age_days_dt'] = ( scientists['died_dt'] - scientists['born_dt'] )
print( scientists )
#                   Name        Born  ...    died_dt  age_days_dt
#0     Rosaline Franklin  1920-07-25  ... 1958-04-16   13779 days
#1        William Gosset  1876-06-13  ... 1937-10-16   22404 days
#2  Florence Nightingale  1820-05-12  ... 1910-08-13   32964 days
#3           Marie Curie  1867-11-07  ... 1934-07-04   24345 days
#4         Rachel Carson  1907-05-27  ... 1964-04-14   20777 days
#5             John Snow  1813-03-15  ... 1858-06-16   16529 days
#6           Alan Turing  1912-06-23  ... 1954-06-07   15324 days
#7          Johann Gauss  1777-04-30  ... 1855-02-23   28422 days
#[8 rows x 8 columns]

# Convert the days to years using the astype method
scientists['age_years_dt'] = scientists['age_days_dt'].astype('timedelta64[Y]')
print( scientists )
#                   Name        Born  ... age_days_dt  age_years_dt
#0     Rosaline Franklin  1920-07-25  ...  13779 days          37.0
#1        William Gosset  1876-06-13  ...  22404 days          61.0
#2  Florence Nightingale  1820-05-12  ...  32964 days          90.0
#3           Marie Curie  1867-11-07  ...  24345 days          66.0
#4         Rachel Carson  1907-05-27  ...  20777 days          56.0
#5             John Snow  1813-03-15  ...  16529 days          45.0
#6           Alan Turing  1912-06-23  ...  15324 days          41.0
#7          Johann Gauss  1777-04-30  ...  28422 days          77.0
#[8 rows x 9 columns]

# Many functions and methods in pandas will have
#   an inplace parameter
# that you can set to True if you want to perform the action "in place"
# Q: What does it mean by "in place"?

##########################
# 2.5.3. Dropping Values #
##########################
# To drop a column, we can either
#   select all the columns we want to by using the column subsetting techniques,
#   or select columns to drop with the drop method on our dataframe.
# To summarize, (1) column subsetting technique or (2) drop method.

print( scientists.columns )
#                   Name        Born  ... age_days_dt  age_years_dt
#0     Rosaline Franklin  1920-07-25  ...  13779 days          37.0
#1        William Gosset  1876-06-13  ...  22404 days          61.0
#2  Florence Nightingale  1820-05-12  ...  32964 days          90.0
#3           Marie Curie  1867-11-07  ...  24345 days          66.0
#4         Rachel Carson  1907-05-27  ...  20777 days          56.0
#5             John Snow  1813-03-15  ...  16529 days          45.0
#6           Alan Turing  1912-06-23  ...  15324 days          41.0
#7          Johann Gauss  1777-04-30  ...  28422 days          77.0
#[8 rows x 9 columns]

# scientists.rows
#   AttributeError: 'DataFrame' object has no attribute 'rows

# axis=1 to drop column-wise
scientists_dropped = scientists.drop( ['Age'], axis=1 )
print( scientists_dropped )
#                   Name        Born  ... age_days_dt age_years_dt
#0     Rosaline Franklin  1920-07-25  ...  13779 days         37.0
#1        William Gosset  1876-06-13  ...  22404 days         61.0
#2  Florence Nightingale  1820-05-12  ...  32964 days         90.0
#3           Marie Curie  1867-11-07  ...  24345 days         66.0
#4         Rachel Carson  1907-05-27  ...  20777 days         56.0
#5             John Snow  1813-03-15  ...  16529 days         45.0
#6           Alan Turing  1912-06-23  ...  15324 days         41.0
#7          Johann Gauss  1777-04-30  ...  28422 days         77.0
#[8 rows x 8 columns]
