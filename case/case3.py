"""
This file could contain the necessary calls to make plots etc for case 3
"""

import sys
sys.path.append('../')
import os
import lorenz

def ode_lorenz_attractor(X, t): # Defining the ODE functions, initial conditions and case parameters, and calling the solver
    
    x, y, z = X

    delta = 10
    beta = 8 / 3
    rho = 28

    dxdt = delta * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z

    return [dxdt, dydt, dzdt]

if os.path.exists('case3') is False:
    os.mkdir('case3')

c0 = [8, 8, 24]    # Initial Conditions
f = ode_lorenz_attractor   # ODE

lorenz.run.execute(f,c0,'case3',False)
