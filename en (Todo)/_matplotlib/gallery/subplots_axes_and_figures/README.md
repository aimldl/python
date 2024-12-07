## Matplotlib > Gallery > Subplots, axes and figures > README.md
Selected examples from [Gallery](https://matplotlib.org/gallery/index.html) are below. Basically, each sub-section of this page is an excerpt from the Matplotlib's official document. If necessary, I've modified the code and put some comments.

#### Format of Each Sub-Section
In each sub-section, hyperlinks to the Matplotlib's document and a working Python code are provided. For example, all the sub-sections are formattted as follows.

```
Example Name
Figure
example_name.py
Example Code
Comments
```

Tip: it's convenient to ***"find" a code snippet*** because all the relevant Python codes are aggregated in this page.

### Jump to:
#### Advanced Subplots
* [Aligning Labels](#aligning_labels)

* [Zooming in and out using Axes.margins and the subject of "stickiness"](#zooming_in_and_out_using_axes_margins_and_the_subject_of_stickiness)

#### [Aligning Labels](https://matplotlib.org/gallery/subplots_axes_and_figures/align_labels_demo.html#sphx-glr-gallery-subplots-axes-and-figures-align-labels-demo-py) <a name="aligning_labels"></a>

<img src="https://matplotlib.org/_images/sphx_glr_align_labels_demo_001.png" width="450" height="300"/>

[aligning_labels.py](#aligning_labels.py)
```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

fig = plt.figure(tight_layout=True)
gs = gridspec.GridSpec(2, 2)

ax = fig.add_subplot(gs[0, :])
ax.plot(np.arange(0, 1e6, 1000))
ax.set_ylabel('YLabel0')
ax.set_xlabel('XLabel0')

for i in range(2):
    ax = fig.add_subplot(gs[1, i])
    ax.plot(np.arange(1., 0., -0.1) * 2000., np.arange(1., 0., -0.1))
    ax.set_ylabel('YLabel1 %d' % i)
    ax.set_xlabel('XLabel1 %d' % i)
    if i == 0:
        for tick in ax.get_xticklabels():
            tick.set_rotation(55)
fig.align_labels()  # same as fig.align_xlabels(); fig.align_ylabels()

plt.show()
```

#### [Zooming in and out using Axes.margins and the subject of "stickiness"](https://matplotlib.org/gallery/subplots_axes_and_figures/axes_margins.html#sphx-glr-gallery-subplots-axes-and-figures-axes-margins-py) <a name="zooming_in_and_out_using_axes_margins_and_the_subject_of_stickiness"></a>

##### Zooming in and out using Axes.margins
<img src="https://matplotlib.org/_images/sphx_glr_axes_margins_001.png" width="450" height="300"/>
##### On the "stickiness" of certain plotting methods
<img src="https://matplotlib.org/_images/sphx_glr_axes_margins_002.png" width="450" height="300"/>

[zooming_in_and_out_using_axes_margins_and_the_subject_of_stickiness-1.py](#zooming_in_and_out_using_axes_margins_and_the_subject_of_stickiness-1.py)
```python
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 3.0, 0.01)

ax1 = plt.subplot(212)
ax1.margins(0.05)           # Default margin is 0.05, value 0 means fit
ax1.plot(t1, f(t1))

ax2 = plt.subplot(221)
ax2.margins(2, 2)           # Values >0.0 zoom out
ax2.plot(t1, f(t1))
ax2.set_title('Zoomed out')

ax3 = plt.subplot(222)
ax3.margins(x=0, y=-0.25)   # Values in (-0.5, 0.0) zooms in to center
ax3.plot(t1, f(t1))
ax3.set_title('Zoomed in')

plt.show()
```
[zooming_in_and_out_using_axes_margins_and_the_subject_of_stickiness-2.py](#zooming_in_and_out_using_axes_margins_and_the_subject_of_stickiness-2.py)
```python
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
```

(EOF)
