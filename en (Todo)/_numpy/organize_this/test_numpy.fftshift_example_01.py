"""
test_numpy.fftshift_example_01.py

This is an example code for numpy.fft.fftshift
https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fftshift.html#numpy.fft.fftshift

More in general, Discrete Fourier Transform (numpy.fft)
https://docs.scipy.org/doc/numpy/reference/routines.fft.html
"""

import numpy as np

freqs = np.fft.fftfreq(10,0.1)
freqs
#array([ 0.,  1.,  2.,  3.,  4., -5., -4., -3., -2., -1.])

# Shift the zero-frequency component to the center of the spectrum.
np.fft.fftshift( freqs )
#array([-5., -4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.])

# Shift the zero-frequency component only along the second axis

freqs = np.fft.fftfreq( 9, d=1./9)
freqs
#array([ 0.,  1.,  2.,  3.,  4., -4., -3., -2., -1.])

freqs_reshaped = np.fft.fftfreq( 9, d=1./9).reshape(3,3)
freqs_reshaped
#array([[ 0.,  1.,  2.],
#       [ 3.,  4., -4.],
#       [-3., -2., -1.]])

np.fft.fftshift( freqs_reshaped, axes=(1,) )
#array([[ 2.,  0.,  1.],
#       [-4.,  3.,  4.],
#       [-1., -3., -2.]])