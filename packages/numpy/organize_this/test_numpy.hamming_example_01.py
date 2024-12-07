"""
test_numpy.hamming_example_01.py
This is an example code for numpy.hamming
https://docs.scipy.org/doc/numpy/reference/generated/numpy.hamming.html
"""

from numpy.fft import fft, fftshift
import numpy as np
import matplotlib.pyplot as plt

window = np.hamming(51)
plt.plot(window)
#[<matplotlib.lines.Line2D object at 0x7f199c027630>]
plt.title("Hamming Window")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.show()
