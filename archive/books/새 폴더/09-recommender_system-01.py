# -*- coding: utf-8 -*-
'''
09-추천시스
* Draft: 2020-0322 (Sun)
'''

import numpy as np

R = np.array( [[4, np.NaN, np.NaN, 2, np.NaN],
			   [np.NaN, 5, np.NaN, 3, 1],
			   [np.NaN, np.NaN, 3, 4, 4],
			   [5, 2, 1, 2, np.NaN]])
num_users, num_items = R.shape
K=3

np.random.seed(1)
P = np.random.normal( scale=1./K, size=(num_users,K) )
Q = np.random.normal( scale=1./K, size=(num_items,K) )

