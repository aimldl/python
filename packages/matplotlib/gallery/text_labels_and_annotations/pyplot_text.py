#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
text_labels_and_annotations/pyplot_text.py
Matplotlib > Gallery > Text, labels and annotations> Pyplot Text
https://matplotlib.org/3.1.1/gallery/pyplots/pyplot_text.html#sphx-glr-gallery-pyplots-pyplot-text-py
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)  # Fixing random state for reproducibility

# Gaussian Distribution
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')  # plt.text(x, y, text)
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()