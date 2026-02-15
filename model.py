
# Dynamic model of the tank
def tank_dynamics(h, inFlow, A, k):
    """
    Computes the time derivative of the fluid level in the tank.

    Parameters:
    h (float): Current water level in the tank (m)
    Fin (float): Inflow rate into the tank (m^3/s)

    Returns:
    float: Time derivative of the fluid level (m/s) dh/dt
    """
    # Outflow rate based on current water level
    outflow = k * (h ** 0.5) # Outflow rate (m^3/s) outflow = k * sqrt(h)

    # Time derivative of the fluid level
    dh_dt = (inFlow - outflow) / A # Change in fluid level (m/s)

    return dh_dt