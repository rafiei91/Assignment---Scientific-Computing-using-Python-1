"""
This file could contain the necessary calls to make plots etc for 
case 2

"""
import sys
sys.path.append('../')
import os
import lorenz

def ode_lorenz_attractor1(X, t):
    # Define parameter
    x, y, z = X

    # Case 2
    delta = 10
    beta = 8 * (1 / 3)
    rho = 16

    dxdt = delta * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z

    # the function returns the vector [dxdt, dydt, dzdt]
    return [dxdt, dydt, dzdt]

if os.path.exists('case2') is False:
    os.mkdir('case2')

U_0 = [-1,-1,20]    # Initial Conditions
f = ode_lorenz_attractor1   # ODE

lorenz.run.simulate(f,U_0,'case2',False)
