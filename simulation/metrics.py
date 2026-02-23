import numpy as np

# Calcualte overshoot
def calculate_overshoot(h, setpoint):
    h_max = np.max(h) # Maximum level reached
    overshoot = (h_max - setpoint)/setpoint * 100 # Calculate overshoot as a percentage
    return max(0, overshoot) # Ensure overshoot is non-negative

# Calculate settling time
def calculate_settling_time(h, t, setpoint, tolerance=0.02):
    lower_bound = setpoint * (1 - tolerance) # Lower bound of acceptable range
    upper_bound = setpoint * (1 + tolerance) # Upper bound of acceptable range
    for i in range(len(h)):
        if np.all((h[i:] >= lower_bound) & (h[i:] <= upper_bound)): # Check if all subsequent values are within bounds
            return t[i] # Return the time at which the system settles within the tolerance
    return None # Return None if the system never settles within the tolerance
# Compute steady-state error
def calculate_steady_state_error(h, setpoint):
    steady_state_value = h[-1] # Final value of the response
    error = setpoint - steady_state_value # Calculate error
    return error

# Calculate integral of absolute error (IAE)
def compute_iae(t, h, sp_history):
    error = np.abs(sp_history - h) # Absolute error at each time step
    iae = np.trapezoid(error, t) # Integrate error over time using trapezoidal rule
    return iae