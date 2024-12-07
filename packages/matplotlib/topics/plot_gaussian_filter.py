#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aimldl > python3 > packages > matplotlib > topics > plot_gaussian_filter.py

2019-11-15 (Fri)
Plot Gaussian Filter to file a patent.
"""

import numpy as np
import matplotlib.pyplot as plt

sigma  = 1.0
sigma2 = sigma*sigma  # sigma
n_samples = 1000

x   = np.linspace(-4, 4, n_samples)
x2  = x*x
g_x = np.exp( - x2 / (2*sigma2)) / np.sqrt( 2*np.pi*sigma2 )

plt.plot( x, g_x )
plt.grid()
plt.xlabel('x')
plt.ylabel('G(x)')
plt.show()
