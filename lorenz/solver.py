"""
This file contains the ODE solver

"""
import numpy as np


def ode_solver(f, U_0, dt=0.01, T=50000 * 0.01):
    """
    This function contains the ODE solver. It implements a simple Newton Euler algorithm.

    INPUT::

     f: ODE function in the form of f(X,t). X can be an array of the form [a, b, c ...]
     U_0: initial condition. U_0 = [a0, b0, c0, ...]
     dt: time step for discretizing the ODE
     T: end time of the simulation (N*dt) where N describes the number of timesteps

    OUPUT::
     u: solution of the ODE e.g. u[0] = a, u[1] = b etc.
     t: time array

    """

    N_t = int(round(float(T) / dt))
    # Ensure that any list/tuple returned from f_ is wrapped as array
    f_ = lambda u, t: np.asarray(f(u, t))
    u = np.zeros((N_t + 1, len(U_0)))
    t = np.linspace(0, N_t * dt, len(u))
    u[0] = U_0
    for n in range(N_t):
        u[n + 1] = u[n] + dt * f_(u[n], t[n])
    return u, t
