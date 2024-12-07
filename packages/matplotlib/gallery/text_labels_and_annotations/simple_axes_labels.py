#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
text_labels_and_annotations/simple_axes_labels.py
Matplotlib > Gallery > Text, labels and annotations> Simple axes labels
https://matplotlib.org/3.1.1/gallery/pyplots/fig_axes_labels_simple.html#sphx-glr-gallery-pyplots-fig-axes-labels-simple-py
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
fig.subplots_adjust(top=0.8)
ax1 = fig.add_subplot(211)

# Plot a sine wave
t     = np.arange(0.0, 1.0, 0.01)
s     = np.sin(2 * np.pi * t)
line, = ax1.plot(t, s, lw=2)
ax1.set_ylabel('volts')
ax1.set_title('a sine wave')

# Plot a histogram
np.random.seed(19680801)  # Fixing random state for reproducibility
ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
n, bins, patches = ax2.hist( np.random.randn(1000), 50 )
ax2.set_xlabel('time (s)')

plt.show()