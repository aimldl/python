import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cvx

f = np.array( [1,1] )
A = np.array( [[2,1], [1,2]] )
b = np.array( [[29],[25]] )
lb = np.array( [[2],[5]] )

x = cvx.Variable(2,1)

objective = cvx.Minimize( -f*x )
constraints = [ A*x <=b, lb <=x ]

prob = cvx.Problem( objective, contraints )
result = prob.solve()

print(x.value)
print(result)

   # A = np.array( [2,1], [1,2] )
# => A = np.array( [[2,1], [1,2]] )
# Traceback (most recent call last):
  # File "cvxpy-example-linear_programming-01.py", line 6, in <module>
    # A = np.array( [2,1], [1,2] )
# TypeError: data type not understood