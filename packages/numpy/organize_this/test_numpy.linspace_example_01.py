"""
test_numpy.linspace_example_01.py
This is an example code for numpy.linspace
https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html

"""

import numpy as np
import matplotlib.pyplot as plt

np.linspace(2.0,3.0, num=5)
np.linspace(2.0,3.0, num=5, endpoint=False)
np.linspace(2.0,3.0, num=5, retstep=True)

N = 8
y = np.zeros(N)
x1 = np.linspace(0,10,N, endpoint=True)
x2 = np.linspace(0,10,N, endpoint=False)
plt.plot(x1,y,'o')
plt.plot(x2,y+0.5, 'o')
plt.ylim([-0.5,1])
plt.show()