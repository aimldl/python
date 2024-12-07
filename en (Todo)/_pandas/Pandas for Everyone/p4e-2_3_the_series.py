#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pandas_for_everyone-2_3_the_series.py
2.3.The Series
"""

import pandas as pd

##################
# 2.3.The Series #
##################

# Create our example dataframe with a row index label
scientists = pd.DataFrame(
        data = {'Occupation': ['Chemist','Statistician'],
                'Born': ['1920-07-25','1876-06-13'],
                'Died': ['1958-04-16','1937-10-16'],
                'Age': [37,61]
                },
        index=['Rosaline Franklin','William Gosset'],
        columns=['Occupation','Born','Died','Age']
        )
print( scientists )
#                     Occupation        Born        Died  Age
#Rosaline Franklin       Chemist  1920-07-25  1958-04-16   37
#William Gosset     Statistician  1876-06-13  1937-10-16   61

first_row = scientists.loc['William Gosset']
print( type( first_row) )
#<class 'pandas.core.series.Series'>

print( first_row )
#Occupation    Statistician
#Born            1876-06-13
#Died            1937-10-16
#Age                     61
#Name: William Gosset, dtype: object

print( first_row.index )
#Index(['Occupation', 'Born', 'Died', 'Age'], dtype='object')

print( first_row.keys() )
#Index(['Occupation', 'Born', 'Died', 'Age'], dtype='object')

print( first_row.values )
#['Statistician' '1876-06-13' '1937-10-16' 61]

# TODO: Figure this out.
# Q: I don't know what this is... because it's not mentioned in the book.
print( first_row.keys )
#<bound method Series.keys of
#Occupation    Statistician
#Born            1876-06-13
#Died            1937-10-16
#Age                     61
#Name: William Gosset, dtype: object>

# Index is an attribute, so no ().
print( first_row.index[0] )
#Occupation

# keys is a method, so () is necessary.
print( first_row.keys()[0] )
#Occupation
# Notice the results are identical!

#####################################
# 2.3.1. The Series IS ndarray-like #
#####################################

ages = scientists['Age']
print( ages )
#Rosaline Franklin    37
#William Gosset       61
#Name: Age, dtype: int64

# A Series and numpy.ndarray share a lot of similarities. 
# (Numpy is a scientific computing library that typically deals with numeric vectors.)
# A Series can be thought of as an extension to the numpy.ndarray.
# So there is an overlap of attributes and methods.

print( ages.mean() )
#49.0
print( ages.min() )
#37
print( ages.max() )
#61
print( ages.std() )
#16.97056274847714

print( ages.hist() )
# Wow, the historygram is shown in the command line.

#####################################
# 2.3.2. Boolean Subsetting: Series #
#####################################
scientists = pd.read_csv('../data/scientists.csv')

ages = scientists['Age']
print( ages )
#0    37
#1    61
#2    90
#3    66
#4    56
#5    45
#6    41
#7    77
#Name: Age, dtype: int64

print( ages.describe() )
#count     8.000000
#mean     59.125000
#std      18.325918
#min      37.000000
#25%      44.000000
#50%      58.500000
#75%      68.750000
#max      90.000000
#Name: Age, dtype: float64

print( ages.mean() )
#59.125

print( ages[ ages > ages.mean() ] )
#1    61
#2    90
#3    66
#7    77
#Name: Age, dtype: int64

print( ages > ages.mean() )
#0    False
#1     True
#2     True
#3     True
#4    False
#5    False
#6    False
#7     True
#Name: Age, dtype: bool

print( type( ages > ages.mean()) )
#<class 'pandas.core.series.Series'>

manual_bool_values = [True, True, False, False, True, True, False, True]
print( ages[ manual_bool_values ])
#0    37
#1    61
#4    56
#5    45
#7    77
#Name: Age, dtype: int64

##############################################################
# 2.3.3. Operations Are Automatically Aligned and Vectorized #
#        (Broadcasting)                                      #
##############################################################

#######################################
# 2.3.3.1. Vectors of the Same Length #
#######################################
print( ages )
#0    37
#1    61
#2    90
#3    66
#4    56
#5    45
#6    41
#7    77
#Name: Age, dtype: int64

print( ages+ ages )
#0     74
#1    122
#2    180
#3    132
#4    112
#5     90
#6     82
#7    154
#Name: Age, dtype: int64

print( ages * ages )
#0    1369
#1    3721
#2    8100
#3    4356
#4    3136
#5    2025
#6    1681
#7    5929
#Name: Age, dtype: int64

############################################
# 2.3.3.2. Vectors With Integers (Scalars) #
############################################
# The scalar value is repeatly used across all the elements of the vector 'ages'.
print( ages + 100 )
#0    137
#1    161
#2    190
#3    166
#4    156
#5    145
#6    141
#7    177
#Name: Age, dtype: int64

print( ages * 2 )
#0     74
#1    122
#2    180
#3    132
#4    112
#5     90
#6     82
#7    154
#Name: Age, dtype: int64

###########################################
# 2.3.3.3. Vectors With Different Lengths #
###########################################
# The behavior depends on the type of the vectors (after ages).

#################
# With a Series #
#################
# The operation matches the index.
# The rest of the resulting vector is filled with NaN, not a number.
print( ages + pd.Series([1,100]) )
#0     38.0
#1    161.0
#2      NaN
#3      NaN
#4      NaN
#5      NaN
#6      NaN
#7      NaN
#dtype: float64

####################
# With other types #
####################
# The shapes must match.
# For example, ValueError is returned with np.array.

# This will cause an error
#import numpy as np
#print( ages + np.array( [1,100] ) )
#ValueError: operands could not be broadcast together with shapes (8,) (2,) 

###################################################################
# 2.3.3.4. Vectors With Common Index Labels (Automatic Alignment) #
###################################################################
print( ages )
#0    37
#1    61
#2    90
#3    66
#4    56
#5    45
#6    41
#7    77
#Name: Age, dtype: int64

rev_ages = ages.sort_index( ascending=False )
print( rev_ages )
#7    77
#6    41
#5    45
#4    56
#3    66
#2    90
#1    61
#0    37
#Name: Age, dtype: int64
# Notice the index is reversed as well as the value.

print( ages*2 )
#0     74
#1    122
#2    180
#3    132
#4    112
#5     90
#6     82
#7    154
#Name: Age, dtype: int64

print( ages + rev_ages )
#0     74
#1    122
#2    180
#3    132
#4    112
#5     90
#6     82
#7    154
#Name: Age, dtype: int64

# Note we get the same values to ages*2
#   even though the vector is reversed!
# Why? The vectors are aligned FIRST before the operation is carried out.
