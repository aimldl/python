"""
test_numpy.hamming_example_02.py
This is an example code for numpy.hamming
https://docs.scipy.org/doc/numpy/reference/generated/numpy.hamming.html
"""

from numpy.fft import fft, fftshift
import numpy as np
import matplotlib.pyplot as plt

# Part 1: Hamming Window in Time 
#   Create and plot the Hamming Window (in the time domain)
window = np.hamming(51)
plt.plot(window)
#[<matplotlib.lines.Line2D object at 0x7f199c027630>]
plt.title("Hamming Window")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.show()

# Part 2: Hamming Window in Frequency
#   Apply FFT to the generated Hamming Window &
#   plot the figure to see the Hammin Window (in the frequency domain)
A = fft(window, 2048) / 25.5  # Amplitude
A_shifted = fftshift(A) 
mag = np.abs( A_shifted )
freq = np.linspace( -0.5,0.5, len(A) )
response = 20 * np.log10( mag )
response = np.clip( response, -100,100 )

plt.figure()
plt.plot( freq,response )
plt.title("Frequency response of Hamming Window")
plt.xlabel("Magnitude [dB]")
plt.ylabel("Normalized Frequency [cycles per sample]")
plt.axis('tight')
plt.show()