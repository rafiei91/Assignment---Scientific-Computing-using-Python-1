"""
This file contains the interface/function for

1: computing a trajectory using an ODE solver from solver.py
2: save data to file
3: plot data

"""
from . import filehandling as fh
from . import plot
from . import solver


def simulate(f, U_0, name, s):
    """
    Interfacing function for executing different scenarios.

    INPUT::

     f: ODE function in the form of f(X,t). X can be an array of the form [a, b, c ...]
     U_0: initial condition. U_0 = [a0, b0, c0, ...]
     name: name of the file

    OUPUT::

    """

    u, t = solver.ode_solver(f, U_0)

    x = u[:, 0]
    y = u[:, 1]
    z = u[:, 2]

    fh.save_data([x, y, z, t], name)
    plot.plot2d(x, y, z, name, s)
    plot.plot3d(x, y, z, name, s)
