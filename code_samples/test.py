# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:39:45 2019

@author: aimldl
"""

import numpy as np

print( np.random.choice(5, 3, replace=False ) )

a = ['pooh', 'rabbit', 'piglet', 'Christopher']
print( np.random.choice(a, 3, replace=False ) )

print( np.random.choice(8, 32, replace=False ) )

