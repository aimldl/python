#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
text_labels_and_annotations/auto-wrapping_text.py
Matplotlib > Gallery > Text, labels and annotations> Auto-wrapping text
https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/autowrap.html#sphx-glr-gallery-text-labels-and-annotations-autowrap-py
"""

import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")
plt.text(4, 1, t, ha='left', rotation=15, wrap=True)
plt.text(6, 5, t, ha='left', rotation=15, wrap=True)
plt.text(5, 5, t, ha='right', rotation=-15, wrap=True)
plt.text(5, 10, t, fontsize=18, style='oblique', ha='center',
         va='top', wrap=True)
plt.text(3, 4, t, family='serif', style='italic', ha='right', wrap=True)
plt.text(-1, 0, t, ha='left', rotation=-15, wrap=True)

plt.show()
