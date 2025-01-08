import matplotlib.pyplot as plt
import numpy as np

# Function to calculate the next x value
def x_n(x, h):
    return x + h

# Function to calculate the first y value (y_1) using the first derivative
def y_1(y_0, dy, h):
    return h * dy + y_0  # dy is the first derivative of y at x=0

# Function to calculate subsequent y values using the finite difference method
def y_n(y_1, y_0, h, x_0):
    return y_1 * (2 - h * x_0) + y_0 * (1 + h * x_0 - h * h * x_0) + h * h * x_0

# Parameters
h = 0.1  # Step size
x_start = 0  # Starting x value
x_end = 2    # Ending x value
y_0 = 1      # Initial y value
dy = 0.5     # First derivative at x=0

# Initialize variables
x_values = [x_start]
y_values = [y_0]

# Calculate the first y value
y_first = y_1(y_0, dy, h)
y_values.append(y_first)

# Generate x and y values
x = x_start
while x < x_end:
    x = x_n(x, h)
    x_values.append(x)
    if len(y_values) > 1:
        y_next = y_n(y_values[-1], y_values[-2], h, x)
        y_values.append(y_next)

# Plot the graph
plt.plot(x_values, y_values, marker='o', label='Finite Difference Method')
plt.title('Graph of y vs. x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

