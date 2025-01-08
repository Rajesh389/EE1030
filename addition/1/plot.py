import numpy as np
import matplotlib.pyplot as plt

# Function to compute y and dy using Euler's method
def value(h):
    # Initial conditions
    x = 0.0
    y = np.zeros(52)
    dy = np.zeros(52)
    y[0] = 0.0  # Initial value of y
    dy[0] = 1.0 # Initial value of dy/dx

    # Euler's method loop
    for i in range(1, 52):
        # Compute the second derivative ddy
        ddy = x * x * dy[i - 1] + x - x * y[i - 1]
        
        # Update y and dy using Euler's method
        y[i] = y[i - 1] + h * dy[i - 1]
        dy[i] = dy[i - 1] + h * ddy

        # Increment x
        x += h

    return np.linspace(0, h * 51, 52), y

# Set step size
h = 0.1

# Get x and y values
x_vals, y_vals = value(h)

# Plotting the graph
plt.plot(x_vals, y_vals, label="y(x)")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Euler's Method Solution")
plt.legend()
plt.grid(True)
plt.show()

