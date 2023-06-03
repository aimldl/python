#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lines_bars_and_markers/hlines_and_vlines.py

Matplotlib > Gallery > Lines, bars and markers > hlines and vlines
https://matplotlib.org/gallery/lines_bars_and_markers/vline_hline_demo.html#sphx-glr-gallery-lines-bars-and-markers-vline-hline-demo-py
"""

import matplotlib.pyplot as plt
import numpy as np

t   = np.arange(0.0, 5.0, 0.1)
s   = np.exp(-t) + np.sin(2 * np.pi * t) + 1
nse = np.random.normal(0.0, 0.3, t.shape) * s

fig, (vax, hax) = plt.subplots(1, 2, figsize=(12, 6))

# Plot the figure on the left
vax.plot(t, s + nse, '^')  # the green triangles, s+ noise
vax.vlines(t, [0], s)      # Black vertical lines for the signal

# By using ``transform=vax.get_xaxis_transform()`` the y coordinates are scaled
# such that 0 maps to the bottom of the axes and 1 to the top.

# red vertical lines on x=1 & x=2
vax.vlines([1, 2], 0, 1, transform=vax.get_xaxis_transform(), colors='r')
vax.set_xlabel('time (s)')
vax.set_title('Vertical lines demo')
# The left figure is completed above.

# Plot the figure on the right
#   The x & y axises are reversed!
hax.plot(s + nse, t, '^')
hax.hlines(t, [0], s, lw=2)
hax.set_xlabel('time (s)')
hax.set_title('Horizontal lines demo')

# I added the following line to draw two horizontal lines at y=1 & y=2
# Notice three changes:
#  (1) vax.vlines    -> hax.hlines,
#  (2) transform=vax -> transform.hax
#  (3) get_xaxis_... -> get_yaxis_...
hax.hlines([1, 2], 0, 1, transform=hax.get_yaxis_transform(), colors='r')

plt.show()
