#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
p4e-1_2_and_3_loading_data_and_looking_at_columns_rows_and_cells.py
pandas_for_everyone

Clone or download the dataset at https://github.com/jennybc/gapminder
File gapminder.tsv located at jennybc/gapminder/inst/extdata/gapminder.tsv.
"""

#%%#################################
# 1.2. Loading Your First Data Set #
####################################

import pandas as pd

df = pd.read_csv('../data/gapminder.tsv', delimiter='\t')
print( type(df) )
#<class 'pandas.core.frame.DataFrame'>

print( df.shape )
#(16230, 1)

print( df.columns )
# Index(['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap'], dtype='object')

print( df.dtypes )
#country       object
#continent     object
#year           int64
#lifeExp      float64
#pop            int64
#gdpPercap    float64
#dtype: object

print( df.info() )
#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 1704 entries, 0 to 1703
#Data columns (total 6 columns):
#country      1704 non-null object
#continent    1704 non-null object
#year         1704 non-null int64
#lifeExp      1704 non-null float64
#pop          1704 non-null int64
#gdpPercap    1704 non-null float64
#dtypes: float64(2), int64(2), object(2)
#memory usage: 80.0+ KB
#None

#%%#########################################
# 1.3. Looking at Columns, Rows, and Cells #
############################################

# 1.3.1. Subsetting Columns
# 1.3.1.1 Subsetting Columns by Name
country_df = df['country']
print( country_df.head() )
#0    Afghanistan
#1    Afghanistan
#2    Afghanistan
#3    Afghanistan
#4    Afghanistan
#Name: country, dtype: object

print( country_df.tail() )
#1699    Zimbabwe
#1700    Zimbabwe
#1701    Zimbabwe
#1702    Zimbabwe
#1703    Zimbabwe
#Name: country, dtype: object

subset = df[ ['country', 'continent', 'year'] ]
print( subset.tail() )
#1699  Zimbabwe    Africa  1987
#1700  Zimbabwe    Africa  1992
#1701  Zimbabwe    Africa  1997
#1702  Zimbabwe    Africa  2002
#1703  Zimbabwe    Africa  2007

# 1.3.1.2 Subsetting Columns by Index Position Break in Pandas v0.20
# No example!

#%% 1.3.2. Subsetting Rows
# 1.3.2.1 Subsetting Rows by Index Label: loc

print( df.head() )
#       country continent  year  lifeExp       pop   gdpPercap
#0  Afghanistan      Asia  1952   28.801   8425333  779.445314
#1  Afghanistan      Asia  1957   30.332   9240934  820.853030
#2  Afghanistan      Asia  1962   31.997  10267083  853.100710
#3  Afghanistan      Asia  1967   34.020  11537966  836.197138
#4  Afghanistan      Asia  1972   36.088  13079460  739.981106

print( df.loc(0) )
#<pandas.core.indexing._LocIndexer object at 0x7f339082dd18>
#-> Wrong!

print( df.loc[0] )
#country      Afghanistan
#continent           Asia
#year                1952
#lifeExp           28.801
#pop              8425333
#gdpPercap        779.445
#Name: 0, dtype: object
#-> Right!

print( df.loc[99] )
#country      Bangladesh
#continent          Asia
#year               1967
#lifeExp          43.453
#pop            62821884
#gdpPercap       721.186
#Name: 99, dtype: object


#%% Getting the last row
#print( df.loc[-1] )
# KeyError: -1
# This will cause an error!
# Because loc is waiting for an actual row number!
# But print( df.iloc[-1] ) does work!

number_of_rows = df.shape[0]
last_row_index = number_of_rows -1
print( df.loc[last_row_index] )
#country      Zimbabwe
#continent      Africa
#year             2007
#lifeExp        43.487
#pop          12311143
#gdpPercap     469.709
#Name: 1703, dtype: object

print( df.tail(1) )
#        country continent  year  lifeExp       pop   gdpPercap
# 1703  Zimbabwe    Africa  2007   43.487  12311143  469.709298

# Q: Why do the output results differ?
# A: It's because head & tail outputs DataFrame while loc[n] outputs Series.

subset_loc  = df.loc[0]
subset_head = df.head(1)

print( type(subset_loc) )
#<class 'pandas.core.series.Series'>

print( type(subset_head) )
#<class 'pandas.core.frame.DataFrame'>

# 1.3.2.1 Subsetting Rows by Row Number: iloc
# iloc does the same thing as loc, but is used to subset by the row index number.
# Keep in mind that the index labels do not necessarily have to be row numbers.

print( df.iloc[1] )
#country      Afghanistan
#continent           Asia
#year                1957
#lifeExp           30.332
#pop              9240934
#gdpPercap        820.853
#Name: 1, dtype: object

print( df.loc[1] )
#country      Afghanistan
#continent           Asia
#year                1957
#lifeExp           30.332
#pop              9240934
#gdpPercap        820.853
#Name: 1, dtype: object

print( df.iloc[99] )
#country      Bangladesh
#continent          Asia
#year               1967
#lifeExp          43.453
#pop            62821884
#gdpPercap       721.186
#Name: 99, dtype: object

print( df.iloc[-1] )
#country      Zimbabwe
#continent      Africa
#year             2007
#lifeExp        43.487
#pop          12311143
#gdpPercap     469.709
#Name: 1703, dtype: object

print( df.iloc[ [0,99,999] ] )
#         country continent  year  lifeExp       pop    gdpPercap
#0    Afghanistan      Asia  1952   28.801   8425333   779.445314
#99    Bangladesh      Asia  1967   43.453  62821884   721.186086
#999     Mongolia      Asia  1967   51.253   1149500  1226.041130

# 1.3.2.3 Subsetting Rows with ix No Longer Works in Pandas v.0.20
# There's an example, but I won't do it.
#df.ix[0]
#df.ix[99]
#df.ix[0,99,999]

#%% 1.3.3. Mixing It Up
# TODO: Work on the examples from here.
