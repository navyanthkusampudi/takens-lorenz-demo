# utils/lorenz_solver.py

def lorenz_system(t, state, sigma, beta, rho):
    """
    Lorenz system of ODEs.

    Parameters:
    - t: time variable (not used in the equations)
    - state: current state of the system [x, y, z]
    - sigma: Prandtl number
    - beta: geometric factor
    - rho: Rayleigh number

    Returns:
    - derivatives: list of derivatives [dx/dt, dy/dt, dz/dt]
    """
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]