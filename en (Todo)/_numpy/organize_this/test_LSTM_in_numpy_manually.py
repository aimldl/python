# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 23:09:06 2018

@author: the.kim
"""

import numpy as np

x = np.array( [[1.,1.,1.]] )
print("x=",x)

c = 0.1 * np.asarray( [[0,1]] )
h = 0.1 * np.asarray( [[2,3]] )

num_units = 2
args = np.concatenate( (x,h), axis=1 )
print(args)

out_size = 4 * num_units
proj_size = args.shape[-1]

print(out_size)     # 8
print(proj_size)    # 5  # args.shape -> (1, 5)

print("input ", args)

# Initialize weights to 0.5
weights = 0.5 * np.ones( [proj_size, out_size])
print("weights ", weights)

out = np.matmul(args, weights)
print("out ", out )

# Why does this guy set the bias to 0.5?
bias = 0.5 * np.ones( [out_size] )
print(bias)

concat = out + bias
print(concat)

print(np.split(concat,4,1))

i,j,f,o = np.split(concat,4,1)
print("i ", i)
print("j ", j)
print("f ", f)
print("o ", o)

g = np.tanh(j)
print(g)