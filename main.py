import matplotlib.pyplot as plt
from simulation.closed_loop import closed_loop_simulation
from simulation.open_loop import simulate_tank_level, ode_tank_solution
from simulation.metrics import calculate_overshoot, calculate_settling_time, calculate_steady_state_error, compute_iae

# Tank model parameters
A = 1.5 # Cross-sectional area of the tank (m^2)
k = 0.5 # Flow coefficient (m^3/s)
g = 9.81 # Acceleration due to gravity (m/s^2)
h0 = 0 # Initial water level in the tank (m)
dt = 0.1 # Time step for simulation (s)

# Closed-loop control parameters
kp = 1 # Proportional gain
ki = kp/5 # Integral gain
kd = 2*ki # Derivative gain

# Simulate closed-loop control
h_cl, t_cl, Fin_values, setpoint_values = closed_loop_simulation(h0, kp, ki, kd, dt=0.1, t_final=100, A=A, k=k)
# Calculate performance metrics
overshoot = calculate_overshoot(h_cl, setpoint_values[-1])
settling_time = calculate_settling_time(h_cl, t_cl, setpoint_values[-1])
steady_state_error = calculate_steady_state_error(h_cl, setpoint_values[-1])
iae = compute_iae(t_cl, h_cl, setpoint_values)
print(f"Overshoot: {overshoot:.2f}%")
print(f"Settling Time: {settling_time:.2f} seconds")    
print(f"Steady-State Error: {steady_state_error:.2f} m")
print(f"Integral of Absolute Error (IAE): {iae:.2f} m*s")
# Combined plot
fig, ax1 = plt.subplots(2, 1, sharex=True)
# Tank level plot
ax1[0].plot(t_cl, h_cl, label='Tank Level (h)', color='blue')
ax1[0].plot(t_cl, setpoint_values, color='red', linestyle='--', label='Setpoint')
ax1[0].set_title('Closed-Loop Control of Tank Level')
ax1[0].set_ylabel('Level (m)')
ax1[0].legend()
ax1[0].grid()
# Control input plot
ax1[1].plot(t_cl, Fin_values, label='Control Input (Fin)', color='green')
ax1[1].set_title('Control Input Over Time') 
ax1[1].set_xlabel('Time (s)')
ax1[1].set_ylabel('Inflow Rate (m^3/s)')
ax1[1].legend()
ax1[1].grid()
plt.show()  



