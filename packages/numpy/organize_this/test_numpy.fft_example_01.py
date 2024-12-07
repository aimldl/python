"""
test_numpy.fft_example_01.py

This is an example code for numpy.fft.fft
https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html#numpy.fft.fft

More in general, Discrete Fourier Transform (numpy.fft)
https://docs.scipy.org/doc/numpy/reference/routines.fft.html

>>> np.arange(8)
array([0, 1, 2, 3, 4, 5, 6, 7])

when x=0, a=1,
        ...
     x=8, e^2(pi)j
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(8)
a = np.exp( 2j*np.pi * x/8 )
plt.plot( a )
np.fft.fft( a )

t = np.arange(256)
#array([0, 1, 2, ... , 254, 255])
sp = np.fft.fft( np.sin(t) )
freq = np.fft.fftfreq( t.shape[-1] )
plt.plot( freq, sp.real, freq, sp.imag )
plt.show()

"""
In this example, real input has an FFT which is Hermitian,
i.e., symmetric in the real part and anti-symmetric in the imaginary part,
as described in the numpy.fft documentation:
"""

plt.figure()

plt.subplot(211)
plt.title("Real part")
plt.plot( freq, sp.real )
plt.grid(True)
plt.axis([-0.5,0.5,-100,100])
plt.ylabel("?")

plt.subplot(212)
plt.title("Imagenary part")
plt.plot( freq, sp.imag )
plt.grid(True)

plt.axis([-0.5,0.5,-100,100])
plt.xlabel("?")
plt.ylabel("?")

#plt.title("Spectrum of r'$e^(2\pij*x/8)$'")

