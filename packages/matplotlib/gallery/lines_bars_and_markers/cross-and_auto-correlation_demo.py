#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lines_bars_and_markers/cross-and_auto-correlation_demo.py

Matplotlib > Gallery > Lines, bars and markers > Cross- and Auto-Correlation Demo
https://matplotlib.org/gallery/lines_bars_and_markers/xcorr_acorr_demo.html#sphx-glr-gallery-lines-bars-and-markers-xcorr-acorr-demo-py
"""

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# np.random.randn(2, 100) returns samples from the “standard normal” distribution.
#   array([[1.0493, 0.866099, ... ,  -1.27382],    # random stored in x
#         [-1.38774, 0.155221, ... , -0.492031]]) # random stored in y
x, y = np.random.randn(2, 100)  # Two random varables with 100 samples
t    = np.arange( 0, len(x) )  # len(x)=100

# Plot auto- & cross-correlation.
fig, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax1.set_title('Auto-Correlation: x')
ax1.grid(True)

ax2.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax2.set_title('Cross-Correlation: x & y')
ax2.grid(True)

plt.show()

# Plot random variable x & y
fig, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
ax1.plot( t, x )
# t.max()=99, So add 1 to display 100 in the figure
ax1.set_xlim( t.min(), t.max()+1 )
ax1.set_ylim(-3, 3)
ax1.set_title('Random variable x')
ax1.grid()

ax2.plot( t, y )
ax2.set_xlim( t.min(), t.max()+1 )
ax2.set_ylim(-3, 3)
ax2.set_title('Random variable y')
ax2.grid()

plt.show()

# Plotting all four plots into 2x2 subplots doesn't work well.
# The x & y ranges of auto- and cross-correlation are weird.
# So I'll just use two subplots like I did above.

#fig, axes = plt.subplots(2, 2, sharex=True)
#axes[0,0].acorr( x, usevlines=True, normed=True, maxlags=50, lw=2, color='C0')
#axes[0,0].set_title('Auto-Correlation: x')
#axes[0,0].grid()
#
#axes[1,0].xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
#axes[1,0].set_title('Cross-Correlation: x & y')
#axes[1,0].grid()
#
#axes[0,1].plot( t, x, color='C0' )
#axes[0,1].set_xlim( t.min(), t.max() )
#axes[0,1].set_ylim(-3, 3)
#axes[0,1].set_title('Random variable x')
#axes[0,1].grid()
#
#axes[1,1].plot( t, y, color='r' )
#axes[1,1].set_xlim( t.min(), t.max() )
#axes[1,1].set_ylim(-3, 3)
#axes[1,1].set_title('Random variable y')
#axes[1,1].grid()
#
#plt.show()
