#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
text_labels_and_annotations/composing_custom_legends-2.py
Matplotlib > Gallery > Text, labels and annotations> Composing Custom Legends
https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/custom_legends.html#sphx-glr-gallery-text-labels-and-annotations-custom-legends-py
"""

from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D  # NEW

# Fixing random state for reproducibility
np.random.seed(19680801)
N = 10
# An integer is added from 0 to 9 to the logspace with additive random noise
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
# data is 100x10 numpy array in the float64 type
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

# NEW
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
# NEW