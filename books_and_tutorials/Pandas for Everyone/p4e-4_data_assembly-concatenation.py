#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pandas_for_everyone-4_data_assembly-concatenation.py
4. Data Assembly
4.1. Introduction
4.2. Tidy Data

So what is tidy data? Hdley Wickham's paper defines it as
  meeting the following criteria:
    Each row is an observation.
    Each column is a variable.
    Each type of observational unit forms a table.
4.2.1. Combining Data Sets

When data is tidy, you need to 
  combine various tables together to answer a question.

4.3. Concatenation (concat)
Concatenation can be though of appending a row or column to your data.
"""
####################
# 4. Data Assembly #
####################

################################
# 4.3. Concatenation  (concat) #
################################

######################
# 4.3.1. Adding Rows #
######################

import pandas as pd

df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')

print( df1 )
#    A   B   C   D
#0  a0  b0  c0  d0
#1  a1  b1  c1  d1
#2  a2  b2  c2  d2
#3  a3  b3  c3  d3

print( df2 )
#    A   B   C   D
#0  a4  b4  c4  d4
#1  a5  b5  c5  d5
#2  a6  b6  c6  d6
#3  a7  b7  c7  d7

print( df3 )
#     A    B    C    D
#0   a8   b8   c8   d8
#1   a9   b9   c9   d9
#2  a10  b10  c10  d10
#3  a11  b11  c11  d11

# All the dataframes to be concatenated are passed in a list.
row_concat = pd.concat( [df1,df2,df3] )
print( row_concat )
#     A    B    C    D
#0   a0   b0   c0   d0
#1   a1   b1   c1   d1
#2   a2   b2   c2   d2
#3   a3   b3   c3   d3
#0   a4   b4   c4   d4
#1   a5   b5   c5   d5
#2   a6   b6   c6   d6
#3   a7   b7   c7   d7
#0   a8   b8   c8   d8
#1   a9   b9   c9   d9
#2  a10  b10  c10  d10
#3  a11  b11  c11  d11
# Notice the original row indices are kept.

# Subsetting row 3 of the table.
print( row_concat.iloc[3,] )
#A    a3
#B    b3
#C    c3
#D    d3
#Name: 3, dtype: object

# If () is used, ValueError occus.
# print( row_concat.iloc(3,) )
# ValueError: No axis named 3 for object type <class 'type'>

# Q: What happens when you use loc or ix to subset the new dataframe?
# A: 
print( row_concat.loc[3,] )
#     A    B    C    D
#3   a3   b3   c3   d3
#3   a7   b7   c7   d7
#3  a11  b11  c11  d11

###############################
# Section 2.2.1 shows the process for creating a Series.

# Create a new row of data
new_row_series = pd.Series( ['n1','n2','n3','n4'] )
print( new_row_series )
#0    n1
#1    n2
#2    n3
#3    n4

# Attempt to add the new row to a dataframe
# Concatenating a Series to a dataframe doesn't append correctly!
print( pd.concat([df1, new_row_series]) )
#     A    B    C    D    0
#0   a0   b0   c0   d0  NaN
#1   a1   b1   c1   d1  NaN
#2   a2   b2   c2   d2  NaN
#3   a3   b3   c3   d3  NaN
#0  NaN  NaN  NaN  NaN   n1
#1  NaN  NaN  NaN  NaN   n2
#2  NaN  NaN  NaN  NaN   n3
#3  NaN  NaN  NaN  NaN   n4

 # TODO: Let's start from p.321

###############################
# 4.3.1.1. Ignoring the Index #
###############################

#########################
# 4.3.2. Adding Columns #
#########################

###############################################
# 4.3.3. Concatenation With Different Indices #
###############################################

####################################################
# 4.3.3.1. Concatenate Rows With Different Columns #
####################################################

####################################################
# 4.3.3.2. Concatenate Columns With Different Rows #
####################################################





