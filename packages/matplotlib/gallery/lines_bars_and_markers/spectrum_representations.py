#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lines_bars_and_markers/spectrum_representations.py

Matplotlib > Gallery > Lines, bars and markers > Spectrum Representations
https://matplotlib.org/gallery/lines_bars_and_markers/stem_plot.html#sphx-glr-gallery-lines-bars-and-markers-stem-plot-py
"""

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
