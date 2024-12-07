#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pandas_for_everyone-2_6_exporting_and_importing_data-csv.py
2.6.Exporting and Importing data
2.6.2. CSV
CSV (Comman Separated Values)

Popular types of delimiter include:
    comma,
    tab, or even
    semicolon.

CSV's preference to TSV (Tab Separated Values) is 
  possibly because any program can open this kind of data structure
  when collaborating and sharing data.

"""
####################################
# 2.6.Exporting and Importing data #
####################################

###############################
# 2.6.2.2. Importing CSV Data #
###############################
# Uses pd.read_csv.
# I put 2.6.2.2. on top of this Python script
#   simply because the following part is necessary.

import pandas as pd

scientists = pd.read_csv('../data/scientists.csv')
names = scientists['Name']

#################
# 2.6.2. CSV #
#################

# Save a series into a CSV
names.to_csv('../output/scientists_names_series.csv')

# Save a datafrma into a TSV (Tab-Separated Value)
scientists.to_csv('../output/scientists_dataframe.csv', sep='\t')

#############################################
# 2.6.2.1. Removing Row Numbers From Output #
#############################################
# When you open the created CSV or TSV file, 
#   the first column looks like the row number of the dataframe.
# When the save file is opend with a text editor, it looks like this.
#
#   0,Rosaline Franklin
#   1,William Gosset
#   2,Florence Nightingale
#   3,Marie Curie
#   4,Rachel Carson
#   5,John Snow
#   6,Alan Turing
#   7,Johann Gauss
#
# Keep in mind that this column is really saving the row label.
# To remove the row label, use index=False.
names.to_csv('../output/scientists_names_series_no_index.csv', index=False)
#Rosaline Franklin
#William Gosset
#Florence Nightingale
#Marie Curie
#Rachel Carson
#John Snow
#Alan Turing
#Johann Gauss

scientists.to_csv('../output/scientists_dataframe_no_index.csv', index=False)
