#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lines_bars_and_markers/using_span_where.py

Matplotlib > Gallery > Lines, bars and markers > Using span_where
https://matplotlib.org/gallery/lines_bars_and_markers/span_regions.html#using-span-where
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as collections

t  = np.arange(0.0, 2, 0.01)
s1 = np.sin(2*np.pi*t)
# This line exists in the example, but it's not used.
#s2 = 1.2*np.sin(4*np.pi*t)

fig, ax = plt.subplots()
ax.set_title('using span_where')
ax.plot(t, s1, color='black')       # Plot s1
ax.axhline(0, color='black', lw=2)  # Draw a horizontal line for y=0

# Green shady area is applied where s1>0
collection = collections.BrokenBarHCollection.span_where(
    t, ymin=0, ymax=1, where=s1 > 0, facecolor='green', alpha=0.5)
ax.add_collection(collection)

# Green shady area is applied where s1<0
collection = collections.BrokenBarHCollection.span_where(
    t, ymin=-1, ymax=0, where=s1 < 0, facecolor='red', alpha=0.5)
ax.add_collection(collection)

plt.show()
