import numpy as np
# Dynamic model of the tank
def tank_dynamics(h, inFlow, A, k,t):
    """
    Computes the time derivative of the fluid level in the tank.

    Parameters:
    h (float): Current water level in the tank (m)
    inFlow (float): Inflow rate into the tank (m^3/s)
    A (float): Cross-sectional area of the tank (m^2)
    k (float): Flow coefficient (m^3/s)
    t (float): Current time (s)

    Returns:
    float: Time derivative of the fluid level (m/s) dh/dt
    """
    def disturbance(t):
        # Example disturbance: A sinusoidal disturbance with amplitude 0.1 m^3/s and frequency 0.1 Hz
        if t < 50: # No disturbance for the first 50 seconds
            return 0
        return 0.5
    
    # Outflow rate based on current water level
    outflow = k * (h ** 0.5)+ disturbance(t) # Outflow rate (m^3/s) outflow = k * sqrt(h)

    # Time derivative of the fluid level
    dh_dt = (inFlow - outflow) / A # Change in fluid level (m/s)

    return dh_dt