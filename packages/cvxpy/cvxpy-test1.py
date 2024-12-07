#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cvx

#f = np.array( [[1, 4]] )
f = np.array( [[1], [4]] )
H = np.array( [[1,0],[0,4]])
A = np.array( [[-2, -4],[1, 5 ],[2, 2]] )
b = np.array( [[-35],[50],[40]] )
lb = np.array( [[0],[0]] )

x = cvx.Variable( 2,1 )
objective = cvx.Minimize( cvx.quad_form(x, H) + f.T*x )
constraints = [A*x <=b, lb <=x]

prob = cvx.Problem(objective, constraints)
result = prob.solve()

print( x.value )
print( result )