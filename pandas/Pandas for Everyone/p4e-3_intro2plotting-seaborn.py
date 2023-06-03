#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
p4e-3_intro2plotting-seaborn.py
pandas_for_everyone
3. Introduction to Plotting
  3.1. Introduction
  3.2. Matplotlib
  3.3. Statistical Graphics Using matplotlib
    3.3.1. Univariate
      3.3.1.1. Histograms
    3.3.2. Bivariate
      3.3.2.1. Scatterplot
      3.3.2.2. Boxplot
    3.3.3. Multivariate Data
  3.4. Seaborn
    3.4.1. Univariate
      3.4.1.1. Histograms
      3.4.1.2. Density Plot (Kernel Density Estimation)
      3.4.1.3. Rug Plot
      3.4.1.4. Count Plot (Bar Plot)
    3.4.2. Bivariate Data
      3.4.2.1. Scatter Plot
      # TODO: Start from here.  
"""
#%%############################
# 3. Introduction to Plotting #
###############################

import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset('tips')

################
# 3.4. Seaborn #
################
#####################
# 3.4.1. Univariate #
#####################
#%%###################
# 3.4.1.1. Histograms#
######################
# If only histogram is desired, set 'kde=False'.
#  KDE (Kernel Density Estimation)
hist, ax = plt.subplots()
ax = sns.distplot( tips['total_bill'], kde=False )
ax.set_title('Total Bill Histogram')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Frequency')
plt.show()


#%% distplot plots both a histogram 
#   and a density plot (using a kernel density estimation)

hist, ax = plt.subplots()

ax = sns.distplot( tips['total_bill'] )
ax.set_title('Total Bill Histogram with Density Plot')
plt.show()

# A bell curve is shown that follows the same trend
#   as the histogram bars.
# (Note: All values are marked approximate.)

#%%##################################################
# 3.4.1.2. Density Plot (Kernel Density Estimation) #
#####################################################

# set 'hist=False' to plot the density plots.
den, ax = plt.subplots()
ax = sns.distplot( tips['total_bill'], hist=False)
ax.set_title('Total Bill Density')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Unit Probability')
plt.show()

# You can also sns.kdeplot if you just want a density plot
den, ax = plt.subplots()
ax = sns.kdeplot( tips['total_bill'] )
ax.set_title('Total Bill Density (kdeplot)')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Unit Probability')
plt.show()


#%%##################
# 3.4.1.3. Rug Plot #
#####################
# Rug plots are a one-dimensional representation of a variable's distribution.
# They are typically used with other plots to enhance a visualization.

hist_den_rug, ax = plt.subplots()
ax = sns.distplot( tips['total_bill'], rug=True)
ax.set_title('Total Bill Histogram with Density and Rug Plot')
ax.set_xlabel('Total Bill')
plt.show()

# A bell curve is shown touching the horizontal axis
#   with histogram bars shown between them.
# Q: I don't understand the meaning of this rug plot.

#%%###############################
# 3.4.1.4. Count Plot (Bar Plot) #
##################################
# Bar plots can be used to count discrete variables.

count, ax = plt.subplots()
ax = sns.countplot( 'day', data=tips )
ax.set_title('Count of days')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Frequency')
plt.show()


#%%######################
# 3.4.2. Bivariate Data #
#########################

#%%######################
# 3.4.2.1. Scatter Plot #
#########################
# TODO: Start from here.
