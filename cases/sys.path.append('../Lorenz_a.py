def Lorenz_attractor(X, t, delta, beta, rho):
    # Define parameter
    x, y, z = X

    dxdt = delta * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z

    # the function returns the vector [dxdt, dydt, dzdt]
    return [dxdt, dydt, dzdt]
