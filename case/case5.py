"""
This file could contain the necessary calls to make plots etc for case 5
"""

import sys
sys.path.append('../')
import os
import lorenz

def ode_lorenz_attractor(X, t): # Defining the ODE functions, initial conditions and case parameters, and calling the solver
    
    x, y, z = X

    delta = 14
    beta = 13 / 3
    rho = 28

    dxdt = delta * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z

    return [dxdt, dydt, dzdt]

if os.path.exists('case5') is False:
    os.mkdir('case5')

c0 = [-1,-1,20]    # Initial Conditions
f = ode_lorenz_attractor   # ODE

lorenz.run.execute(f,c0,'case5',False)
