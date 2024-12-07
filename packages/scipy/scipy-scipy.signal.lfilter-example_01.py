"""
scipy-scipy.signal.lfilter-example_01.py

This is an example code for scipy.signal.lfilter
https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html

"""

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1,1,201)
x = (        np.sin( 2*np.pi*0.75*t*(1-t) + 2.1 ) 
     + 0.1 * np.sin( 2*np.pi*1.25*t + 1 )
     + 0.18* np.cos( 2*np.pi*3.85*t) )

# Add small Gaussian noise to x
xn = x + np.random.randn( len(t) ) * 0.08

# Create an order 3 lowpass butterworth filter
b, a = signal.butter(3,0.05)
print( "b = ", b )
print( "a = ", a )
# Apply the filter to xn.
# Use lfilter_zi to choose the initial condition of the filter

zi  = signal.lfilter_zi(b,a)
print( "xn[0] = ", xn[0] )
z,_ = signal.lfilter(b,a,xn,zi=zi*xn[0])

# Apply the filter again, to have a result filtered at an order the same as filtfilt
z2,_ = signal.lfilter(b,a,z,zi=zi*z[0])

# Use filtfilt to apply the filter
y = signal.filtfilt(b,a,xn)

# Plot the original signal and the various filtered versions
plt.figure
plt.subplot(221)
plt.plot(t,x,'k-')
plt.grid(True)
#plt.plot(t,xn,'b')
plt.plot(t,xn,'b',alpha=0.75)
plt.legend(('x','xn_0.75'))

plt.subplot(222)
plt.plot(t,x,'k-')
plt.plot(t,z,'r--')
plt.grid(True)
plt.title('lfilter once to xn')

plt.subplot(223)
plt.plot(t,x,'k-')
plt.plot(t,z2)
plt.grid(True)
plt.title('lfilter twice to xn')

plt.subplot(224)
plt.plot(t,x,'k-')
plt.plot(t,y)
plt.grid(True)
plt.title('filtfilt to xn')
