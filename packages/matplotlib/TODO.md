##### aimldl/python3/packages/matplotlib/TODO.md
* Draft: 2020-0318 (Wed)
# TODO
* Summarize the commands in the following example and let them alreadily available.
```python
# Telco Customer Churn Problem
# EDA
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,1)
ax[0].hist( df['MonthlyCharges'], bins=25 )
ax[0].grid()
ax[0].set_title( 'MonthlyCharges' )
ax[0].set_xlabel( 'USD' )
ax[0].set_ylim( [0, 2000] )

ax[1].hist( df['TotalCharges'], bins=25 )
ax[1].grid()
ax[1].set_title( 'TotalCharges' )
ax[1].set_xlabel( 'USD' )
ax[1].set_ylim( [0, 2000] )

fig.tight_layout()
```

* Work on the following example in the gallery.
```python
import matplotlib.pyplot as plt
import numpy as np

data = ((3, 1000), (10, 3), (100, 30), (500, 800), (50, 1))

dim = len(data[0])
w = 0.75
dimw = w / dim

fig, ax = plt.subplots()
x = np.arange(len(data))
for i in range(len(data[0])):
    y = [d[i] for d in data]
    b = ax.bar(x + i * dimw, y, dimw, bottom=0.001)

ax.set_xticks(x + dimw / 2, map(str, x))
ax.set_yscale('log')

ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()
```
