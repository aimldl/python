#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lines_bars_and_markers/stem_plot.py

Matplotlib > Gallery > Lines, bars and markers > Stem plot
https://matplotlib.org/gallery/lines_bars_and_markers/stem_plot.html#sphx-glr-gallery-lines-bars-and-markers-stem-plot-py
"""

import matplotlib.pyplot as plt
import numpy as np

# Plot 1
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))

plt.stem(x, y, use_line_collection=True)
plt.show()

# Plot 2
markerline, stemlines, baseline = plt.stem(x, y, linefmt='grey', markerfmt='D', 
                                           bottom=1.1, use_line_collection=True)
markerline.set_markerfacecolor('none')
plt.show()

# Plot 2: changed 'bottom'
markerline, stemlines, baseline = plt.stem(x, y, linefmt='grey', markerfmt='D', 
                                           bottom=1.0, use_line_collection=True)
markerline.set_markerfacecolor('none')
plt.show()
