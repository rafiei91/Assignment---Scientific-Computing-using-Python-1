"""
In this file you may have your tests


"""
import sys
sys.path.append('../')

import unittest
from scipy.integrate import solve_ivp
import numpy as np

import lorenz


def ode_lorenz_attractor1(X, t):
    # Define parameter
    x, y, z = X

    # Case 1
    delta = 10
    beta = 8 * (1 / 3)
    rho = 6

    dxdt = delta * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z

    # the function returns the vector [dxdt, dydt, dzdt]
    return [dxdt, dydt, dzdt]


def ode_lorenz_attractor2(t, X):
    # Define parameter
    x = X[0]
    y = X[1]
    z = X[2]

    # Case 1
    delta = 10
    beta = 8 * (1 / 3)
    rho = 6

    dxdt = delta * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z

    # the function returns the vector [dxdt, dydt, dzdt]
    return [dxdt, dydt, dzdt]


class TestMethod(unittest.TestCase):

    # def test_up(self):
    #    self.assertEqual('foo'.upper(), 'FOo')

    # def test_isupper(self):
    #    self.assertTrue('FOO'.isupper())
    #    self.assertFalse('Foo'.isupper())

    def test_solver(self):
        # Using Scipy solver
        U_0 = [-1, -1, 20]
        dt = 0.01
        N = 50001
        T = N * dt

        sol = solve_ivp(ode_lorenz_attractor2, y0=U_0, t_span=[0, T], t_eval=np.arange(0, T, dt))
        x1 = sol.y[0]
        y1 = sol.y[1]
        z1 = sol.y[2]

        # Using own solver implementation
        f = ode_lorenz_attractor1
        u, t = lorenz.solver.ode_solver(f, U_0)

        x2 = u[:, 0]
        y2 = u[:, 1]
        z2 = u[:, 2]

        assert np.allclose(x1, x2, rtol=1e1, atol=1e1)
        assert np.allclose(y1, y2, rtol=1e1, atol=1e1)
        assert np.allclose(z1, z2, rtol=1e1, atol=1e1)
