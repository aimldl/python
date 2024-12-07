#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5])
plt.ylabel('natural numbers')
plt.show()

'''
Problem
AttributeError: module 'matplotlib.pyplot' has no attribute 'plt'

Hint
plt.plt([1, 2, 3, 4, 5])

Solution
plt.plot([1, 2, 3, 4, 5])
'''
