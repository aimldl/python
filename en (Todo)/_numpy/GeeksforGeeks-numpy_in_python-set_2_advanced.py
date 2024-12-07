

#NumPy in Python | Set 2 (Advanced)
#https://www.geeksforgeeks.org/numpy-python-set-2-advanced/

#   1. Stacking
#     np.vstack
#     np.hstack
#     np.column_stack
#     np.row_stack
#     np.concatenate
#
#   2.Splitting
#     np.shplit
#     np.vsplit
#     np.array_split
#
#   3.Broadcasting
#     NumPy operations are usually done element-by-element
#       which requires two arrays to have exactly the same shape.
#     Numpy's broadcasting rule relaxes this constraint
#       when the array's shapes meet certain constraints.
#
#     The smaller array is "broadcast"ed across the larger array
#       so that both arrays have compatible shapes.
#     Note there're cases where broadcasting is a bad idea
#       because it leads to inefficient use of memory that slows computation.
#
#     The Broadcasting Rule
#       The size of the trailing axes for both arrays in an operation
#       must either be the same or
#                    one of them must be one.
#     Examples
#       A is the larger array than B.
#       So B is broadcasted or matched the same to fit the size of A.
#       That is, B 1x3 is broadcasted to 4x3.
#
#       A(2-D array): 4 x 3
#       B(1-D array):     3
#       Result      : 4 x 3
#     
#       B is smaller, so its size is matched to that of A.
#       The resulting size of B is 7x3x6x5.
#
#       A(4-D array): 7 x 1 x 6 x 1
#       B(3-D array):     3 x 1 x 5
#       Result      : 7 x 3 x 6 x 5
#
#       This would be a mismatch!
#       A: 4 x 3
#       B:     4
#
#   4. Working with datetime
#     Numpy has core array data types
#       which natively support datetime functionality.
#     The data type is "datetime64".
#
#   5.Linear algebra in Numpy')
#     Various methods to apply linear algebra in Numpy include:
#       rank, determinant, trace, etc.
#       eigen values of matrices
#       matrix & vector products: dot product, inner product, outer product, 
#       matrix exponentiation
#       solving linear or tensor equations
#       and much more!
#
#   Linear regression with least squares method
#     We want to solve this linear equations.
#       x + 2*y = 8
#       3*x + 4*y = 18
#
#   The above linear equations can be expressed in the matrix form like below.
#     [1 2] [x] = [8]
#     [3 4] [y]   [18]

#     AX = B where X =[x], A= [1 2], & B =[8]
#                     [y]     [3 4]       [18]
#     X = A^(-1)B = inv(A)B
#       A linear regression line is of the form:
#       w_1 x + w_2 = y
#
#   The solution is the line that minimizes the sum of the squares of the distance
#     from each data point to the line.
#   Given n pairs of data (x_i,y_i), the parameters that we are looking for are
#     w_1 & w_2 which minimize the error.
#       || (w_1 x_i + w_2 -y_i) ||^2
#     which is squares.

#Datetimes and Timedeltas
#https://docs.scipy.org/doc/numpy-1.15.1/reference/arrays.datetime.html


import numpy as np

print("1.Stacking")
a = np.array( [[1,2],[3,4],] )
print( a )
#[[1 2]
# [3 4]]

b = np.array( [[5,6],[7,8]] )
print( b )
#[[5 6]
# [7 8]]

print( np.vstack( (a,b) ) )
#[[1 2]
# [3 4]
# [5 6]
# [7 8]]

print( np.hstack( (a,b) ) )
#[[1 2 5 6]
# [3 4 7 8]]

c = [5,6]
print( c )
#[5, 6]

print( np.column_stack( (a,c) ) )
#[[1 2 5]
# [3 4 6]]

print( np.row_stack( (a,c) ) )
#[[1 2]
# [3 4]
# [5 6]]

print( np.concatenate( (a,b), 1) )
#[[1 2 5 6]
# [3 4 7 8]]

print( np.concatenate( (a,b), axis=1) )
#[[1 2 5 6]
# [3 4 7 8]]

print( np.concatenate( (a,b),0) )
#[[1 2]
# [3 4]
# [5 6]
# [7 8]]

print( np.concatenate( (a,b), axis=0) )
#[[1 2]
# [3 4]
# [5 6]
# [7 8]]

print("2. Splitting")
a = np.array( [[1,3,5,7,9,11],
               [2,4,6,8,10,12]] )
print( a )
#[[ 1  3  5  7  9 11]
# [ 2  4  6  8 10 12]]

print( np.hsplit(a,2) )
#[array([[1, 3, 5],
#        [2, 4, 6]]),
# array([[ 7,  9, 11],
#        [ 8, 10, 12]])]

print( np.vsplit(a,2) )
#[array([[ 1,  3,  5,  7,  9, 11]]),
# array([[ 2,  4,  6,  8, 10, 12]])]

# Q: What's gonna happen when the size of array is not an even number?

b = np.array( [[1,3,5,7,9,11,13],
               [2,4,6,8,10,12,14]] )
print( b )
#[[ 1  3  5  7  9 11 13]
# [ 2  4  6  8 10 12 14]]

print( np.hsplit(b,2) )
# ValueError: array split does not result in an equal division

print("3. Broadcasting")

# When a scalar value is combined in an operation,
a = np.array( [1.,2.,3.] )
print( a )
#[1. 2. 3.]

# The following operation is equal to...
c = [2.,2.,2.]
print( a*c )
#[2. 4. 6.]
# Note '*' is an elementwise operation!

# ...this! The scalar b is stretched into an array with the same shape as a 
# during the arithmetic operation. This is the simplest broadcasting example.
b = 2.0
print( a*b )
#[2. 4. 6.]
# Comment: Well, this broadcasting thing explains how Numpy works internally.
# I don't actually have to understand it, I guess.
# This is just a scalar multiplication. What's so fuss about it?

