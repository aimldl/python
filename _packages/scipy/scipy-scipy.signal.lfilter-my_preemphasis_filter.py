"""
scipy-scipy.signal.lfilter-my_preemphasis_filter.py

This is an example code for scipy.signal.lfilter
https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html

This is an example to create a preemphasis filter
y[n]=x[n]-0.97x[n-1]

"""

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1,1,201)
x = np.sin( 2*np.pi*0.75*t + 1.0 )

plt.figure
plt.subplot(211)
plt.plot(t,x,'k-')
plt.grid(True)
# Input signal
plt.title('sin(2*pi*0.75*t+1.0)')


b = [1., -0.97]
a = [1.]
y = signal.lfilter(b, a, x)
# y[n] = x[n] - 0.97 x[n-1]

plt.subplot(212)
plt.plot(t,y,)
plt.grid(True)
# Filtered signal
plt.title('y[n]=x[n]-0.97x[n-1]')
