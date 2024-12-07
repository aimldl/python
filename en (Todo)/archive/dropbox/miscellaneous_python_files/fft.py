
# 05-02 FFT 기본; 파이썬(python)으로 FFT 해석하고 그래프 그리기
# Q. 파이썬에서 FFT를 하고 amplitude, phase 그래프를 어떻게 그리지?
# A. numpy.fft.fft(), abs(), angle() 함수를 써보자.
# https://techreviewtips.blogspot.com/2017/11/05-02-fft.html

import matplotlib.pyplot as plt
import numpy as np
import math

# Create a signal
fs = 2000   # Hz
T = 1/fs
t_max = 0.05 # sec
t = np.arange(0, t_max, T)

x = 0.6 * np.cos( 2*np.pi*t + np.pi/2) + np.cos( 2*np.pi*120*t)
y = x

# Plot the signal
plt.figure(num=1, dpi=100, facecolor='white')
plt.plot(t, y, 'r')
plt.xlabel('time (sec)')
plt.ylabel('y')
plt.savefig('./test_figure1_dpi_300.png', dpi=300)

# FFT (Fast Fourier Transform) of the signal
n = len(y)
num_fft = n
k = np.arange(num_fft)
f0 = k*fs/num_fft  # Double sides freq range
f0 = f0[range( math.trunc(num_fft/2) )]

Y = np.fft.fft(y) / num_fft  # FFT & normalization
Y = Y[ range( math.trunc(num_fft/2)) ]  # Single sided freq range
amplitute_hz = 2*abs(Y)
phase_angle = np.angle(Y)*180 / np.pi

# Plot the FFT of the signal
plt.figure(num=2, dpi=100, facecolor='white')
plt.subplots_adjust(hspace=0.6, wspace=0.3)

plt.subplot(3, 1, 1)
plt.plot(t, y, 'r')
plt.title('Signal Analysis with FFT')
plt.xlabel('time(sec)')
plt.ylabel('y')

plt.subplot(3, 1, 2)
plt.plot(f0, amplitute_hz, 'r')
plt.xlim(0, 200)
plt.ylim(0, 1.2)
plt.xlabel('Freq (Hz)')
plt.ylabel('Amplitude')
plt.xticks( np.arange(0,500,20) )
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(f0, phase_angle, 'r')
plt.xlim(0, 200)
plt.ylim(-180, 180)
plt.xlabel('Freq (Hz)')
plt.ylabel('Phase (degree)')
plt.xticks( [0, 60, 120, 200] )
plt.yticks( [-180, -90, 0, 90, 180] )
plt.grid()

# Save the figure.
plt.savefig('./test_fig2.png', dpi=300)

# Show the figure.
# "Enalble X11 forwarding" must be checked for ssh
plt.show()
