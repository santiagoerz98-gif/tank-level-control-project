import numpy as np
from model.tank import tank_dynamics
from scipy.integrate import solve_ivp

def simulate_tank_level(h0, inFlow, dt=0.1, t_final=100,A=1.5,k=0.5):
    """
    Simulates the tank level over time given initial conditions and inflow.

    Parameters:
    h0 (float): Initial level in the tank (m)
    inFlow (float): constant inflow rate into the tank (m^3/s)
    time_steps (int): Number of time steps for the simulation
    t_final (float): Final time for the simulation (s)

    Returns:
    np.ndarray: Array of water levels at each time step
    """
    t = np.arange(0, t_final, dt) # Time array
    h_levels = np.zeros_like(t) # Array to store tank levels
    h_levels[0] = h0 # Set initial level

    for i in range(1, len(t)):
        dh_dt = tank_dynamics(h_levels[i-1], inFlow, A, k) # Get dh/dt
        h_levels[i] = h_levels[i-1] + dh_dt * dt # Update level using Euler's method

        if h_levels[i] < 0: # Ensure level does not go negative
            h_levels[i] = 0 # Set level to zero if negative

    return h_levels,t 

# Solve the tank level using an ODE solver for comparison
def ode_tank_solution(h0, inFlow, A, k):

    def tank_ode(t, h):
        return (inFlow-np.sqrt(h)*k)/A

    t_span = (0, 100) # Time span for the simulation
    t_eval = np.arange(0, 100, 0.1) # Time points to evaluate the solution

    sol = solve_ivp(tank_ode, t_span, [h0], t_eval=t_eval)

    return sol.y[0], sol.t
