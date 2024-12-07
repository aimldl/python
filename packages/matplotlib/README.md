* 2021-03-04 (Thu)
* 2020-09-01 (Tue)

# Matplotlib for Python
## 1. Overview
Matplotlib is a Python library to plot like Matlab. https://matplotlib.org/ provides nice learning materials. To import matplotlib, use:
```python
import matplotlib.pyplot as plt
```
To embed the plot in a Jupyter Notebook, add:
```python
%matplotlib inline
```
## 2. Installation
### Google Colab
* Matploblib is built into Google Colab.
* So installation is not necessary.

### Local environment
* Install [Anaconda](https://www.anaconda.com/) and Matplotlib comes automatically with Anaconda.
* For details, refer to [Install Matplotlib](INSTALL.md)

## 3. Examples
Refer to [Examples](https://matplotlib.org/gallery/index.html) to see what's possible with matplotlib.
> This gallery contains examples of the many things you can do with Matplotlib.

I have selected several useful examples in [Summary of Matplotlib Gallery](gallery/summary-matplotlib-gallery.md) and added brief comments if necessary.

### Selected Python Code Examples
matplotlib must be imported to use it. To plot [Simple Plot Example](gallery/lines_bars_and_markers#simple_plot), 
<img src="https://matplotlib.org/_images/sphx_glr_simple_plot_001.png" width="450" height="300"/>

```python
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
# Plot
fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
ax.grid()
fig.savefig("test.png")
plt.show()
```

Another example to use Line2D is from [Composing Custom Legends](https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/custom_legends.html#sphx-glr-gallery-text-labels-and-annotations-custom-legends-py):

<img src="https://matplotlib.org/3.1.1/_images/sphx_glr_custom_legends_002.png" width="450" height="300" />

```python
from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
```
## 4. Learning Materials
### 4.1. Tutorials
* [Pyplot tutorial](https://matplotlib.org/tutorials/introductory/pyplot.html)
* [Tutorials](https://matplotlib.org/3.1.1/tutorials/index.html)
* [Matplotlib Tutorial – A Complete Guide to Python Plot w/ Examples](https://www.machinelearningplus.com/plots/matplotlib-tutorial-complete-guide-python-plot-examples/), Selva Prabhakaran, January 22, 2019

### 4.2. Documentation
* [User's Guide](https://matplotlib.org/users/index.html)
* [Documentation overview](https://matplotlib.org/contents.html). 
* Github Repository: [matplotlib](https://github.com/matplotlib) / [cheatsheets](https://github.com/matplotlib/cheatsheets)
