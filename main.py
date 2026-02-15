from model import tank_dynamics
import numpy as np
from simulation import simulate_tank_level, ode_tank_solution
import matplotlib.pyplot as plt


# Tank model parameters
A = 1.5 # Cross-sectional area of the tank (m^2)
k = 0.5 # Flow coefficient (m^3/s)
g = 9.81 # Acceleration due to gravity (m/s^2)
h0 = 0.5 # Initial water level in the tank (m)
inFlow = 0.5 # Inflow rate into the tank (m^3/s)

# for inFlow in [0.3,0.5, 0.7, 1]: # Different inflow rates (m^3/s)
#     h, t = simulate_tank_level(h0, inFlow, dt=0.1, t_final=100,A=A, k=k) # Simulate tank level over time
#     plt.plot(t, h, label=f"inFlow={inFlow} m^3/s")

h, t = simulate_tank_level(h0, inFlow, dt=0.1, t_final=100,A=A, k=k) # Simulate tank level over time
plt.plot(t, h, label=f"inFlow={inFlow} m^3/s")

# Compare with ODE solution
h_ode, t_ode = ode_tank_solution(h0, inFlow, A, k)
plt.plot(t_ode, h_ode, label="Tank Level (ODE Solution)", linestyle='--')

# Graph the results
plt.xlabel("Time (s)")
plt.ylabel("Tank Level (m)")
plt.title("Tank Response for ODE Solution vs Numerical Simulation")
plt.legend()
plt.grid(True)
plt.show()
