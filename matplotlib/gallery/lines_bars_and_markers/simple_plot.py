#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lines_bars_and_markers/simple_plot.py

Matplotlib > Gallery > Lines, bars and markers > Simple plot
https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py
"""

import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# Plot
fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
ax.grid()
fig.savefig("test.png")
plt.show()

# Equivalently
fig, ax = plt.subplots()
ax.plot(t, s)
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
ax.grid()
fig.savefig("test.png")
plt.show()
