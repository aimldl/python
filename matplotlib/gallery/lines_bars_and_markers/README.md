## Matplotlib > Gallery > Lines, bars and markers > README.md
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
#### Simple Plotting
* [Simple Plot](#simple_plot)
* [Customizing dashed line styles](#customizing_dashed_line_styles)
* [Linestyles](#linestyles)
* [Masked Demo](#masked_demo)
* [Using span_where](#using_span_where)
* [hlines and vlines](#hlines_and_vlines)
* [Multicolored lines](#multicolored_lines)

#### For Digital Signal Processing
* [Stem Plot](#stem_plot)
* [Plotting the coherence of two signals](#plotting_coherence_of_two_signals)
* [Spectrum Representations](#spectrum_representations)
* [Cross- and Auto-Correlation Demo](#correlation_demo)
---
#### [Simple Plot](https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py) <a name="simple_plot"></a>

<img src="https://matplotlib.org/_images/sphx_glr_simple_plot_001.png" width="450" height="300"/>

[simple_plot.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/simple_plot.py)

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
Instead of ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks'),
```python
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
```
can be used.

#### [Customizing dashed line styles](https://matplotlib.org/gallery/lines_bars_and_markers/line_demo_dash_control.html#sphx-glr-gallery-lines-bars-and-markers-line-demo-dash-control-py)  <a name="customizing_dashed_line_styles"></a>

<img src="https://matplotlib.org/_images/sphx_glr_line_demo_dash_control_001.png" width="450" height="300" />

[customizing_dashed_line_styles.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/customizing_dashed_line_styles.py)

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
y = np.sin(x)

fig, ax = plt.subplots()

# Using set_dashes() to modify dashing of an existing line
line1, = ax.plot(x, y, label='Using set_dashes()')
line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break

# Using plot(..., dashes=...) to set the dashing when creating a line
line2, = ax.plot(x, y - 0.2, dashes=[6, 2], label='Using the dashes parameter')

ax.legend()
plt.show()
```

#### [Linestyles](https://matplotlib.org/gallery/lines_bars_and_markers/linestyles.html#sphx-glr-gallery-lines-bars-and-markers-linestyles-py) <a name="linestyles"></a>

<img src="https://matplotlib.org/_images/sphx_glr_linestyles_001.png" width="900" height="750" />

[linestyles.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/linestyles.py)

```python
import numpy as np
import matplotlib.pyplot as plt

linestyle_str = [
     ('solid', 'solid'),      # Same as (0, ()) or '-'
     ('dotted', 'dotted'),    # Same as (0, (1, 1)) or '.'
     ('dashed', 'dashed'),    # Same as '--'
     ('dashdot', 'dashdot')]  # Same as '-.'

linestyle_tuple = [
     ('loosely dotted',        (0, (1, 10))),
     ('dotted',                (0, (1, 1))),
     ('densely dotted',        (0, (1, 1))),

     ('loosely dashed',        (0, (5, 10))),
     ('dashed',                (0, (5, 5))),
     ('densely dashed',        (0, (5, 1))),

     ('loosely dashdotted',    (0, (3, 10, 1, 10))),
     ('dashdotted',            (0, (3, 5, 1, 5))),
     ('densely dashdotted',    (0, (3, 1, 1, 1))),

     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]


def plot_linestyles(ax, linestyles):
    X, Y = np.linspace(0, 100, 10), np.zeros(10)
    yticklabels = []

    for i, (name, linestyle) in enumerate(linestyles):
        ax.plot(X, Y+i, linestyle=linestyle, linewidth=1.5, color='black')
        yticklabels.append(name)

    ax.set(xticks=[], ylim=(-0.5, len(linestyles)-0.5),
           yticks=np.arange(len(linestyles)), yticklabels=yticklabels)

    # For each line style, add a text annotation with a small offset from
    # the reference point (0 in Axes coords, y tick value in Data coords).
    for i, (name, linestyle) in enumerate(linestyles):
        ax.annotate(repr(linestyle),
                    xy=(0.0, i), xycoords=ax.get_yaxis_transform(),
                    xytext=(-6, -12), textcoords='offset points',
                    color="blue", fontsize=8, ha="right", family="monospace")


fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 3]},
                               figsize=(10, 8))

plot_linestyles(ax0, linestyle_str[::-1])
plot_linestyles(ax1, linestyle_tuple[::-1])

plt.tight_layout()
plt.show()
```

#### [Masked Demo](https://matplotlib.org/gallery/lines_bars_and_markers/masked_demo.html#sphx-glr-gallery-lines-bars-and-markers-masked-demo-py) <a name="masked_demo"></a>

<img src="https://matplotlib.org/_images/sphx_glr_masked_demo_001.png" width="450" height="300" />

[masked_demo.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/masked_demo.py)

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.02)
y = np.sin(x)
y1 = np.sin(2*x)
y2 = np.sin(3*x)
ym1 = np.ma.masked_where(y1 > 0.5, y1)
ym2 = np.ma.masked_where(y2 < -0.5, y2)

lines = plt.plot(x, y, x, ym1, x, ym2, 'o')
plt.setp(lines[0], linewidth=4)
plt.setp(lines[1], linewidth=2)
plt.setp(lines[2], markersize=10)

plt.legend(('No mask', 'Masked if > 0.5', 'Masked if < -0.5'),
           loc='upper right')
plt.title('Masked line demo')
plt.show()
```
#### [Using span_where](https://matplotlib.org/gallery/lines_bars_and_markers/span_regions.html#sphx-glr-gallery-lines-bars-and-markers-span-regions-py) <a name="using_span_where"></a>

<img src="https://matplotlib.org/_images/sphx_glr_span_regions_001.png" width="450" height="300" />

[using_span_where.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/using_span_where.py)

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as collections

t  = np.arange(0.0, 2, 0.01)
s1 = np.sin(2*np.pi*t)
# This line exists in the example, but it's not used.
#s2 = 1.2*np.sin(4*np.pi*t)

fig, ax = plt.subplots()
ax.set_title('using span_where')
ax.plot(t, s1, color='black')       # Plot s1
ax.axhline(0, color='black', lw=2)  # Draw a horizontal line for y=0

# Green shady area is applied where s1>0
collection = collections.BrokenBarHCollection.span_where(
    t, ymin=0, ymax=1, where=s1 > 0, facecolor='green', alpha=0.5)
ax.add_collection(collection)

# Green shady area is applied where s1<0
collection = collections.BrokenBarHCollection.span_where(
    t, ymin=-1, ymax=0, where=s1 < 0, facecolor='red', alpha=0.5)
ax.add_collection(collection)

plt.show()
```
#### [hlines and vlines](https://matplotlib.org/gallery/lines_bars_and_markers/vline_hline_demo.html#sphx-glr-gallery-lines-bars-and-markers-vline-hline-demo-py) <a name="hlines_and_vlines"></a>

<img src="https://matplotlib.org/_images/sphx_glr_vline_hline_demo_001.png" width="720" height="480" />

[hlines_and_vlines.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/hlines_and_vlines.py)

```python
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

plt.show()
```

[hlines_and_vlines.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/hlines_and_vlines.py) includes the following line which adds two horizontal lines on the right figure.
```python
# I added the following line to draw two horizontal lines at y=1 & y=2
# Notice three changes:
#  (1) vax.vlines    -> hax.hlines,
#  (2) transform=vax -> transform.hax
#  (3) get_xaxis_... -> get_yaxis_...
hax.hlines([1, 2], 0, 1, transform=hax.get_yaxis_transform(), colors='r')
```
<img src="https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/fig-hlines_and_vlines.png" width="600" height="400" />

#### [Multicolored lines](https://matplotlib.org/gallery/lines_bars_and_markers/multicolored_line.html#sphx-glr-gallery-lines-bars-and-markers-multicolored-line-py) <a name="multicolored_lines"></a>

<img src="https://matplotlib.org/_images/sphx_glr_multicolored_line_001.png" width="450" height="300" />

[multicolored_lines.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/multicolored_lines.py)

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

x    = np.linspace(0, 3 * np.pi, 500)
y    = np.sin(x)
dydx = np.cos(0.5 * (x[:-1] + x[1:]))  # first derivative

# Create a set of line segments so that we can color them individually
# This creates the points as a N x 1 x 2 array so that we can stack points
# together easily to get the segments. The segments array for line collection
# needs to be (numlines) x (points per line) x 2 (for x and y)
points   = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)

# Create a continuous norm to map from data points to colors
norm = plt.Normalize( dydx.min(), dydx.max() )
lc   = LineCollection(segments, cmap='viridis', norm=norm)
# Set the values used for colormapping
lc.set_array(dydx)
lc.set_linewidth(2)
line = axs[0].add_collection(lc)
fig.colorbar(line, ax=axs[0])

# Use a boundary norm instead
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
lc   = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
line = axs[1].add_collection(lc)
fig.colorbar(line, ax=axs[1])

axs[0].set_xlim(x.min(), x.max())
axs[0].set_ylim(-1.1, 1.1)
plt.show()
```

#### [Stem Plot](https://matplotlib.org/gallery/lines_bars_and_markers/stem_plot.html#sphx-glr-gallery-lines-bars-and-markers-stem-plot-py) <a name="stem_plot"></a>

<img src="https://matplotlib.org/_images/sphx_glr_stem_plot_001.png" width="450" height="300" />

[stem_plot.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/stem_plot.py)

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))

plt.stem(x, y, use_line_collection=True)
plt.show()
```

<img src="https://matplotlib.org/_images/sphx_glr_stem_plot_002.png" width="450" height="300" />

```python
markerline, stemlines, baseline = plt.stem(x, y, linefmt='grey', markerfmt='D',
                                           bottom=1.1, use_line_collection=True)
markerline.set_markerfacecolor('none')
plt.show()
```

#### [Plotting the coherence of two signals](https://matplotlib.org/gallery/lines_bars_and_markers/cohere.html#sphx-glr-gallery-lines-bars-and-markers-cohere-py) <a name="plotting_coherence_of_two_signals"></a>

<img src="https://matplotlib.org/_images/sphx_glr_cohere_001.png" width="450" height="400" />

[plotting_coherence_of_two_signals.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/plotting_coherence_of_two_signals.py)

```python
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

dt   = 0.01    #  10ms, sampling interval
fs   = 1 / dt  # 100Hz, sampling frequency
t    = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

# Two signals with a coherent part at 10Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

# Plot
fig, axs = plt.subplots(2, 1)
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('time')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)

cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('coherence')

fig.tight_layout()
plt.show()
```
#### [Spectrum Representations](https://matplotlib.org/gallery/lines_bars_and_markers/spectrum_demo.html#sphx-glr-gallery-lines-bars-and-markers-spectrum-demo-py) <a name="spectrum_representations"></a>

<img src="https://matplotlib.org/_images/sphx_glr_spectrum_demo_001.png" width="800" height="500" />

[spectrum_representations.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/spectrum_representations.py)

```python
import matplotlib.pyplot as plt
import numpy as np

dt = 0.01    #  10ms, sampling interval
fs = 1 / dt  # 100Hz, sampling frequency
t = np.arange(0, 10, dt)

# Generate noise
np.random.seed(0)
nse  = np.random.randn(len(t))
r    = np.exp(-t / 0.05)
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]

# Generate signal
s = 0.1 * np.sin(4 * np.pi * t) + cnse

# Plot
fig, axes = plt.subplots( nrows=3, ncols=2, figsize=(7, 7) )

# Plot signal in time
axes[0, 0].set_title("Signal")
axes[0, 0].plot(t, s, color='C0')
axes[0, 0].set_xlabel("Time")
axes[0, 0].set_ylabel("Amplitude")

# Plot signal in frequency
#   plot different spectrum types
axes[1, 0].set_title("Magnitude Spectrum")
axes[1, 0].magnitude_spectrum(s, Fs=fs, color='C1')

axes[1, 1].set_title("Log. Magnitude Spectrum")
axes[1, 1].magnitude_spectrum(s, Fs=fs, scale='dB', color='C1')

axes[2, 0].set_title("Phase Spectrum ")
axes[2, 0].phase_spectrum(s, Fs=fs, color='C2')

axes[2, 1].set_title("Angle Spectrum")
axes[2, 1].angle_spectrum(s, Fs=fs, color='C2')

axes[0, 1].remove()  # Don't display empty ax

fig.tight_layout()
plt.show()
```

#### [Cross- and Auto-Correlation Demo](https://matplotlib.org/gallery/lines_bars_and_markers/xcorr_acorr_demo.html#sphx-glr-gallery-lines-bars-and-markers-xcorr-acorr-demo-py) <a name="correlation_demo"></a>

<img src="https://matplotlib.org/_images/sphx_glr_xcorr_acorr_demo_001.png" width="600" height="400" />

[cross-and_auto-correlation_demo.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/cross-and_auto-correlation_demo.py)

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.randn(2, 100)
fig, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax1.grid(True)

ax2.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax2.grid(True)

plt.show()
```

The above code doesn't display the two random variables. I modified to plot two random variables x & y in a separate subplot in  [cross-and_auto-correlation_demo.py](https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/cross-and_auto-correlation_demo.py). Note auto- & cross-correlation plots don't scale well with plt.plot(...) function. So I had to use a separate subplot to display x & y.
```python

# np.random.randn(2, 100) returns samples from the “standard normal” distribution.
#   array([[1.0493, 0.866099, ... ,  -1.27382],    # random stored in x
#         [-1.38774, 0.155221, ... , -0.492031]]) # random stored in y
t    = np.arange( 0, len(x) )  # len(x)=100

# Plot random variable x & y
fig, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
ax1.plot( t, x )
# t.max()=99, So add 1 to display 100 in the figure
ax1.set_xlim( t.min(), t.max()+1 )
ax1.set_ylim(-3, 3)
ax1.set_title('Random variable x')
ax1.grid()

ax2.plot( t, y )
ax2.set_xlim( t.min(), t.max()+1 )
ax2.set_ylim(-3, 3)
ax2.set_title('Random variable y')
ax2.grid()

plt.show()
```
<img src="https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/fig-cross-and_auto-correlation-1.png" width="450" height="300" />
<img src="https://github.com/aimldl/python3/blob/master/packages/matplotlib/gallery/lines_bars_and_markers/fig-cross-and_auto-correlation-2.png" width="450" height="300" />

(EOF)
