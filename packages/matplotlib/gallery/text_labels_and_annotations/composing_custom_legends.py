#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
text_labels_and_annotations/composing_custom_legends.py
Matplotlib > Gallery > Text, labels and annotations> Composing Custom Legends
https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/custom_legends.html#sphx-glr-gallery-text-labels-and-annotations-custom-legends-py
"""

# sphinx_gallery_thumbnail_number = 2
from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
# An integer is added from 0 to 9 to the logspace with additive random noise
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
# data is 100x10 numpy array in the float64 type
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(lines)