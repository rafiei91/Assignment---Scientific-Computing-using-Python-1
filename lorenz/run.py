"""
This file contains the interface/function for
"""

from . import filehandling as fh
from . import plot
from . import solver

def execute(f, c0, case, s): # Execute ODE solver and call the saver and ploters

    u, t = solver.ode_solver(f, c0)

    x = u[:, 0]
    y = u[:, 1]
    z = u[:, 2]

    fh.save_data([x, y, z, t], case)
    plot.2D_plot(x, y, z, case, s)
    plot.plot3d(x, y, z, case, s)
