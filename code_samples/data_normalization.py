'''
data_normalization.py
https://aimldl.blog.me/221627895429

https://livebook.manning.com/book/deep-learning-with-python/chapter-3/190
'''
from keras.datasets import boston_housing
import numpy as np

# Load data
(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()
print(f'train_data.shape = {train_data.shape}' )  # (404, 13)
print(f'test_data.shape = {test_data.shape}' )    # (102, 13)
print( train_data[0] )
#[  1.23247   0.        8.14      0.        0.538     6.142    91.7
#   3.9769    4.      307.       21.      396.9      18.72   ]
print( train_targets[0] )
# 15.2

# Prepare data
#   Normalize the data with respect to the features
mean = train_data.mean( axis=0 )
std  = train_data.std( axis=0 )

# Option 1
x_train = (train_data - mean) / std
x_test  = (test_data - mean) / std

# Option 2
train_data -= mean
train_data /= std
test_data  -= mean
test_data  /= std

print( 'Compare the normalized values.' )
print( x_train[0] )
print( train_data[0] )
#Compare the normalized values.
#[-0.27224633 -0.48361547 -0.43576161 -0.25683275 -0.1652266  -0.1764426
#  0.81306188  0.1166983  -0.62624905 -0.59517003  1.14850044  0.44807713
#  0.8252202 ]
#[-0.27224633 -0.48361547 -0.43576161 -0.25683275 -0.1652266  -0.1764426
#  0.81306188  0.1166983  -0.62624905 -0.59517003  1.14850044  0.44807713
#  0.8252202 ]

print( x_test[0] )
print( test_data[0] )
#[ 1.55369355 -0.48361547  1.0283258  -0.25683275  1.03838067  0.23545815
#  1.11048828 -0.93976936  1.67588577  1.5652875   0.78447637 -3.48459553
#  2.25092074]
#[ 1.55369355 -0.48361547  1.0283258  -0.25683275  1.03838067  0.23545815
#  1.11048828 -0.93976936  1.67588577  1.5652875   0.78447637 -3.48459553
#  2.25092074]
