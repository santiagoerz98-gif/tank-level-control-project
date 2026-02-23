# Class PID 


class PID:
    def __init__(self, kp, ki, kd, dt=0.01,u_min=0, u_max=2):
        self.kp = kp # Proportional gain
        self.ki = ki # Integral gain
        self.kd = kd # Derivative gain
        self.dt = dt # Time step
        self.u_min = u_min # Minimum control output
        self.u_max = u_max # Maximum control output

        # Initialize integral and previous error for derivative calculation
        self.integral = 0
        self.previous_error = 0
    def update(self, measurement,setpoint):
        # Calculate error
        error = setpoint - measurement
        # Derivative term
        derivative = (error - self.previous_error) / self.dt
        # Non-saturated output
        unsat_output = self.kp * error + self.ki * self.integral + self.kd * derivative
        # Saturate output
        output = max(self.u_min, min(self.u_max, unsat_output))
        # Anti-windup: If output is saturated, prevent integral from increasing
        if output == unsat_output:
            self.integral += error * self.dt
        # Update previous error
        self.previous_error = error
        return output

