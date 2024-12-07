#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
p4e-1_4_groupd_and_aggregated_calculations-groupby.py
pandas_for_everyone

Clone or download the dataset at https://github.com/jennybc/gapminder
File gapminder.tsv located at jennybc/gapminder/inst/extdata/gapminder.tsv.
"""

#%%######################
# Prerequisite for 1.4. #
#########################
# THIS PART IS NOT IN THE BOOK
import pandas as pd

df = pd.read_csv('../data/gapminder.tsv', delimiter='\t')
print( df.head() )
#       country continent  year  lifeExp       pop   gdpPercap
#0  Afghanistan      Asia  1952   28.801   8425333  779.445314
#1  Afghanistan      Asia  1957   30.332   9240934  820.853030
#2  Afghanistan      Asia  1962   31.997  10267083  853.100710
#3  Afghanistan      Asia  1967   34.020  11537966  836.197138
#4  Afghanistan      Asia  1972   36.088  13079460  739.981106

#%% The concept of groupby.

df_year = df.groupby('year')
print( df_year.head() )
# head doesn't work? But there's only one count for...
#        country continent  year  lifeExp       pop     gdpPercap
#0   Afghanistan      Asia  1952   28.801   8425333    779.445314
#1   Afghanistan      Asia  1957   30.332   9240934    820.853030
#2   Afghanistan      Asia  1962   31.997  10267083    853.100710
#3   Afghanistan      Asia  1967   34.020  11537966    836.197138
#4   Afghanistan      Asia  1972   36.088  13079460    739.981106
#5   Afghanistan      Asia  1977   38.438  14880372    786.113360
#6   Afghanistan      Asia  1982   39.854  12881816    978.011439
#7   Afghanistan      Asia  1987   40.822  13867957    852.395945
#8   Afghanistan      Asia  1992   41.674  16317921    649.341395
#9   Afghanistan      Asia  1997   41.763  22227415    635.341351
#10  Afghanistan      Asia  2002   42.129  25268405    726.734055
#11  Afghanistan      Asia  2007   43.828  31889923    974.580338
#12      Albania    Europe  1952   55.230   1282697   1601.056136
#13      Albania    Europe  1957   59.280   1476505   1942.284244
#14      Albania    Europe  1962   64.820   1728137   2312.888958
#15      Albania    Europe  1967   66.220   1984060   2760.196931
#16      Albania    Europe  1972   67.690   2263554   3313.422188
#17      Albania    Europe  1977   68.930   2509048   3533.003910
#18      Albania    Europe  1982   70.420   2780097   3630.880722
#19      Albania    Europe  1987   72.000   3075321   3738.932735
#20      Albania    Europe  1992   71.581   3326498   2497.437901
#21      Albania    Europe  1997   72.950   3428038   3193.054604
#22      Albania    Europe  2002   75.651   3508512   4604.211737
#23      Albania    Europe  2007   76.423   3600523   5937.029526
#24      Algeria    Africa  1952   43.077   9279525   2449.008185
#25      Algeria    Africa  1957   45.685  10270856   3013.976023
#26      Algeria    Africa  1962   48.303  11000948   2550.816880
#27      Algeria    Africa  1967   51.407  12760499   3246.991771
#28      Algeria    Africa  1972   54.518  14760787   4182.663766
#29      Algeria    Africa  1977   58.014  17152804   4910.416756
#30      Algeria    Africa  1982   61.368  20033753   5745.160213
#31      Algeria    Africa  1987   65.799  23254956   5681.358539
#32      Algeria    Africa  1992   67.744  26298373   5023.216647
#33      Algeria    Africa  1997   69.152  29072015   4797.295051
#34      Algeria    Africa  2002   70.994  31287142   5288.040382
#35      Algeria    Africa  2007   72.301  33333216   6223.367465
#36       Angola    Africa  1952   30.015   4232095   3520.610273
#37       Angola    Africa  1957   31.999   4561361   3827.940465
#38       Angola    Africa  1962   34.000   4826015   4269.276742
#39       Angola    Africa  1967   35.985   5247469   5522.776375
#40       Angola    Africa  1972   37.928   5894858   5473.288005
#41       Angola    Africa  1977   39.483   6162675   3008.647355
#42       Angola    Africa  1982   39.942   7016384   2756.953672
#43       Angola    Africa  1987   39.906   7874230   2430.208311
#44       Angola    Africa  1992   40.647   8735988   2627.845685
#45       Angola    Africa  1997   40.963   9875024   2277.140884
#46       Angola    Africa  2002   41.003  10866106   2773.287312
#47       Angola    Africa  2007   42.731  12420476   4797.231267
#48    Argentina  Americas  1952   62.485  17876956   5911.315053
#49    Argentina  Americas  1957   64.399  19610538   6856.856212
#50    Argentina  Americas  1962   65.142  21283783   7133.166023
#51    Argentina  Americas  1967   65.634  22934225   8052.953021
#52    Argentina  Americas  1972   67.065  24779799   9443.038526
#53    Argentina  Americas  1977   68.481  26983828  10079.026740
#54    Argentina  Americas  1982   69.942  29341374   8997.897412
#55    Argentina  Americas  1987   70.774  31620918   9139.671389
#56    Argentina  Americas  1992   71.868  33958947   9308.418710
#57    Argentina  Americas  1997   73.275  36203463  10967.281950
#58    Argentina  Americas  2002   74.340  38331121   8797.640716
#59    Argentina  Americas  2007   75.320  40301927  12779.379640

print( df_year )
#<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f339063d860>

print( df_year.head() )
#        country continent  year  lifeExp       pop     gdpPercap
#0   Afghanistan      Asia  1952   28.801   8425333    779.445314
#1   Afghanistan      Asia  1957   30.332   9240934    820.853030
#...
#58    Argentina  Americas  2002   74.340  38331121   8797.640716
#59    Argentina  Americas  2007   75.320  40301927  12779.379640
# Well, head doesn't work?

#%% What's the difference?
# Let's find out year=1952
print( df[ df['year']== 1952 ] )
#                       country continent  ...        pop     gdpPercap
#0                  Afghanistan      Asia  ...    8425333    779.445314
#12                     Albania    Europe  ...    1282697   1601.056136
#                       ...       ...  ...        ...           ...
#1680                    Zambia    Africa  ...    2672000   1147.388831
#1692                  Zimbabwe    Africa  ...    3080907    406.884115

#[142 rows x 6 columns]

#%% groupby groups in terms of each year such as 1952, 1957, and so on.

print( df_year['lifeExp'] )
#<pandas.core.groupby.generic.SeriesGroupBy object at 0x7f339064e080>

print( df_year['lifeExp'].head() )
#0     28.801
#1     30.332
#...
#58    74.340
#59    75.320
#Name: lifeExp, dtype: float64

# THIS PART IS NOT IN THE BOOK

#%%#########################################
# 1.4. Grouped and Aggregated Calculations #
############################################
print( df_year['lifeExp'].mean() )
#year
#1952    49.057620
#1957    51.507401
#1962    53.609249
#1967    55.678290
#1972    57.647386
#1977    59.570157
#1982    61.533197
#1987    63.212613
#1992    64.160338
#1997    65.014676
#2002    65.694923
#2007    67.007423
#Name: lifeExp, dtype: float64

# For each year, get the mean...

grouped_year_df = df.groupby('year')
print( type(grouped_year_df) )
#<class 'pandas.core.groupby.generic.DataFrameGroupBy'>

# The following command returns only the memory location.
print( grouped_year_df )
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f3390789400>

grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print( type(grouped_year_df_lifeExp) )
#<class 'pandas.core.groupby.generic.SeriesGroupBy'>

print( grouped_year_df_lifeExp )
#<pandas.core.groupby.generic.SeriesGroupBy object at 0x7f3390638eb8>

# Because we know the Series grouped_year_df_lifeExp is of type float64.

mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print( mean_lifeExp_by_year )
#year
#1952    49.057620
#1957    51.507401
#1962    53.609249
#1967    55.678290
#1972    57.647386
#1977    59.570157
#1982    61.533197
#1987    63.212613
#1992    64.160338
#1997    65.014676
#2002    65.694923
#2007    67.007423
#Name: lifeExp, dtype: float64

#%%#############################
# Group-by on Multiple Columns #
################################
#   Q: What if we want to group and stratify the data by more than one variable?
# = Q: What if we want to perform the same cauculation on multiple columns?

multi_group_var = df.groupby( ['year','continent'])[ ['lifeExp', 'gdpPercap'] ].mean()
print( multi_group_var )

# The output data is grouped by year AND continent.
# For each year-continent pair, mean is applied both on lifeExp and gdpPercap.
# Notice the hierarchical structure in the columns between year and continent.
# To flatten the dataframe, use the reset_index method below.

#                  lifeExp     gdpPercap
#year continent                         
#1952 Africa     39.135500   1252.572466
#     Americas   53.279840   4079.062552
#     Asia       46.314394   5195.484004
#     Europe     64.408500   5661.057435
#     Oceania    69.255000  10298.085650
#1957 Africa     41.266346   1385.236062
#     Americas   55.960280   4616.043733
#     Asia       49.318544   5787.732940
#     Europe     66.703067   6963.012816
#     Oceania    70.295000  11598.522455
#1962 Africa     43.319442   1598.078825
#     Americas   58.398760   4901.541870
#     Asia       51.563223   5729.369625
#     Europe     68.539233   8365.486814
#     Oceania    71.085000  12696.452430
#1967 Africa     45.334538   2050.363801
#     Americas   60.410920   5668.253496
#     Asia       54.663640   5971.173374
#     Europe     69.737600  10143.823757
#     Oceania    71.310000  14495.021790
#1972 Africa     47.450942   2339.615674
#     Americas   62.394920   6491.334139
#     Asia       57.319269   8187.468699
#     Europe     70.775033  12479.575246
#     Oceania    71.910000  16417.333380
#1977 Africa     49.580423   2585.938508
#     Americas   64.391560   7352.007126
#     Asia       59.610556   7791.314020
#     Europe     71.937767  14283.979110
#     Oceania    72.855000  17283.957605
#1982 Africa     51.592865   2481.592960
#     Americas   66.228840   7506.737088
#     Asia       62.617939   7434.135157
#     Europe     72.806400  15617.896551
#     Oceania    74.290000  18554.709840
#1987 Africa     53.344788   2282.668991
#     Americas   68.090720   7793.400261
#     Asia       64.851182   7608.226508
#     Europe     73.642167  17214.310727
#     Oceania    75.320000  20448.040160
#1992 Africa     53.629577   2281.810333
#     Americas   69.568360   8044.934406
#     Asia       66.537212   8639.690248
#     Europe     74.440100  17061.568084
#     Oceania    76.945000  20894.045885
#1997 Africa     53.598269   2378.759555
#     Americas   71.150480   8889.300863
#     Asia       68.020515   9834.093295
#     Europe     75.505167  19076.781802
#     Oceania    78.190000  24024.175170
#2002 Africa     53.325231   2599.385159
#     Americas   72.422040   9287.677107
#     Asia       69.233879  10174.090397
#     Europe     76.700600  21711.732422
#     Oceania    79.740000  26938.778040
#2007 Africa     54.806038   3089.032605
#     Americas   73.608120  11003.031625
#     Asia       70.728485  12473.026870
#     Europe     77.648600  25054.481636
#     Oceania    80.719500  29810.188275

# To flatten the dataframe, use the reset_index method below.
# The hierarchical structure in the columns are gone!

flat = multi_group_var.reset_index()
print( flat.head(15) )
#    year continent    lifeExp     gdpPercap
#0   1952    Africa  39.135500   1252.572466
#1   1952  Americas  53.279840   4079.062552
#2   1952      Asia  46.314394   5195.484004
#3   1952    Europe  64.408500   5661.057435
#4   1952   Oceania  69.255000  10298.085650
#5   1957    Africa  41.266346   1385.236062
#6   1957  Americas  55.960280   4616.043733
#7   1957      Asia  49.318544   5787.732940
#8   1957    Europe  66.703067   6963.012816
#9   1957   Oceania  70.295000  11598.522455
#10  1962    Africa  43.319442   1598.078825
#11  1962  Americas  58.398760   4901.541870
#12  1962      Asia  51.563223   5729.369625
#13  1962    Europe  68.539233   8365.486814
#14  1962   Oceania  71.085000  12696.452430

#%%################################
# 1.4.2. Grouped Frequency Counts #
###################################
# Another common data-related task is to calculate frequencies.
# Use nunique and value_counts.

# The number of unique values in a series
print( df.groupby('continent')['country'].nunique() )
#continent
#Africa      52
#Americas    25
#Asia        33
#Europe      30
#Oceania      2
#Name: country, dtype: int64

