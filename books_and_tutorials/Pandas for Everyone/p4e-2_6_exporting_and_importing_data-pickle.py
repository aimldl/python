#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pandas_for_everyone-2_6_exporting_and_importing_data-pickle.py
2.6.Exporting and Importing data
2.6.1. pickle

The pickle files are saved with an extension of .p, .pkl, or .pickle.
"""
####################################
# 2.6.Exporting and Importing data #
####################################

#################
# 2.6.1. pickle #
#################

##################
# 2.6.1.1 Series #
##################

import pandas as pd

scientists = pd.read_csv('../data/scientists.csv')
print( scientists )
#                   Name        Born        Died  Age          Occupation
#0     Rosaline Franklin  1920-07-25  1958-04-16   37             Chemist
#1        William Gosset  1876-06-13  1937-10-16   61        Statistician
#2  Florence Nightingale  1820-05-12  1910-08-13   90               Nurse
#3           Marie Curie  1867-11-07  1934-07-04   66             Chemist
#4         Rachel Carson  1907-05-27  1964-04-14   56           Biologist
#5             John Snow  1813-03-15  1858-06-16   45           Physician
#6           Alan Turing  1912-06-23  1954-06-07   41  Computer Scientist
#7          Johann Gauss  1777-04-30  1855-02-23   77       Mathematician

names = scientists['Name']
print( names )
#0       Rosaline Franklin
#1          William Gosset
#2    Florence Nightingale
#3             Marie Curie
#4           Rachel Carson
#5               John Snow
#6             Alan Turing
#7            Johann Gauss

names.to_pickle('../output/scientists_names_series.pickle')

#####################
# 2.6.1.2 DataFrame #
#####################
scientists.to_pickle('../output/scientists_dataframe.pickle')
# The file name in the book is 'scientists_df.pickle'

###############################
# 2.6.1.3 Reading pickle Data #
###############################
scientist_names_from_pickle = pd.read_pickle('../output/scientists_names_series.pickle')
print( scientist_names_from_pickle )
#0       Rosaline Franklin
#1          William Gosset
#2    Florence Nightingale
#3             Marie Curie
#4           Rachel Carson
#5               John Snow
#6             Alan Turing
#7            Johann Gauss
#Name: Name, dtype: object

scientists_from_pickle = pd.read_pickle('../output/scientists_dataframe.pickle')
print( scientists_from_pickle )
#                   Name        Born        Died  Age          Occupation
#0     Rosaline Franklin  1920-07-25  1958-04-16   37             Chemist
#1        William Gosset  1876-06-13  1937-10-16   61        Statistician
#2  Florence Nightingale  1820-05-12  1910-08-13   90               Nurse
#3           Marie Curie  1867-11-07  1934-07-04   66             Chemist
#4         Rachel Carson  1907-05-27  1964-04-14   56           Biologist
#5             John Snow  1813-03-15  1858-06-16   45           Physician
#6           Alan Turing  1912-06-23  1954-06-07   41  Computer Scientist
#7          Johann Gauss  1777-04-30  1855-02-23   77       Mathematician

