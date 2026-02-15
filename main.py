import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 1, 100)# Generate time vector
y = np.sin(t) # Generate a sine wave

plt.plot(t, y) # Plot the sine wave
plt.title('Environment test')
plt.xlabel('Time (s)')
plt.ylabel('signal')
plt.show() # Display the plot