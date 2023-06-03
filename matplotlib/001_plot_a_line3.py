!#/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5],[1, 4, 9, 16, 25], 'ro')
plt.plot([1, 2, 3, 4, 5],[1, 4, 9, 16, 25], 'b-')
plt.axis([0,6,0,20])
plt.show()
