#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
subplots_axes_and_figures/zooming_in_and_out_using_axes_margins_and_the_subject_of_stickiness-2.py

Matplotlib > Gallery > Subplots, axes and figures > Zooming in and out using Axes.margins and the subject of "stickiness"
https://matplotlib.org/gallery/subplots_axes_and_figures/axes_margins.html#sphx-glr-gallery-subplots-axes-and-figures-axes-margins-py

TODO: Test this code.
"""

y, x = np.mgrid[:5, 1:6]
poly_coords = [
    (0.25, 2.75), (3.25, 2.75),
    (2.25, 0.75), (0.25, 0.75)
]
fig, (ax1, ax2) = plt.subplots(ncols=2)

# Here we set the stickiness of the axes object...
# ax1 we'll leave as the default, which uses sticky edges
# and we'll turn off stickiness for ax2
ax2.use_sticky_edges = False

for ax, status in zip((ax1, ax2), ('Is', 'Is Not')):
    cells = ax.pcolor(x, y, x+y, cmap='inferno')  # sticky
    ax.add_patch(
        plt.Polygon(poly_coords, color='forestgreen', alpha=0.5)
    )  # not sticky
    ax.margins(x=0.1, y=0.05)
    ax.set_aspect('equal')
    ax.set_title('{} Sticky'.format(status))

plt.show()