# Multiplying a scalar value

a = np.array( [0., 10., 20., 30.] )
print(a)
#[ 0. 10. 20. 30.]

b = np.array( [0.,1.,2.] )
print(b)
#[0. 1. 2.]

print( a[:, np.newaxis] + b )
#[[ 0.  1.  2.]
# [10. 11. 12.]
# [20. 21. 22.]
# [30. 31. 32.]]

print("4. Working with datetime")
# Numpy has core array data types
#   which natively support datetime functionality.
# The data type is "datetime64".

# Create a date
today = np.datetime64('2017-02-12')
print('Date is:', today)
#Date is: 2019-07-06
print('Year is:', np.datetime64(today,'Y'))
#Year is: 2019
print('Month is:', np.datetime64(today,'M'))
#Month is: 2019-07
# Q: How can I get '07' only? The official docs don't explain this!

print('Day is:', np.datetime64(today,'D'))
#Day is: 2019-07-06
# Q: How can I get '06' only? The official docs don't explain this!

# Creating array of dates in a month
dates = np.arange('2017-02','2017-03', dtype='datetime64[D]')
print( dates )
#['2017-02-01' '2017-02-02' '2017-02-03' '2017-02-04' '2017-02-05'
# '2017-02-06' '2017-02-07' '2017-02-08' '2017-02-09' '2017-02-10'
# '2017-02-11' '2017-02-12' '2017-02-13' '2017-02-14' '2017-02-15'
# '2017-02-16' '2017-02-17' '2017-02-18' '2017-02-19' '2017-02-20'
# '2017-02-21' '2017-02-22' '2017-02-23' '2017-02-24' '2017-02-25'
# '2017-02-26' '2017-02-27' '2017-02-28']

# See if today exists within dates and return either True or False.
print( today in dates )
# True

dates_without_D = np.arange('2017-02','2017-03', dtype='datetime64')
print( dates_without_D )
#['2017-02']

dates_without_D2 = np.arange('2017-02','2017-12', dtype='datetime64')
print( dates_without_D2 )
#['2017-02' '2017-03' '2017-04' '2017-05' '2017-06' '2017-07' '2017-08'
# '2017-09' '2017-10' '2017-11']

# Arithmetic operation on dates  # GREP
dur = np.datetime64('2017-05-22') - np.datetime64('2016-05-22')  # GREP
print( dur )    # GREP
#365 days       # GREP
print( np.timedelta64(dur,'W') )  # GREP: the use of timedelta64 is confusing.
#52 weeks       # GREP

#print( np.datetime64(dur,'W') )
#ValueError: Could not convert object to NumPy datetime

# Sorting dates
a = np.array( ['2017-02-12','2016-10-13','2019-05-22'], dtype='datetime64' )
print( np.sort(a) )
#['2016-10-13' '2017-02-12' '2019-05-22']

print('5.Linear algebra in Numpy')
# Various methods to apply linear algebra in Numpy include:
#   rank, determinant, trace, etc.
#   eigen values of matrices
#   matrix & vector products: dot product, inner product, outer product, 
#   matrix exponentiation
#   solving linear or tensor equations
#   and much more!

A = np.array( [[6, 1, 1],
               [4,-2, 5],
               [2, 8, 7]] )
#Rank of A
print( np.linalg.matrix_rank(A) )
#3

# Trace of A
print( np.trace(A) )
#11

# Determinant of A
print( np.linalg.det(A) )
#-306.0

# Inverse of A
print( np.linalg.inv(A) )
#[[ 0.17647059 -0.00326797 -0.02287582]
# [ 0.05882353 -0.13071895  0.08496732]
# [-0.11764706  0.1503268   0.05228758]]

# A raised to power 3
print( np.linalg.matrix_power( A, 3 ) )  # It's not A^3, but A*A*A
#[[336 162 228]
# [406 162 469]
# [698 702 905]]

# We want to solve this linear equations.
#   x + 2*y = 8
# 3*x + 4*y = 18

# Coefficients
A = np.array( [[1,2],[3,4]] )

# Constants
B = np.array([8,18])
print( np.linalg.solve(A,B) )
#[2. 3.]

# The above linear equations can be expressed in the matrix form like below.
# [1 2] [x] = [8]
# [3 4] [y]   [18]

# AX = B where X =[x], A= [1 2], & B =[8]
#                 [y]     [3 4]       [18]
# X = A^(-1)B = inv(A)B

X = np.linalg.inv(A).dot(B)
print( X )
#[2. 3.]

# Linear regression with least squares method
# A linear regression line is of the form:
#   w_1 x + w_2 = y
#
# The solution is the line that minimizes the sum of the squares of the distance
# from each data point to the line.
# Given n pairs of data (x_i,y_i), the parameters that we are looking for are
# w_1 & w_2 which minimize the error.
#   || (w_1 x_i + w_2 -y_i) ||^2
# which is squares.

# import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,9)  # [0,...,8]
print(x)
#[0 1 2 3 4 5 6 7 8]

A = np.array( [x,np.ones(9)] )
print(A)
#[[0. 1. 2. 3. 4. 5. 6. 7. 8.]
# [1. 1. 1. 1. 1. 1. 1. 1. 1.]]
print( A.shape )
#(2, 9)

# TODO

# linearly generated sequence
y = [19,20,20.5,21.5,22,23,23,25.5,24]  # Note this is a list object, not array!
print(y)
print( len(y) )
# 9

w = np.linalg.lstsq( A.T, y)[0]

# Plot the line
line = w[0]*x+w[1]  # Regression line
plt.plot(x,line,'r-')
plt.plot(x,y,'o')
plt.show()
