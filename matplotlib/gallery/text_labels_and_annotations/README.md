## Matplotlib > Gallery > ***Text, labels and annotations*** > README.md
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

### Table of Contents
#### Legend
* [Composing Custom Legends](#composing_custom_legends)

#### Text
* [Pyplot Text](#pyplot_text)
* [Using accented text in matplotlib](#using_accented_text_in_matplotlib)
* [Auto-wrapping text](#auto-wrapping_text)

#### Axes
* [Simple axes labels](#simple_axes_labels)
---
#### [Composing Custom Legends](https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/custom_legends.html#sphx-glr-gallery-text-labels-and-annotations-custom-legends-py) <a name="composing_custom_legends"></a>

* Default: legend per lline
<img src="https://matplotlib.org/3.1.1/_images/sphx_glr_custom_legends_001.png" width="450" height="300"/>

[composing_custom_legends.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/composing_custom_legends.py)
```python
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
```
Notice the role of cycler. The colors of lines look different without the line:
> rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))
<img src="https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/fig-composing_custom_legends-no_rcParams.png" width="450" height="300"/>

* Custom Legend
<img src="https://matplotlib.org/3.1.1/_images/sphx_glr_custom_legends_002.png" width="450" height="300"/>

[composing_custom_legends-2.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/composing_custom_legends-2.py)

```python
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
```
* Different Kinds of Labels: Line, Scatter, Color Patch
<img src="https://matplotlib.org/3.1.1/_images/sphx_glr_custom_legends_003.png" width="450" height="300"/>

[composing_custom_legends-3.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/composing_custom_legends-3.py)

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], color='b', lw=4, label='Line'),
                   Line2D([0], [0], marker='o', color='w', label='Scatter',
                          markerfacecolor='g', markersize=15),
                   Patch(facecolor='orange', edgecolor='r',
                         label='Color Patch')]

# Create the figure
fig, ax = plt.subplots()
ax.legend(handles=legend_elements, loc='center')

plt.show()
```
#### [Pyplot Text](https://matplotlib.org/3.1.1/gallery/pyplots/pyplot_text.html#sphx-glr-gallery-pyplots-pyplot-text-py) <a name="pyplot_text"></a>

<img src="https://matplotlib.org/3.1.1/_images/sphx_glr_pyplot_text_001.png" width="450" height="300"/>

[pyplot_text.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/pyplot_text.py)

```python
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
```

#### [Using accented text in matplotlib](https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/accented_text.html#using-accented-text-in-matplotlib) <a name="using_accented_text_in_matplotlib"></a>

* Mathtext demo
<img src="https://matplotlib.org/3.1.1/_images/sphx_glr_accented_text_001.png" width="450" height="300"/>

* Unicode demo
<img src="https://matplotlib.org/3.1.1/_images/sphx_glr_accented_text_002.png" width="450" height="300"/>

[using_accented_text_in_matplotlib.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/using_accented_text_in_matplotlib.py)

```python
import matplotlib.pyplot as plt

# Mathtext demo
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_title(r'$\ddot{o}\acute{e}\grave{e}\hat{O}'
             r'\breve{i}\bar{A}\tilde{n}\vec{q}$', fontsize=20)

# Shorthand is also supported and curly braces are optional
ax.set_xlabel(r"""$\"o\ddot o \'e\`e\~n\.x\^y$""", fontsize=20)
ax.text(4, 0.5, r"$F=m\ddot{x}$")
fig.tight_layout()

# Unicode demo
fig, ax = plt.subplots()
ax.set_title("GISCARD CHAHUTÉ À L'ASSEMBLÉE")
ax.set_xlabel("LE COUP DE DÉ DE DE GAULLE")
ax.set_ylabel('André was here!')
ax.text(0.2, 0.8, 'Institut für Festkörperphysik', rotation=45)
ax.text(0.4, 0.2, 'AVA (check kerning)')

plt.show()
```

#### [Auto-wrapping text](https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/autowrap.html#sphx-glr-gallery-text-labels-and-annotations-autowrap-py) <a name="auto-wrapping_text"></a>

<img src="https://matplotlib.org/3.1.1/_images/sphx_glr_autowrap_001.png" width="450" height="300"/>

[auto-wrapping_text.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/auto-wrapping_text.py)

```python
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
```
The above example is hard to understand because all the texts are in a single figure. So each text is plotted in a figure below.

[auto-wrapping_text-custom.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/auto-wrapping_text-custom.py)

```python
import matplotlib.pyplot as plt

t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(4, 1, t, ha='left', rotation=15, wrap=True)

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(6, 5, t, ha='left', rotation=15, wrap=True)

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(5, 5, t, ha='right', rotation=-15, wrap=True)

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(5, 10, t, fontsize=18, style='oblique', ha='center', va='top', wrap=True)

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(3, 4, t, family='serif', style='italic', ha='right', wrap=True)

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(-1, 0, t, ha='left', rotation=-15, wrap=True)

plt.show()
```

<img src="https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/fig-auto-wrapping_text-4_1.png" width="450" height="300"/>

<img src="https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/fig-auto-wrapping_text-6_5.png" width="450" height="300"/>

<img src="https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/fig-auto-wrapping_text-5_5.png" width="450" height="300"/>

<img src="https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/fig-auto-wrapping_text-5_10.png" width="450" height="300"/>

<img src="https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/fig-auto-wrapping_text-3_4.png" width="450" height="300"/>

<img src="https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/fig-auto-wrapping_text--1_0.png" width="450" height="300"/>

#### [Simple axes labels](https://matplotlib.org/3.1.1/gallery/pyplots/fig_axes_labels_simple.html#sphx-glr-gallery-pyplots-fig-axes-labels-simple-py) <a name="simple_axes_labels"></a>

<img src="https://matplotlib.org/3.1.1/_images/sphx_glr_fig_axes_labels_simple_001.png" width="450" height="300"/>

[simple_axes_labels.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/text_labels_and_annotations/simple_axes_labels.py)

```python
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
```

(EOF)
