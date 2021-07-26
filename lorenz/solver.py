"""
This file contains the ODE solver
"""
import numpy as np

def ode_solver(f, c0, dt=0.01, N_t=50000): # ODE solver by simple Newton Euler algorithm

    T = N_t * dt
    f_ = lambda u, t: np.asarray(f(u, t))
    u = np.zeros((N_t + 1, len(c0)))
    t = np.linspace(0, N_t * dt, len(u))
    u[0] = c0
    for n in range(N_t):
        u[n + 1] = u[n] + dt * f_(u[n], t[n])
    return u, t
