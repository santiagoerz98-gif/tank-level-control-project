# Tank Level Control with PID (Nonlinear Simulation)

## 📌 Overview

This project implements a nonlinear dynamic simulation of a tank level control system using a PID controller in Python.

The objective is to model a realistic closed-loop process including:

- Nonlinear process dynamics
- Actuator saturation
- Anti-windup compensation
- Setpoint tracking
- Disturbance rejection
- Quantitative performance metrics

---

## 🧮 Process Model

The tank dynamics are described by:

[
\frac{dh}{dt} = \frac{F_{in} - k\sqrt{h}}{A}
]

Where:

- (h) = liquid level
- (F\_{in}) = manipulated inlet flow
- (k\sqrt{h}) = nonlinear outlet flow
- (A) = tank cross-sectional area

This represents a nonlinear first-order system commonly found in process industries.

---

## 🎛 Control Architecture

Closed-loop configuration:

```
Setpoint → PID Controller → Saturation (Valve) → Tank → Measurement → PID
```

### Implemented Features

- Proportional, Integral, Derivative terms
- Actuator saturation limits
- Anti-windup mechanism
- Variable setpoint function
- External disturbance injection

---

## 📊 Performance Metrics

The project computes automatically:

- Overshoot (%)
- Settling time (±2%)
- Steady-state error
- Integral Absolute Error (IAE)

Example output:

```
Overshoot: 6.8%
Settling Time: 41.3 s
Steady-State Error: 0.0003
IAE: 11.9
```

---

## 🔬 Experiments Included

### 1. Open-loop response

Baseline process behavior without control.

### 2. Closed-loop PID control

Stabilization to a fixed setpoint.

### 3. Setpoint tracking

Step change in reference level.

### 4. Disturbance rejection

Step increase in outlet flow.

### 5. Anti-windup comparison

With and without integrator protection.

---

## 📁 Project Structure

```
model/
    tank.py              # Nonlinear tank model

control/
    pid.py               # PID controller with saturation & anti-windup

simulation/
    closed_loop.py       # Simulation engine
    open_loop

main.py                  # Runs experiments and metrics
```

---

## 🚀 How to Run

```bash
pip install numpy scipy matplotlib
python main.py
```

---

## 📈 Future Improvements

- Automatic tuning (Ziegler-Nichols / IMC)
- Sensor noise modeling
- Derivative filtering
- Robustness analysis
- Model predictive control (MPC) extension

---

## 🎯 Learning Goals

This project helped me understand the practical implementation of:

- Nonlinear dynamic modeling
- Closed-loop control design
- Realistic actuator constraints
- Performance evaluation of PID controllers

It bridges control theory with industrial process applications.

---

---
