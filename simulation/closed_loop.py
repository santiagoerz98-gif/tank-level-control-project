import numpy as np
import matplotlib.pyplot as plt
from model.tank import tank_dynamics
from control.pid import PID


def closed_loop_simulation(h0, kp, ki, kd, dt=0.1, t_final=100,A=1.5,k=0.5):
    """
    Simulates the closed-loop control of the tank level using a PID controller.

    Parameters:
    h0 (float): Initial level in the tank (m)
    kp (float): Proportional gain
    ki (float): Integral gain
    kd (float): Derivative gain
    dt (float): Time step for the simulation (s)
    t_final (float): Final time for the simulation (s)

    Returns:
    np.ndarray: Array of water levels at each time step
    np.ndarray: Array of time points corresponding to the levels
    """
    def setpoint(t):
        if t > 40:
            return 5
        return 5

    t = np.arange(0, t_final, dt) # Time array
    h = np.zeros_like(t) # Array to store tank levels
    h[0] = h0 # Set initial level
    Fin_values = np.zeros_like(t) # Array to store control inputs (inflow)
    setpoint_values = np.zeros_like(t) # Array of setpoint values for plotting

    # Initialize PID controller
    pid = PID(kp, ki, kd, dt=dt)

    for i in range(1, len(t)):
        setpoint_values[i] = setpoint(t[i]) # Store setpoint value for plotting
        Fin = pid.update(h[i-1], setpoint_values[i]) # Get control input from PID controller
        Fin = max(0, Fin) # Ensure control input (inflow) is non-negative
        Fin_values[i] = Fin # Store control input for analysis
        
        # Simulate tank dynamics with control input as inflow
        dh_dt = tank_dynamics(h[i-1], Fin, A, k,t[i]) # Get dh/dt
        h[i] = h[i-1] + dh_dt * dt # Update level using Euler's method

        if h[i] < 0: # Ensure level does not go negative
            h[i] = 0 # Set level to zero if negative

    return h, t, Fin_values, setpoint_values