"""
test_numpy.fftfreq_example_01.py

This is an example code for numpy.fft.fftshift
https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fftfreq.html#numpy.fft.fftfreq

More in general, Discrete Fourier Transform (numpy.fft)
https://docs.scipy.org/doc/numpy/reference/routines.fft.html
"""

import numpy as np

# Part 1: As is given in the example
signal = np.array( [-2, 8, 6, 4, 1, 0, 3, 5], dtype=float )
fourier = np.fft.fft( signal )
n = signal.size
timestep = 0.1
freq = np.fft.fftfreq(n, d=timestep)
print( freq )

# Part 2: I've added some more lines to visualize what's going on here.
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(211)
plt.plot( signal )
plt.grid(True)
plt.title("Signal in Time Domain ")

plt.subplot(212)
plt.plot( abs(fourier) )
plt.grid(True)
plt.title("Amplitude of the Signal in Frequency Domain ")