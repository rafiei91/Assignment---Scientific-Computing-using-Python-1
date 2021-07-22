"""
This file contains the necessary calls to make plots etc for case 1
"""

import sys
import os
import lorenz

delta = 10
beta = 8 * (1 / 3)
rho = 6

if os.path.exists('case1') is False:
    os.mkdir('case1')

U_0 = [-1,-1,20]    # Initial Conditions
f = Lorenz_a   # ODE

sys.path.append('../')

lorenz.run.simulate(f,U_0,'case1',False)
