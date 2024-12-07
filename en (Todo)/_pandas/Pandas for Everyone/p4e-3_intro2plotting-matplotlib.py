#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
p4e-3_intro2plotting-matplotlib.py
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
"""
###############################
# 3. Introduction to Plotting #
###############################

#####################
# 3.1. Introduction #
#####################

import seaborn as sns
anscombe = sns.load_dataset('anscombe')
print( anscombe )
#   dataset     x      y
#0        I  10.0   8.04
#1        I   8.0   6.95
#2        I  13.0   7.58
#3        I   9.0   8.81
#4        I  11.0   8.33
#5        I  14.0   9.96
#6        I   6.0   7.24
#7        I   4.0   4.26
#8        I  12.0  10.84
#9        I   7.0   4.82
#10       I   5.0   5.68
#11      II  10.0   9.14
#12      II   8.0   8.14
#13      II  13.0   8.74
#14      II   9.0   8.77
#15      II  11.0   9.26
#16      II  14.0   8.10
#17      II   6.0   6.13
#18      II   4.0   3.10
#19      II  12.0   9.13
#20      II   7.0   7.26
#21      II   5.0   4.74
#22     III  10.0   7.46
#23     III   8.0   6.77
#24     III  13.0  12.74
#25     III   9.0   7.11
#26     III  11.0   7.81
#27     III  14.0   8.84
#28     III   6.0   6.08
#29     III   4.0   5.39
#30     III  12.0   8.15
#31     III   7.0   6.42
#32     III   5.0   5.73
#33      IV   8.0   6.58
#34      IV   8.0   5.76
#35      IV   8.0   7.71
#36      IV   8.0   8.84
#37      IV   8.0   8.47
#38      IV   8.0   7.04
#39      IV   8.0   5.25
#40      IV  19.0  12.50
#41      IV   8.0   5.56
#42      IV   8.0   7.91
#43      IV   8.0   6.89

###################
# 3.2. Matplotlib #
###################
import matplotlib.pyplot as plt

dataset_1 = anscombe[ anscombe['dataset']== 'I' ]
print( dataset_1 )
#   dataset     x      y
#0        I  10.0   8.04
#1        I   8.0   6.95
#2        I  13.0   7.58
#3        I   9.0   8.81
#4        I  11.0   8.33
#5        I  14.0   9.96
#6        I   6.0   7.24
#7        I   4.0   4.26
#8        I  12.0  10.84
#9        I   7.0   4.82
#10       I   5.0   5.68

plt.plot( dataset_1['x'], dataset_1['y'] )
plt.plot( dataset_1['x'], dataset_1['y'], 'o')

dataset_2 = anscombe[ anscombe['dataset']=='II' ]
dataset_3 = anscombe[ anscombe['dataset']=='III' ]
dataset_4 = anscombe[ anscombe['dataset']=='IV' ]

fig = plt.figure()
axe1 = fig.add_subplot(2,2,1)
axe2 = fig.add_subplot(2,2,2)
axe3 = fig.add_subplot(2,2,3)
axe4 = fig.add_subplot(2,2,4)

axe1.plot( dataset_1['x'], dataset_1['y'], 'o' )
axe2.plot( dataset_2['x'], dataset_2['y'], 'o' )
axe3.plot( dataset_3['x'], dataset_3['y'], 'o' )
axe4.plot( dataset_4['x'], dataset_4['y'], 'o' )

axe1.set_title('dataset_1')
axe2.set_title('dataset_2')
axe3.set_title('dataset_3')
axe4.set_title('dataset_4')

fig.suptitle('Anscombe Data')
fig.tight_layout()

##############################################
# 3.3. Statistical Graphics Using matplotlib #
##############################################
tips = sns.load_dataset('tips')
print( tips.head() )
#   total_bill   tip     sex smoker  day    time  size
#0       16.99  1.01  Female     No  Sun  Dinner     2
#1       10.34  1.66    Male     No  Sun  Dinner     3
#2       21.01  3.50    Male     No  Sun  Dinner     3
#3       23.68  3.31    Male     No  Sun  Dinner     2
#4       24.59  3.61  Female     No  Sun  Dinner     4


#####################
# 3.3.1. Univariate #
#####################
# Univariate = a single variable

#######################
# 3.3.1.1. Histograms #
#######################
fig = plt.figure()
axes1 = fig.add_subplot(1,1,1)
axes1.hist( tips['total_bill'], bins=10 )
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Frequenty')
axes1.set_ylabel('Total Bill')

# Q: What if I skip subplot? Does it still work without the subplot?
# A: No. AttributeError occurs without it.
# fig = plt.figure()
# fig.hist( tips['total_bill'], bins=10 )
# AttributeError: 'Figure' object has no attribute 'hist'

####################
# 3.3.2. Bivariate #
####################
# Vivariate = two variables

########################
# 3.3.2.1. Scatterplot #
########################

scatter_plot = plt.figure()
axe1 = scatter_plot.add_subplot(1,1,1)
axe1.scatter( tips['total_bill'], tips['tip'] )
axe1.set_title('Scatterplot of Total Bill vs. Tip')
axe1.set_xlabel('Total Bill')
axe1.set_ylabel('Tip')
scatter_plot.show()  # This line may be redundant if this script is run in Spyder.
#/home/aimldl/.local/lib/python3.6/site-packages/matplotlib/figure.py:445: 
#UserWarning: Matplotlib is currently using module://ipykernel.pylab.backend_inline,
#which is a non-GUI backend, so cannot show the figure.
#% get_backend())

####################
# 3.3.2.2. Boxplot #
####################
# Boxplots are used when a discrete variable is plotted against a continuous variable.

tips_male = (tips['sex'] == 'Male')
tips_female = (tips['sex'] == 'Female')

boxplot = plt.figure()
axe1 = boxplot.add_subplot(1,1,1)
axe1.boxplot(
        [ tips[ tips_female ]['tip'],
          tips[ tips_male ]['tip']],
          labels=['Female','Male']
        )
axe1.set_title('Boxplot of Tips by Sex')
axe1.set_xlabel('Sex')
axe1.set_ylabel('Tip')
axe1.show()

###########################
# 3.3.3. Multivariate Data#
###########################
# Multivariate = many variables
# There isn't a panacea or template that can be used for very case.

# use color to add a third variable sex to our scatter plot.

def recode_sex( sex ):
    if sex == 'Female':
        return 0
    else:
        return 1

print( tips.head() )
#   total_bill   tip     sex smoker  day    time  size
#0       16.99  1.01  Female     No  Sun  Dinner     2
#1       10.34  1.66    Male     No  Sun  Dinner     3
#2       21.01  3.50    Male     No  Sun  Dinner     3
#3       23.68  3.31    Male     No  Sun  Dinner     2
#4       24.59  3.61  Female     No  Sun  Dinner     4


# Create a new column 'sex_color' from values in column 'sex'.
# Convert Female & Male to 0 & 1, respectively.
tips['sex_color'] = tips['sex'].apply( recode_sex )
print( tips['sex_color'].head() )
#0    0
#1    1
#2    1
#3    1
#4    0
#Name: sex_color, dtype: category
#Categories (2, int64): [1, 0]
#
# Notice Female & Male are converted to 0 & 1, respectively.

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1,2,1)
axes1.scatter(
        x=tips['total_bill'],
        y=tips['tip']
        )
axe1.set_title('Scatterplot of Total Bill vs. Tip')
axe1.set_xlabel('Total Bill')
axe1.set_ylabel('Tip')
scatter_plot.show()

axes2 = scatter_plot.add_subplot(1,2,2)
axes2.scatter(
        x=tips['total_bill'],
        y=tips['tip'],
        s=tips['size'] *10,   # Size of the dots based on party size, scaled by *10
        c=tips['sex_color'],  # Color of the dots
        alpha=0.5  # Set the alpha value so points are more transparent
                   # This helps with overlapping points.
        )
axes2.set_title("'Total Bill vs. Tip' Colored by Sex and Sized by Size")
axes2.set_xlabel('Total Bill')
axes2.set_ylabel('Tip')
scatter_plot.show()
